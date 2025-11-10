# Drowsiness-Detection

## Project Description
This project detects driver drowsiness using computer vision technology. By analyzing webcam video in real time, it identifies signs of sleepiness and triggers an alarm to alert the driver, helping to prevent accidents caused by fatigue.

## Installation
To install and run this project, clone the repository and install the required Python packages:


git clone https://github.com/DHINESH0202/Drowsiness-Detection.git

cd Drowsiness-Detection

pip install -r requirements.txt


## Usage
Run the application using:
python app.py


Ensure your webcam is connected, as the program streams real-time video for drowsiness detection.

## How it Works
The system captures live video from the webcam, detects eye closure and other drowsiness indicators using Haarcascades and shape predictors, then plays an alarm sound if drowsiness is detected.

## Requirements
Please refer to the `requirements.txt` file to install all necessary dependencies.

## Contributing
Contributions are welcome! Fork the repository and submit pull requests. For issues or suggestions, please open an issue on GitHub.

## License
This project is licensed under the MIT License.

## Credits
Thanks to open-source libraries such as OpenCV, dlib, and playsound for enabling computer vision and audio features. The dataset used for training models is present in the `dataset` folder.
