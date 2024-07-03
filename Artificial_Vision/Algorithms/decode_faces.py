import cv2
import face_recognition as fr
import numpy as np
from .file_control import File_Control
from .face_region import Face_area

class decode_faces:
    def __init__(self):
        self.images_path = File_Control().dir_database()
        self.face_code = 0
        self.img = []
        self.id_user = []
        self.Face_coordenades = Face_area()
        self.identify_user()

    def encode_images(self, images):
        list_code = []
        for image in images:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cod = fr.face_encodings(image)[0]
            list_code.append(cod)
        return list_code

    def identify_user(self):
        list = os.listdir(self.images_path)
        for lis in list:
            img_db = cv2.imread(f'{self.images_path}/{lis}')
            self.img.append(img_db)
            self.id_user.append(os.path.splitext(lis)[0])
        self.face_code = self.encode_images(self.img)

    def process_frame(self, frame):
        precision_threshold = 0.7
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = fr.face_locations(frameRGB)
        faces_cod = fr.face_encodings(frameRGB, faces)

        for faces_cod, face_log in zip(faces_cod, faces):
            compare = fr.compare_faces(self.face_code, faces_cod)
            likeness = fr.face_distance(self.face_code, faces_cod)
            min_dat = np.argmin(likeness)

            if compare[min_dat] and likeness[min_dat] < precision_threshold:
                user_name = self.id_user[min_dat].upper()
                return True, user_name
        return False, None
