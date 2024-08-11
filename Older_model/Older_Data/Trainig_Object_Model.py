# Training Object Model (TOM)
# This Script was designed by Jesus Jimenez Barrera, Jennifer Enrique Becerril and Asaf Diaz Rivera
""" This script was designed with the purpose of developing a CNN model with which the main function in face
recognition could have a better level of security against identity fraud, (the code structure was based in Yolov3) """

# Program Libraries
from ultralytics import YOLO

model = YOLO('/home/yisus/Documents/Proyectos/Face_Detection/P-SRFOCA_1.0/Models/CNN/yolov8m.pt')
# /Modelos/yolov8l.pt

def main():
      model.train(data='/home/yisus/Downloads/movile_detection/data.yaml', epochs=30, batch=4)

if __name__ == '__main__':
    main()


