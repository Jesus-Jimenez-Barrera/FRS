# This Script was designed by Jesus Jimenez Barrera, Jennifer Enrique Becerril and Asaf Diaz Rivera
""" Script designed to extract a user's facial mesh """

# Program Libraries
import cv2
import time
import imutils
import mediapipe as mdpi

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

# Start of the class
class Extract_mesh:

    # Constructor Initialization
    def __init__(self):

        # Variables for Draw a Facial Mesh
        self.mpDraw = mdpi.solutions.drawing_utils
        self.ConfigDraw = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

        # Object Face Mesh
        self.FacemeshObject = mdpi.solutions.face_mesh
        self.FaceMesh = self.FacemeshObject.FaceMesh(max_num_faces=1)

        # Object Detect
        # Face Detection object from Mediapipe
        self.FaceObject = mdpi.solutions.face_detection

        # Initializing Face Detection
        self.detector = self.FaceObject.FaceDetection(min_detection_confidence=0.5, model_selection=1)
        self.video_cap = None
        self.Face_region = None

    # Function to only initialise capture the video
    def video_start(self):

        cap = detect_camera.find_camera()

        try:

            if cap is not None:

                #print('Se ha encontrado una camara en el indice: ', detect_camera)
                print('Inicializando la captura de video .... ')
                self.video_cap = cv2.VideoCapture(cap)

            else:

                print('No se pudo encontrar ninguna cámara')
                print('Porfavor revise la configuracion de si Hardware o contacte al desarrollador')

        except Exception as e:
            print('Ha ocurrido el siguiente error: ', e)


    # Function designed to generate a window where the facial mesh can be displayed.
    def extract_facial_mesh(self, user_id):

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
                frame = imutils.resize(frame, width=1080)

                # Convert frame to RGB
                frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Process frame to detect facial landmarks
                res = self.FaceMesh.process(frameRGB)

                if res.multi_face_landmarks:
                    for mesh_faces in res.multi_face_landmarks:

                        self.mpDraw.draw_landmarks(frame, mesh_faces, self.FacemeshObject.FACEMESH_CONTOURS,
                                                   self.ConfigDraw, self.ConfigDraw)

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

                        if cv2.waitKey(1) == 13:

                            self.Face_region = frameRGB[ymin:ymax, xmin:xmax]
                            time.sleep(2)
                            cv2.imwrite(f'{object_file.dir_database()}/{user_id}.png',
                                        cv2.cvtColor(self.Face_region, cv2.COLOR_RGB2BGR))
                            print('Foto guardada correctamente.')
                            self.video_cap.release()
                            cv2.destroyAllWindows()

                # Display frame with facial landmarks
                cv2.imshow('Captura de datos biometricos', frame)

                # Exit condition
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            self.video_cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
