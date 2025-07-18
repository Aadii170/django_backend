import uuid

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from store.models import Products, Phones

# ===================================================
# 🛒 CartItem Model
# ➤ Represents one product added to a user's cart
# ===================================================
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 🔗 Linked to the user who added this item
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)  # 📦 Linked to the selected product


# ===================================================
# 📦 Order Model
# ➤ Stores complete order details after checkout
# ===================================================
class Order(models.Model):
    order_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # 🔑 Unique order ID using UUID//     # 🔒 Server-generated (auto)

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 👤 Order placed by this user  # 🔒 Server-generated (auto)
    name = models.CharField(max_length=50)  # 🧾 Customer name            # ✅ User se aata hai
    address = models.CharField(max_length=150)  # 🏠 Delivery address     # ✅ User se aata hai

    pin_code = models.IntegerField(
        validators=[MaxValueValidator(999999), MinValueValidator(000000)]
    )  # 📮 Pincode with 6-digit validation                                # ✅ User se aata hai

    phone_model = models.ForeignKey(
        Phones, on_delete=models.SET_NULL, blank=True, null=True
    )  # 📱 Optional phone model for customized cover                       # ✅ User se aata hai

    phone_no = models.BigIntegerField()  # 📞 Contact number           # ✅ User se aata hai

    is_custom = models.BooleanField(default=False)  # 🎨 Is the product custom-designed?    
    name_on_cover = models.CharField(
        max_length=100, blank=True, null=True, default=""
    )  # ✍️ Optional name on the phone cover

    image = models.ImageField(
        upload_to="images/customize", blank=True, null=True, default=None
    )  # 🖼️ Optional image for custom design

    # 🧾 JSONField to store list of item/product IDs (works in all databases)
    items = models.JSONField(
        default=list, blank=True, null=True
    )  # 📦 Example: [1, 2, 3] — list of product IDs           # 🔒 Server calculate karta hai

    total = models.FloatField()  # 💰 Total price of the order  # 🔒 Server calculate karta hai

    payment_option = models.CharField(
        max_length=50,
        default="ONLINE",
        choices=[("COD", "COD"), ("ONLINE", "ONLINE")],
    )  # 💳 Payment method: Cash on Delivery or Online

    placed = models.BooleanField(default=False)  # ✅ Whether the order is placed or still pending
