# Recognition Script (RS)
# This Script was designed by Jesus Jimenez Barrera, Jennifer Enrique Becerril and Asaf Diaz Rivera
""" This script was designed with the purpose of identifying a user in real time and average
of a query developed to the system's knowledge base, determining which user it is. """

# Program Libraries
import os
import cv2
import imutils
import numpy as np
import mediapipe as mdpi
from ultralytics import YOLO
import face_recognition as fr


# Instantiation of classes inherited from the control scripts
# Function used for initialize camera
from Camera_Scripts import Camera_Detector
detect_camera = Camera_Detector()
# Function used for work with the file control
from File_Control_Script import File_Control
object_file = File_Control()
# Function used for search a specific part of the frame (Face Region)
from Face_Region_Script import Face_area
Face_coordenades = Face_area()


class decode_faces:

    def __init__(self):

        self.images_path = object_file.dir_database()
        # Variables for Draw a Facial Mesh
        self.mpDraw = mdpi.solutions.drawing_utils
        self.connections = None
        self.ConfigDraw = self.mpDraw.DrawingSpec(color=(8, 150, 64), thickness=2, circle_radius=1)
        # Object Face Mesh
        self.FacemeshObject = mdpi.solutions.face_mesh
        self.FaceMesh = self.FacemeshObject.FaceMesh(max_num_faces=1)
        # Object Detect
        self.model = YOLO('/home/yisus/Documents/Proyectos/Face_Detection/P-SRFOCA_1.0/Models/CNN/phone3.pt')
        self.object = False
        # Face Detection object from Mediapipe
        self.FaceObject = mdpi.solutions.face_detection
        # Initializing Face Detection
        self.detector = self.FaceObject.FaceDetection(min_detection_confidence=0.5, model_selection=1)
        self.face_code = 0
        # Control arrays
        self.img = []
        self.id_user = []

    # Function used to encode the images and make a more effective reading
    def encode_images(self, images):

        list_code = []

        for images in images:

            images = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
            cod = fr.face_encodings(images)[0]
            list_code.append(cod)

        return list_code

    # Function by which records are searched and loaded for subsequent processing
    def identify_user(self):

        list = os.listdir(self.images_path)

        for lis in list:

            img_db = cv2.imread(f'{self.images_path}/{lis}')
            self.img.append(img_db)
            self.id_user.append(os.path.splitext(lis)[0])

        # print(self.id_user)
        self.face_code = self.encode_images(self.img)
        self.RTD()

    # Function designed for video outputs
    def information_output(self, frame, message, user_name=None, recognized=False):
        # Get the height and width of the frame
        height, width = frame.shape[:2]

        # Define colors based on recognition status
        if recognized:
            box_color = (29, 227, 107)  # Green
        else:
            box_color = (0, 0, 255)  # Red

        # Draw a box at the bottom of the frame
        cv2.rectangle(frame, (0, height - 50), (width, height), box_color, -1)

        # Define text color
        text_color = (0, 0, 0)  # Black

        # Add the output message
        cv2.putText(frame, message, (10, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 2)

        # If a user is recognized, display the user's name
        if user_name is not None:
            cv2.putText(frame, user_name, (10, height - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 2)

    # Function used to detect objects from a trained network, the model is based on Yolov8
    def Object_Detection(self, frame):
        css_model = ['cell-phone']
        resultsM = self.model(frame, stream=True, imgsz=416)

        for object in resultsM:
            boxesCap = object.boxes

            for boxCap in boxesCap:
                clsCap = int(boxCap.cls[0])

                if clsCap == 1:
                    return True

        return False

    # Function that initializes the video camera
    def video_start(self):

        # Variable created to control de access to the camera
        cap = detect_camera.find_camera()

        try:
            # If the function detect a device then the code start the capture of the data
            if cap is not None:
                print('Inicializando la captura de video .... ')
                self.video_cap = cv2.VideoCapture(cap)

            # If the function does not detect a device then the code will return the next result
            else:
                print('No se pudo encontrar ninguna cámara')
                print('Porfavor revise la configuracion de si Hardware o contacte al desarrollador')

        except Exception as e:
            print('Ha ocurrido el siguiente error: ', e)

    # Function designed to generate a window where the facial mesh can be displayed.
    def RTD(self):
        # Variable designed to control the level of precision
        precision_threshold = 0.7
        # History of eye position
        eye_position_history = []

        try:
            # Function to extract facial mesh from the webcam feed
            self.video_start()

            while True:
                # Reading a frame from the video capture
                ret, frame = self.video_cap.read()

                if not ret:
                    print('la captura del frame se ha interrumpido')
                    break

                # Resize frame for display
                frame = imutils.resize(frame, width=720)
                # Convert frame to RGB
                frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Object detection
                detect_objects = self.Object_Detection(frame.copy())

                # Check if a cell phone is detected
                if detect_objects:

                    user_name = None
                    message = 'Se ha detectado un dispositivo movil (Verificasion invalida)'
                    recognized = False
                    self.information_output(frame, message, user_name, recognized)

                else:

                    # Process frame to detect facial landmarks
                    res = self.FaceMesh.process(frameRGB)

                    if res.multi_face_landmarks:
                        for mesh_faces in res.multi_face_landmarks:

                            self.mpDraw.draw_landmarks(frame, mesh_faces, self.FacemeshObject.FACEMESH_CONTOURS,
                                                       self.connections, self.ConfigDraw)

                            # Get face region
                            xmin, xmax, ymin, ymax = Face_coordenades.get_face_region(res, frame.shape[1], frame.shape[0])

                            if xmin != -1:
                                # Draw rectangle around the face
                                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)

                                # Extract Points
                                px = []
                                py = []
                                listR = []

                                for id, points in enumerate(mesh_faces.landmark):
                                    # Looping through each landmark point in the facial mesh
                                    height, wide, c = frame.shape
                                    x, y = int(points.x * wide), int(points.y * height)
                                    px.append(x)
                                    py.append(y)
                                    listR.append([id, x, y])

                                    # Control designed to calculate eye lengths
                                    if len(listR) == 468:
                                        # Estimation points calculated according to the position where the face is detected
                                        x1, y1 = listR[145][1:]
                                        x2, y2 = listR[159][1:]

                                        # Calculation of historical eye position
                                        eye_x, eye_y = int((x1 + x2) / 2), int((y1 + y2) / 2)
                                        eye_position_history.append((eye_x, eye_y))

                                        # Verify if user look to the camera
                                        if len(eye_position_history) > 10:
                                            deviation = max(abs(eye_x - mean_x) for mean_x, _ in eye_position_history[-10:])

                                            # If a movement is made by the user, the system will detect the change
                                            if deviation > 20:
                                                print('Usuario No esta viendo a la camara. Reiniciando...')
                                                eye_position_history = []

                                            else:
                                                # Recognition variables
                                                faces = fr.face_locations(frameRGB)
                                                faces_cod = fr.face_encodings(frameRGB, faces)

                                                for faces_cod, face_log in zip(faces_cod, faces):

                                                    compare = fr.compare_faces(self.face_code, faces_cod)
                                                    likeness = fr.face_distance(self.face_code, faces_cod)

                                                    min_dat = np.argmin(likeness)

                                                    if compare[min_dat] and likeness[min_dat] < precision_threshold:
                                                        user_dat = self.id_user[min_dat].upper()
                                                        user_name = user_dat
                                                        message = None
                                                        recognized = True
                                                        self.information_output(frame, message, user_name, recognized)
                                                    else:
                                                        user_name = None
                                                        message = 'Usuario no reconocido'
                                                        recognized = False
                                                        self.information_output(frame, message, user_name, recognized)

                # Display frame with facial landmarks and object detection
                cv2.imshow('Captura de datos biometricos', frame)

                # Exit condition
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            self.video_cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')


if __name__ == "__main__":
    recognizer = decode_faces()
    recognizer.identify_user()