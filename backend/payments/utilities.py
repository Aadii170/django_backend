# utilities.py
from django.core.mail import send_mail

from checkout.models import Order
from django.conf import settings


def send_success_email(payment_intent_id):
    send_mail(
        f"Order with payment ID {payment_intent_id} was placed",
        f"""
ordered items: {Order.objects.get(payment_intent_id=payment_intent_id).items}
total cost: {Order.objects.get(payment_intent_id=payment_intent_id).total}
        """,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_RECEIVER],
        fail_silently=False,
    )
