from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.template import Context, Template
from django.utils.html import mark_safe
from django.views.decorators.csrf import csrf_protect

from django.conf import settings

from .utils import encrypt
from .models import Transaction
from checkout.models import Order


# 🎯 Renders the payment form with amount and address for the logged-in user
@csrf_protect
def index(request):
    # 🔐 Check if user is authenticated
    if not request.user.is_authenticated:
        return HttpResponse("You must be logged in.", status=401)

    # 📦 Fetch the active (not yet placed) order for the user
    order = Order.objects.filter(user=request.user, placed=False).first()
    if not order:
        return HttpResponse("No active order found for this user.", status=404)

    # 💰 Extract amount and 📍 address to show in payment form
    amount = order.total
    address = order.address

    # 🖼️ Render the payment form template with order details
    return render(request, "payments/dataForm.html", {"amount": amount, "address": address})


# 🎯 Handles the actual payment request and redirects to CCAvenue payment page
class CCAVRequestHandler(View):
    def post(self, request, *args, **kwargs):
        # 📦 Get the current unplaced order for the user
        order = Order.objects.get(user=request.user, placed=False)

        # 🏦 Basic Payment Gateway Details
        p_merchant_id = settings.MERCHANT_ID
        p_order_id = order.order_id
        p_currency = "INR"
        p_amount = order.total
        p_redirect_url ="websire_main_url"  # ✅ Successful payment callback
        p_cancel_url ="websire_main_url"    # ❌ Failed/cancelled payment callback

        # 🧾 Billing and delivery information
        p_billing_tel = order.phone_no
        p_billing_email = order.username
        p_delivery_name = request.POST.get("delivery_name")
        p_delivery_address = order.address
        p_delivery_zip = order.pin_code

        # 💾 Save the transaction details in the database
        transaction_details = Transaction(
            p_merchant_id=p_merchant_id,
            p_order_id=p_order_id,
            p_currency=p_currency,
            p_amount=p_amount,
            p_redirect_url=p_redirect_url,
            p_cancel_url=p_cancel_url,
            p_billing_tel=p_billing_tel,
            p_billing_email=p_billing_email,
            p_delivery_name=p_delivery_name,
            p_delivery_address=p_delivery_address,
            p_delivery_zip=p_delivery_zip,
        )
        transaction_details.save()

        # 🔐 Prepare and encrypt merchant data to send to CCAvenue
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

        working_key = settings.WORKING_KEY
        encryption = encrypt(merchant_data, working_key)

        # 🧾 CCAvenue iframe to load the hosted payment page
        html = """
        <html>
        <head>
            <title>Sub-merchant checkout page</title>
            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
        </head>
        <body>
            <center>
                <iframe width="482" height="500" scrolling="No" frameborder="0" id="paymentFrame" 
                src="https://test.ccavenue.com/transaction/transaction.do?command=initiateTransaction&merchant_id={{ mid }}&encRequest={{ encReq }}&access_code={{ xscode }}">
                </iframe>
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

        # 📦 Pass the encrypted request and credentials to the iframe template
        context = {
            "mid": settings.MERCHANT_ID,
            "encReq": encryption,
            "xscode": settings.ACCESS_CODE,
        }

        # 🖥️ Render the HTML template with dynamic context
        template = Template(html)
        context_instance = Context(context)
        rendered_html = mark_safe(template.render(context_instance))

        return HttpResponse(rendered_html)
