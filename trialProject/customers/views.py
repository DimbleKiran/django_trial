from django.shortcuts import render
from .forms import CustomerForms
from .models import Customer
import cv2
from django.http import HttpResponse

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import StreamingHttpResponse


def customer_views_forms(r):
    cust_user = CustomerForms
    if r.method == "POST":
        forms = CustomerForms(r.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponse('<h1>Successful...</h1>')
    return render(r, "customers/customer_forms.html", {"cust_user": cust_user})


def customer_views_table(r):
    table = Customer.objects.all()
    return render(r, 'customers/customer_table.html', {"table": table})


def video_feed(request):
    cap = cv2.VideoCapture(0)

    def generate():
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            _, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

        cap.release()
    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')


def save_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        path = default_storage.save('captured_images/' + image.name, ContentFile(image.read()))
        return path
    else:
        return None