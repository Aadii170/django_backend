from django.db import models

from checkout.models import Order


# Create your models here.
class Transaction(models.Model):
    p_merchant_id = models.CharField(max_length=10)
    p_order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    p_currency = models.CharField(max_length=50)
    p_amount = models.CharField(max_length=50)
    p_redirect_url = models.CharField(max_length=50)
    p_cancel_url = models.CharField(max_length=50)
    p_language = models.CharField(max_length=50)
    p_billing_name = models.CharField(max_length=50)
    p_billing_address = models.CharField(max_length=50)
    p_billing_city = models.CharField(max_length=50)
    p_billing_state = models.CharField(max_length=50)
    p_billing_zip = models.CharField(max_length=50)
    p_billing_country = models.CharField(max_length=50)
    p_billing_tel = models.CharField(max_length=50)
    p_billing_email = models.CharField(max_length=50)
    p_delivery_name = models.CharField(max_length=50)
    p_delivery_address = models.CharField(max_length=50)
    p_delivery_city = models.CharField(max_length=50)
    p_delivery_state = models.CharField(max_length=50)
    p_delivery_zip = models.CharField(max_length=50)
    p_delivery_country = models.CharField(max_length=50)
    p_delivery_tel = models.CharField(max_length=50)
    p_merchant_param1 = models.CharField(max_length=50)
    p_merchant_param2 = models.CharField(max_length=50)
    p_merchant_param3 = models.CharField(max_length=50)
    p_merchant_param4 = models.CharField(max_length=50)
    p_merchant_param5 = models.CharField(max_length=50)
    p_integration_type = models.CharField(max_length=50)
    p_promo_code = models.CharField(max_length=50)
    p_customer_identifier = models.CharField(max_length=50)

    def __str__(self):
        return self.p_order_id
