# Jarbas self driving-car
This project aims to develop a self-driving robot car.
The platform is based on Picar-V and Raspberry Pi. Self-driving is based on image processing and CNN.

Steps:
1. Control car with a PS3 remote control
2. Calibrate camera and collect images for training
3. Preprocess images to feed the DNN
4. Build and train a DNN
5. Use DNN to drive the robot car


References:
DeepPiCar: https://towardsdatascience.com/deeppicar-part-1-102e03c83f2c
Behavioural Cloning — End to End Learning for Self-Driving Cars: https://medium.com/swlh/behavioural-cloning-end-to-end-learning-for-self-driving-cars-50b959708e59

## Project structure
- **calibration**: scripts to execute on the Jarbas to calibrate the camera and gather points for perspective transformation. A calibration file will be created with these parameters
- **remote-control**: scripts to control Jarbas via PS3 gamepad. Required for image gathering
- **self-driving**: Jarbas self-driving related scripts
- **model**: Neural Network model and training related stuff

