import base64
from PIL import Image
from io import BytesIO
from flask import Flask, render_template, request, jsonify
from flask_session import Session
from super_gradients.training import models
import os
import torch
import serial
import time
import threading
import random

# Configuración de Arduino
play = 0
ser = serial.Serial('COM6', 9600)
cleaned_data = ""
time.sleep(2)

# Archivo de registro
LOG_FILE_PATH = 'arduino_log.txt'

def log_to_file(message):
    """Registra un mensaje en el archivo de texto."""
    with open(LOG_FILE_PATH, 'a') as log_file:
        log_file.write(f"{message}\n")

def send_to_arduino(data):
    """Envía datos al Arduino y registra el mensaje en un archivo de texto."""
    ser.write(data.encode())
    log_to_file(data)  # Registrar el mensaje enviado

# Función para manejar la lectura del puerto serial de manera asincrónica
def async_read_serial():
    while True:
        data = ser.readline().decode('utf-8').strip()
        if data.startswith("###"):
            cleaned_data = data[3:]
            print(f"Data from Arduino: {cleaned_data}")

# Crear y empezar el hilo para la lectura serial
serial_thread = threading.Thread(target=async_read_serial, daemon=True)
serial_thread.start()

# Configuración del modelo
CHECKPOINT_DIR = 'checkpoints'
os.makedirs('inference_results', exist_ok=True)

device = torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")

model = models.get(
    model_name='yolo_nas_s',
    checkpoint_path='ckpt_best.pth',
    num_classes=1,
).to(device)

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Nombre fijo para el archivo de la imagen recibida
TEMP_IMAGE_PATH = 'images/current_frame.jpg'
RESULT_IMAGE_PATH = 'inference_results/current_result.jpg'

def is_image_valid(file_path):
    """Verifica si la imagen está completa y es válida."""
    try:
        with Image.open(file_path) as img:
            img.verify()  # Verifica la integridad de la imagen
        return True
    except (IOError, SyntaxError) as e:
        print(f"Image verification failed: {e}")
        return False

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/get_frame', methods=['POST'])
def get_frame():
    global play, cleaned_data
    try:
        frame_data = request.form.get('frame')
        binary_data = base64.b64decode(frame_data.split(',')[1])

        # Guardar la imagen recibida en un archivo temporal
        with open(TEMP_IMAGE_PATH, 'wb') as f:
            f.write(binary_data)

        # Verificar la validez de la imagen
        while not is_image_valid(TEMP_IMAGE_PATH):
            print("Image is not valid. Waiting...")
            time.sleep(0.5)  # Esperar medio segundo antes de volver a verificar

        # Procesar la imagen
        with Image.open(TEMP_IMAGE_PATH) as new:
            new = new.rotate(90, expand=True)
            new.save(TEMP_IMAGE_PATH)

        # Realizar inferencia en la imagen recibida
        out = model.predict(TEMP_IMAGE_PATH)
        prediction = out._images_prediction_lst[0].prediction
        boxes = prediction.bboxes_xyxy

        if boxes is not None and len(boxes) > 0:
            first_box = boxes[0]
            point = first_box[1] - first_box[0]
            print(point)
            
            if play == 0:
                send_to_arduino("w")
                play = 1
            else:
                play = 0
                if point < 320:
                    send_to_arduino("a")
                elif point > 320:
                    send_to_arduino("d")
                else:
                    send_to_arduino("w")
        else:
            print("No objects detected.")
            
            if play == 0:
                send_to_arduino("w")
                play = 1
            else:
                numero_aleatorio = random.randint(1, 2)
                if numero_aleatorio == 1:
                    send_to_arduino("a")
                else:
                    send_to_arduino("d")
                play = 0

        # Guardar los resultados de inferencia
        out.save(RESULT_IMAGE_PATH)

        return jsonify({"message": "Frame received and processed successfully"}), 200
    except Exception as e:
        print(f"Error processing frame: {e}")
        return jsonify({"message": "Failed to process frame"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context=("cert/server.cer", "cert/server.key"))
