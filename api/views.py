from django.views import View
from django.http import HttpRequest,JsonResponse
from .models import Customer,Contact
from django.forms import model_to_dict
import json

class CustomersView(View):
    def get(self,request:HttpRequest) ->JsonResponse:
        results=[]
        for customer in Customer.objects.all():
            results.append(model_to_dict(customer, fields=["id","first_name", "last_name", "username"]))
        return JsonResponse(results, safe=False)
    
    def post(self,request: HttpRequest)->JsonResponse:
        body=request.body.decode()
        data=json.loads(body)
        Customer.objects.create(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            username=data.get("username"),
            password=data.get("password")
        )
        return {"message": "created objects"}


class CustomerDetailsView(View):
    pass

class ContactsView(View):
    pass


class ContactsDetailsView(View):
    pass
