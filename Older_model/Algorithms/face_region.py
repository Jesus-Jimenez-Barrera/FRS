class Face_area:
    def __init__(self):
        pass

    def get_face_region(self, res, width, height):
        try:
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

            xmin -= int(0.1 * (xmax - xmin))
            xmax += int(0.1 * (xmax - xmin))
            ymin -= int(0.1 * (ymax - ymin))
            ymax += int(0.1 * (ymax - ymin))

            xmin = max(0, xmin)
            ymin = max(0, ymin)
            xmax = min(width, xmax)
            ymax = min(height, ymax)

            return xmin, xmax, ymin, ymax
        except Exception as e:
            print(f'Ha ocurrido el siguiente error: {e}')
