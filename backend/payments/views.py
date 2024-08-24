from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.template import Context, Template
from django.utils.html import mark_safe
from django.views.decorators.csrf import csrf_protect

from django.conf import settings

from .utils import encrypt, decrypt
from .models import Transaction
from checkout.models import Order


@csrf_protect
def index(request):
    # order = Order.objects.get(user=request.user, placed=False)
    # amount = order.total
    # address = order.address

    return render(
        request,
        "payments/dataForm.html",
    )  # {"amount": amount, "address": address})


class CCAVRequestHandler(View):
    def post(self, request, *args, **kwargs):
        global encryption

        order = Order.objects.get(request.user, placed=False)

        p_merchant_id = settings.MERCHANT_ID
        p_order_id = order.order_id
        p_currency = "INR"
        p_amount = order.total
        p_redirect_url = "websire_main_url"
        p_cancel_url = "websire_main_url"
        # p_language = request.POST.get("language")
        # p_billing_name = request.POST.get("billing_name")
        # p_billing_address = request.POST.get("billing_address")
        # p_billing_city = request.POST.get("billing_city")
        # p_billing_state = request.POST.get("billing_state")
        # p_billing_zip = request.POST.get("billing_zip")
        # p_billing_country = request.POST.get("billing_country")
        p_billing_tel = order.phone_no
        p_billing_email = order.username
        p_delivery_name = request.POST.get("delivery_name")
        p_delivery_address = order.address
        # p_delivery_city = request.POST.get("delivery_city")
        # p_delivery_state = request.POST.get("delivery_state")
        p_delivery_zip = order.pin_code
        # p_delivery_country = request.POST.get("delivery_country")
        # p_delivery_tel = request.POST.get("delivery_tel")
        # p_merchant_param1 = request.POST.get("merchant_param1")
        # p_merchant_param2 = request.POST.get("merchant_param2")
        # p_merchant_param3 = request.POST.get("merchant_param3")
        # p_merchant_param4 = request.POST.get("merchant_param4")
        # p_merchant_param5 = request.POST.get("merchant_param5")
        # p_integration_type = request.POST.get("integration_type")
        # p_promo_code = request.POST.get("promo_code")
        # p_customer_identifier = request.POST.get("customer_identifier")

        transaction_details = Transaction(
            p_merchant_id=p_merchant_id,
            p_order_id=p_order_id,
            p_currency=p_currency,
            p_amount=p_amount,
            p_redirect_url=p_redirect_url,
            p_cancel_url=p_cancel_url,
            # p_language=p_language,
            # p_billing_name=p_billing_name,
            # p_billing_address=p_billing_address,
            # p_billing_city=p_billing_city,
            # p_billing_state=p_billing_state,
            # p_billing_zip=p_billing_zip,
            # # p_billing_country=p_billing_country,
            p_billing_tel=p_billing_tel,
            p_billing_email=p_billing_email,
            p_delivery_name=p_delivery_name,
            p_delivery_address=p_delivery_address,
            # p_delivery_city=p_delivery_city,
            # p_delivery_state=p_delivery_state,
            p_delivery_zip=p_delivery_zip,
            # p_delivery_country=p_delivery_country,
            # p_delivery_tel=p_delivery_tel,
            # p_merchant_param1=p_merchant_param1,
            # p_merchant_param2=p_merchant_param2,
            # p_merchant_param3=p_merchant_param3,
            # p_merchant_param4=p_merchant_param4,
            # p_merchant_param5=p_merchant_param5,
            # p_integration_type=p_integration_type,
            # p_promo_code=p_promo_code,
            # p_customer_identifier=p_customer_identifier,
        )
        transaction_details.save()

        merchant_data = (
            f"merchant_id={p_merchant_id}&"
            f"order_id={p_order_id}&"
            f"currency={p_currency}&"
            f"amount={p_amount}&"
            f"redirect_url={p_redirect_url}&"
            f"cancel_url={p_cancel_url}&"
            f"billing_tel={p_billing_tel}&"
            f"billing_email={p_billing_email}&"
            f"delivery_name={p_delivery_name}&"
            f"delivery_address={p_delivery_address}&"
            f"delivery_zip={p_delivery_zip}&"
        )
        # Add any other merchant_data parameters here

        workingKey = settings.WORKING_KEY
        encryption = encrypt(merchant_data, workingKey)

        html = """
        <html>
        <head>
            <title>Sub-merchant checkout page</title>
            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
        </head>
        <body>
            <center>
            <iframe width="482" height="500" scrolling="No" frameborder="0" id="paymentFrame" src="https://test.ccavenue.com/transaction/transaction.do?command=initiateTransaction&merchant_id={{ mid }}&encRequest={{ encReq }}&access_code={{ xscode }}"></iframe>
            </center>
            <script type="text/javascript">
                $(document).ready(function(){
                    $('iframe#paymentFrame').load(function() {
                         window.addEventListener('message', function(e) {
                             $("#paymentFrame").css("height", e.data['newHeight'] + 'px');  
                         }, false);
                     }); 
                });
            </script>
          </body>
        </html>
        """

        context = {
            "mid": settings.MERCHANT_ID,
            "encReq": encryption,
            "xscode": settings.ACCESS_CODE,
        }

        template = Template(html)
        context_instance = Context(context)
        rendered_html = mark_safe(template.render(context_instance))

        return HttpResponse(rendered_html)
