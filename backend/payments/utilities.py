# ✉️ Utility to send confirmation email when payment is successful

from django.core.mail import send_mail           # 📤 Function to send emails
from checkout.models import Order                # 🛒 Import Order model to get order details
from django.conf import settings                 # ⚙️ Access email settings from Django settings


# ✅ Function to send success email after payment
def send_success_email(payment_intent_id):
    # 🔎 Get order details using the unique payment_intent_id
    order = Order.objects.get(payment_intent_id=payment_intent_id)

    # 📧 Send email with order information
    send_mail(
        subject=f"Order with payment ID {payment_intent_id} was placed",  # 📝 Email subject

        message=f"""
ordered items: {order.items}
total cost: {order.total}
        """,  # 📦 Email body with item list and total cost

        from_email=settings.EMAIL_HOST_USER,         # ✉️ Sender email (from Django settings)
        recipient_list=[settings.EMAIL_RECEIVER],    # 📬 Receiver email (you can set it in settings)
        fail_silently=False,  # 🚨 If there's an error, it should raise an exception
    )
