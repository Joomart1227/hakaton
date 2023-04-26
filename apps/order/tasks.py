from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_confirmation_mail(username, address, pk, email):
    message = f"""
    Zdravstvuite, {username}!
    Podtverdite zakaz na adres {address},

    http://localhost8000/order/{pk}/confirm/

    Esli eto byli ne Vy, ignoriruite eto soobshenie 
    """
    send_mail(
        subject='Podtverjdenie zakaza',
        message=message,
        from_email='test@test.com',
        recipient_list=[email],
        fail_silently=False
    )