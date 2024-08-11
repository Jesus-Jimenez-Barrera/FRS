# This Script was designed by Jesus Jimenez Barrera, Jennifer Enrique Becerril and Asaf Diaz Rivera
""" Script designed to search the facial area in a video in real time. """

# Start of the class
class Face_area:

    # Constructor (Could be used later)
    def __init__(self):
        pass

    # Function designed to obtain a specific area of the face
    def get_face_region(self, res, width, height):

        try:
            # Function to get the region of the detected face
            xmin, xmax = width, 0
            ymin, ymax = height, 0

            for face_landmarks in res.multi_face_landmarks:
                for landmark in face_landmarks.landmark:
                    x, y = int(landmark.x * width), int(landmark.y * height)
                    if x < xmin:
                        xmin = x
                    if x > xmax:
                        xmax = x
                    if y < ymin:
                        ymin = y
                    if y > ymax:
                        ymax = y

            if xmin == xmax or ymin == ymax:
                return -1, -1, -1, -1

            # Adjust coordinates to get a larger region
            xmin -= int(0.1 * (xmax - xmin))
            xmax += int(0.1 * (xmax - xmin))
            ymin -= int(0.1 * (ymax - ymin))
            ymax += int(0.1 * (ymax - ymin))

            # Image bounds
            xmin = max(0, xmin)
            ymin = max(0, ymin)
            xmax = min(width, xmax)
            ymax = min(height, ymax)

            return xmin, xmax, ymin, ymax

        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')



