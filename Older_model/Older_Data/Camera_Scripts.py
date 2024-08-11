""" Script designed to check if the camera can be accessed """
# This Script was designed by Jesus Jimenez Barrera, Jennifer Enrique Becerril and Asaf Diaz Rivera

# Libraries
import cv2
import platform

# Beginning of the camera detector class
class Camera_Detector:

    # Constructor initialization
    def __init__(self):
        self.system = platform.system()

    # Method to search for video output taking into account the operating system
    def find_camera(self):

        cam_index = None

        # Search the camera in Windows
        if self.system == 'Windows':
            for i in range(10):
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    cam_index = i
                    cap.release()
                    break

        # Search the camera in Linux
        elif self.system == 'Linux':
            for i in range(10):
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    cam_index = i
                    cap.release()
                    break

        return cam_index
