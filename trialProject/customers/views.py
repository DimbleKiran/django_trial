from django.shortcuts import render
from .forms import CustomerForms
from .models import Customer
import cv2
from django.http import HttpResponse
import os

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import StreamingHttpResponse


def customer_views_forms(r):
    cust_user = CustomerForms
    if r.method == "POST":
        forms = CustomerForms(r.POST, r.FILES)
        print(forms)
        if forms.is_valid():
            forms.save()
            # return HttpResponse('<h1>Successful...</h1>')
    return render(r, "customers/customer_forms.html", {"cust_user": cust_user})


def customer_views_table(r):
    table = Customer.objects.all()
    return render(r, 'customers/customer_table.html', {"table": table})


def video_feed(request):
    cap = cv2.VideoCapture(0)
    saved_image_path = r'C:\Users\IT\Desktop'

    def mouse_click_event(event, x, y, flags, param):
        global image_path
        if event == cv2.EVENT_LBUTTONDOWN:  # Check if left mouse button is clicked
            print(f"Mouse clicked at coordinates ({x}, {y})")
            # Save the entire frame
            image_path = os.path.join(saved_image_path, f'clicked_image_{x}_{y}.jpg')
            resized_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            cv2.imwrite(image_path, resized_frame)
            return image_path

    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', mouse_click_event)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('frame', frame)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q') or key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    return HttpResponse(f"Image saved at: {image_path}")


# def save_image(request):
#     if request.method == 'POST' and 'image' in request.FILES:
#         image = request.FILES['image']
#         path = default_storage.save('captured_images/' + image.name, ContentFile(image.read()))
#         return path
#     else:
#         return None
