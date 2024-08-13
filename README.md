# BinBot-AIGarbageCollector

### Introduction:
Every day, the accumulation of litter in our streets and public spaces is a global challenge. Despite awareness efforts, the sheer volume of waste requires innovative solutions. This project proposes a transformative response: the use of AI-powered autonomous robots for litter collection in urban environments and offices.

![This is an alt text.](https://i.ibb.co/Krzx2ks/Sin-nombre.png "This is a sample image.")

### Project Vision:
Imagine a future where autonomous robots patrol our streets, parks, and offices, equipped with advanced AI to recognize and collect solid waste such as bottles, disposable plastics, papers, and masks. These robots would operate independently, identifying and collecting trash before transporting it to designated collection centers.

![This is an alt text.](https://i.ibb.co/HnJGdF5/image1.png "This is a sample image.")

## Impact and Feasibility:

* **Impact Potential:** This solution will directly contribute to environmental sustainability, reducing pollution and improving recycling efforts. By deploying robots in public spaces, global initiatives to combat climate change will be supported.
* **Feasibility:** By leveraging existing technologies, the project is practical and feasible. With further investment, AI models could be refined and robot capabilities improved.
* **Originality:** The unique combination of AI and autonomous robotics for waste detection and collection offers a novel solution that could revolutionize waste management.
* **Expandability:** Designed to be scalable, the project has the potential to deploy robot networks in cities around the world, with applications in a variety of settings.
* **Inclusive Design:** The project addresses a universal problem and is applicable in a variety of settings, from public parks to offices, ensuring broad benefits.
![This is an alt text.](https://i.ibb.co/YkYpxMB/1.jpg "This is a sample image.")
![This is an alt text.](https://i.ibb.co/ZSmznCv/pred-0.jpg "This is a sample image.")
![This is an alt text.](https://i.ibb.co/PTV5D6t/3.jpg "This is a sample image.")

## Technical Details:
The AIs were trained on approximately 2,000 images collected manually and labeled with Labelme via Conda. A retrained *YOLO NAS S* model in PyTorch was used to recognize litter. The current prototype of the robot, built with Arduino, functions as a litter patrol using a camera and front sensors to move freely.
![This is an alt text.](https://i.ibb.co/pw60jTn/Screenshot-2.png "This is a sample image.")

## Prototype and Future Improvements:
Currently, the robot communicates with a central server via Wi-Fi using a cell phone camera, although ideally it should have its own camera. Future improvements could include installing more sensors for better recognition of the environment, more powerful motors, larger tires, and wireless connection alternatives such as Bluetooth.
![This is an alt text.](https://i.ibb.co/6tVCxps/Screenshot-3.png "This is a sample image.")

## Implementation:
Installing the program requires a few technical steps:

1. Clone this repository.
2. Select the AI model you want to test, there are the folders **"AI for offices and salons"** and **"AI for parks and streets"** inside each one you will find a .zip file that you must unzip and leave a ckpt_best.pth file, drag the unzipped file from the folder of the model you want to use to the main folder along with the app.py.
3. Create a virtual environment and install the dependencies from the requirements.txt file (Some packages need specific versions of python, I recommend using Python 3.8.10)
4. Download OpenSSL to create your license and key. Then create a folder called "cert" and place the files there.
5. Run the app.py file and go to the *https://* page shown in app.py (The code requires the robot to establish the connection with the server, but if you remove the part of the code that uses the serial communication, the problems will be solved)
6. Observe the results of the detection in real time inside the inferece_results folder and the movements of the robot in the arduino_log.txt file


This project has the potential to revolutionize waste management on a global scale. With sufficient resources and time, significant advances in sustainability could be achieved, including the possibility of making robots completely autonomous with the installation of solar panels. The future of waste management could be driven by AI and autonomous robotics, marking a positive change in the fight against pollution and climate change.
