from django.shortcuts import render
import base64
import cv2
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .Algorithms.decode_faces import decode_faces

@csrf_exempt
def capture_image(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            image_data = data['image'].split(',')[1]
            image_bytes = base64.b64decode(image_data)
            nparr = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            recognizer = decode_faces()
            recognizer.identify_user()
            recognized, user_name = recognizer.process_frame(img)

            response = {
                'recognized': recognized,
                'message': 'Usuario reconocido' if recognized else 'Usuario no reconocido',
                'user_name': user_name if recognized else None
            }
            return JsonResponse(response)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'Artificial_Vision/capture_image.html')
