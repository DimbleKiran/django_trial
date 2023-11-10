from django.shortcuts import render
from .forms import CustomerForms, CustomerDetailsForms
from .models import Customer, CustomerDetails
import cv2
from django.http import HttpResponse, HttpResponseRedirect
import os
from django.contrib import messages
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from django.http import StreamingHttpResponse


def customer_views_forms(r):
    cust_user = CustomerForms
    if r.method == "POST":
        forms = CustomerForms(r.POST, r.FILES)
        if forms.is_valid():
            forms.save()
            r.session['show_success_message'] = True
            # messages.success(r, 'Form submitted successfully!')
            return HttpResponseRedirect('/customers/customerforms/')
    else:
        # Handle the case when it's not a POST request (e.g., GET request)
        cust_user = CustomerForms
    show_success_message = r.session.pop('show_success_message', False)
    return render(r, "customers/customer_forms.html", {"cust_user": cust_user, 'show_success_message': show_success_message})


def customer_views_table(r):
    table = Customer.objects.all()
    return render(r, 'customers/customer_table.html', {"table": table})


def delete(r, id):
    obj = Customer.objects.get(id=id)
    if obj.photo:
        if os.path.exists(obj.photo.path):
            os.remove(obj.photo.path)
    obj.delete()
    return HttpResponseRedirect('/customers/customertables/')


def customer_details_view_form(r):
    cust_details = CustomerDetailsForms
    if r.method == "POST":
        cus_det_forms = CustomerDetailsForms(r.POST)
        if cus_det_forms.is_valid():
            cus_det_forms.save()
            print('Saved')
    return render(r, "customers/customer_details_forms.html", {"cust_details": cust_details})


def customer_details_table(r):
    table1 = CustomerDetails.objects.all()
    return render(r, "customers/customer_details_table.html", {"table1": table1})


def video_feed(r):
    cap = cv2.VideoCapture(0)
    saved_image_path = r'C:\Users\IT\Desktop'
    image_path = 'IMAGE NOT SAVED'

    def mouse_click_event(event, x, y, flags, param):
        nonlocal image_path
        if event == cv2.EVENT_LBUTTONDOWN:  # Check if left mouse button is clicked
            print(f"Mouse clicked at coordinates ({x}, {y})")
            # Save the entire frame
            image_path = os.path.join(saved_image_path, f'clicked_image_{x}_{y}.jpg')
            resized_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            if resized_frame is not None and resized_frame.shape[0] > 0 and resized_frame.shape[1] > 0:
                cv2.imwrite(image_path, resized_frame)
                messages.success(r, f"Image saved at: {image_path}")
                return image_path

            else:
                messages.success(r, image_path)
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

    # messages.success(r, f"Image : {image_path}")

    return HttpResponse(f"Image : {image_path}")




