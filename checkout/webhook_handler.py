from django.http import HttpResponse


class StripeWH_Handler():
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succedeed(self, event):
        """
        Handle the payment_intent.succedeed webhook from stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
