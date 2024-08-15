int echoPin = 12;
int trigPin = 13;
int pingTravelTime;
int d;

int IN1 = 5;
int IN2 = 4;
int IN3 = 2;
int IN4 = 3;

void setup() {
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  
  // Inicializa el generador de números aleatorios
  randomSeed(analogRead(0));
}

void loop() {
  if (Serial.available() > 0) {
    char input = Serial.read();
  
    if (input == 'w') {
      Adelantar();
    }
    if (input == 's') {
      Retroceder();
    }
    if (input == 'a') {
      Izquierda();
    }
    if (input == 'd') {
      Derecha();
    }
    if (input == 'p') {
      Stop();
    }
    if (input == 'g') {
      Girar();
    }
    if (input == 'q') {
      Aleatorio();
    }
    if (input == 'f') {
      sensor();
    }
  }
}

void Adelantar() {
  // Adelantar
  // Dirección motor A
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  // Dirección motor B
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  delay(1000); // Tiempo para moverse (ajusta según sea necesario)

  Stop(); // Detener los motores
}

void Retroceder() {
  // Retroceder
  // Dirección motor A
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  // Dirección motor B
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  // delay(1000); // Tiempo para moverse (ajusta según sea necesario)

  Stop(); // Detener los motores
}

void Derecha() {
  // Girar a la derecha
  // Dirección motor A
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  // Dirección motor B
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  delay(300); // Tiempo para moverse (ajusta según sea necesario)

  Stop(); // Detener los motores
}

void Izquierda() {
  // Girar a la izquierda
  // Dirección motor A
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  // Dirección motor B
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  delay(300); // Tiempo para moverse (ajusta según sea necesario)

  Stop(); // Detener los motores
}

void Stop() {
  // Detener los motores
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, HIGH);
}

void Girar() {
  // Girar
  // Dirección motor A
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  // Dirección motor B
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  delay(1400); // Tiempo para moverse (ajusta según sea necesario)

  Stop(); // Detener los motores
}

void Aleatorio() {
	int direccion = random(2);
	if (direccion == 0) {
	  Derecha();
	} else if (direccion == 1) {
	  Izquierda();
	}
}

void sensor() {
  long t;
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  t = pulseIn(echoPin, HIGH);
  d = t / 59;
  Serial.print("###");
  Serial.println(d);
  
}