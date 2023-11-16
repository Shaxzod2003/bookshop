from django.views import View
from django.http import HttpRequest,JsonResponse
from .models import Customer,Contact,Book, Publisher, Language, Author,Genre
from django.forms import model_to_dict
import json
from django.core.exceptions import ObjectDoesNotExist

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
        return JsonResponse({"message": "created objects"})




class CustomerDetailsView(View):
    def get(self,request: HttpRequest,pk :int)->JsonResponse:
        customer=Customer.objects.get(id=pk)
        result=model_to_dict(customer)
        return JsonResponse(result, safe=False)
    
    def put(self,request:HttpRequest, pk :int) ->JsonResponse:
        data=json.loads(request.body.decode())
        customer=Customer.objects.get(id=pk)
        Customer.objects.update(
            first_name=data.get("first_name", customer.first_name),
            last_name=data.get("last_name", customer.last_name),
            username=data.get("username", customer.username),
            password=data.get("password", customer.password)       
        )
        customer.save()
        return JsonResponse({"Error": "updated object"})


    def patch(self, request:HttpRequest, pk: int) ->JsonResponse:
        pass

    def delete(self, request:HttpRequest,  pk: int)-> JsonResponse:
        customer=Customer.objects.get(id=pk)
        customer.delete()


class ContactsView(View):
    def get(self, request:HttpRequest,pk: int) ->JsonResponse:
        try:
            customer=Customer.objects.get(id=pk)
        except ObjectDoesNotExist :
            return JsonResponse({"Error": "Customer does not exist"})
        
        try:
            contact=Contact.objects.get(customer=customer)
        except ObjectDoesNotExist:
            return JsonResponse({"Error", "contact does not exist"})
        
        result=model_to_dict(contact)
        return JsonResponse(result)
    
    def post(self,request:HttpRequest,pk:int)-> JsonResponse:
        try:
            customer=Customer.objects.get(id=pk)
        except ObjectDoesNotExist:
            return JsonResponse({"Error":"customer does not exist"})
        
        data=json.loads(request.body.decode())
        contact=Contact.objects.create(
            customer=customer,
            email=data.get("email"),
            address=data.get("address"),
            phone=data.get("phone")
        )
        result=model_to_dict(contact)
        return JsonResponse(result, status=201)
    
    def put(self, request:HttpRequest, pk :int)->JsonResponse:
        try:
            customer=Customer.objects.get(id=pk)
        except ObjectDoesNotExist:
            return JsonResponse({"Error":"customer does not exist"})
        
        try:
            contacts=Contact.objects.get(id=pk)
        except ObjectDoesNotExist:
            return JsonResponse({"Error": "contact does not exist"})
        data=json.loads(request.body.decode())
        Contact.objects.update(
            customer=customer,
            email=data.get("email", contacts.email),
            address=data.get("address", contacts.address),
            phone=data.get("phone", contacts.phone)
        )
        contacts.save()
        return JsonResponse({"message": "updated object"})

    def delete(self, request:HttpRequest,pk :int)-> JsonResponse:
        contact=Contact.objects.get(id=pk)
        contact.delete()
        return JsonResponse({"message": "deleted object"})


class PublishersView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        result=[]
        for publisher in Publisher.objects.all():
            result.append(model_to_dict(publisher))
        return JsonResponse(result, safe=False)

    def post(self, request: HttpRequest) -> JsonResponse:
        body=request.body.decode()
        data=json.loads(body)
        Publisher.objects.create(
            name=data.get("name"),
            descripton=data.get("description")
        )
        return JsonResponse({"message", "created objects"})

class PublisherDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            publisher=Publisher.objects.get(id=pk)
        except ObjectDoesNotExist:
            return JsonResponse({"Error":"doesnotexist"})
        result=model_to_dict(publisher)
        return JsonResponse(result)  
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        data=json.loads(request.body.decode())
        publisher=Publisher.objects.get(id=pk)
        Publisher.objects.update(
            name=data.get("name", publisher.name),
            description=data.get("description", publisher.description)
        )
        publisher.save()
        return JsonResponse({"message":"updated object"})
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        publisher=Publisher.objects.get(id=pk)
        publisher.delete()
        return JsonResponse({"message": "deleted object"})

class LanguagesView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        result=[]
        for language in Language.objects.all():
            result.append(model_to_dict(language))
        return JsonResponse(result, safe=False)
    
    def post(self, request: HttpRequest) -> JsonResponse:
        data=json.loads(request.body.decode())
        Language.objects.create(
            lang=data.get("lang")
        )
        return JsonResponse({"message":"created object"})

class LanguageDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        language=Language.objects.get(id=pk)
        result=model_to_dict(language)
        return JsonResponse(result)
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            language=Language.objects.get(id=pk)
        except ObjectDoesNotExist:
            return JsonResponse({"message":"language does not exist"})
        data=json.loads(request.body.decode())
        Language.objects.update(
            lang=data.get("lang",language.lang)
        )
        language.save()
        return JsonResponse({"message": "updated object"})
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        language=Language.objects.get(id=pk)
        language.delete()
        return JsonResponse({"message":"deleted object"})

class AuthorView(View):
    def get(self, request:HttpRequest)->JsonResponse:
        result=[]
        for author in Author.objects.all():
            result.append(model_to_dict(author))
        return JsonResponse(result, safe=False)
    
    def post(self,request:HttpRequest)->JsonResponse:
        data=json.loads(request.body.decode)
        Author.objects.create(
            first_name=data.get("first name"),
            last_name=data.get("last name"),
            bio=data.get("bio")
        )
        return JsonResponse({"message":"created object"})

class AuthorDetailView(View):
    def get(self,request:HttpRequest,pk:int)->JsonResponse:
        author=Author.objects.get(id=pk)
        result=model_to_dict(author)
        return JsonResponse(result)
    
    def put(self,request:HttpRequest,pk:int)->JsonResponse:
        data=json.loads(request.body.decode())
        author=Author.objects.get(id=pk)
        Author.objects.update(
            first_name=data.get("first name",author.first_name),
            last_name=data.get("last name", author.last_name),
            bio=data.get("bio", author.bio)
        )
        author.save()
        return JsonResponse({"message":"updated object"})
    
    def delete(self,request:HttpRequest,pk:int)->JsonResponse:
        author=Author.objects.get(id=pk)
        author.delete()
        return JsonResponse({"message":"deleted object"})
    

class GenreView(View):

    def get(self,request: HttpRequest)->JsonResponse:
        result=[]
        for genre in Genre.objects.all():
            result.append(model_to_dict(genre))
        return JsonResponse(result, safe=False)

    def post(self, request:HttpRequest)->JsonResponse:
        pass


class GenreDetailView(View):
    def get(self, request:HttpRequest,pk:int)->JsonResponse:
        pass

    def put(self,request:HttpRequest,pk:int)->JsonResponse:
        data=json.loads(request.body.decode())
        genre=Genre.objects.get(id=pk)
        Genre.objects.update(
            name=data.get("name",Genre.name),
        )
        Genre.save()
        return JsonResponse({"message":"updated object"})

    def delete(self,request:HttpRequest,pk:int)->JsonResponse:
        genre=Genre.objects.get(id=pk)
        genre.delete()
        return JsonResponse({"message":"deleted object"})

class BooksView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        params = request.GET

        if params.get('title', False):
            books = Book.objects.filter(title__icontains=params.get('title'))
        elif params.get('description', False):
            books = Book.objects.filter(description__icontains=params.get('description'))
        elif params.get('price', False):
            books = Book.objects.filter(price__lte=params.get('price'))
        elif params.get('lang', False):
            books = Book.objects.filter(lang__lang__icontains=params.get('lang'))
        elif params.get('publisher', False):
            books = Book.objects.filter(publisher__name__icontains=params.get('publisher'))
        else:
            books = Book.objects.all()

        result = [model_to_dict(book) for book in books]
        return JsonResponse(result, safe=False)
         
    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body.decode())

        title = data.get('title')
        description = data.get('description')
        price = data.get('price')
        lang = data.get('lang')
        publisher = data.get('publisher')

        if all([title, description, price, lang, publisher]):
            Book.objects.create(
                title=title,
                description=description,
                price=price,
                lang=lang,
                publisher=publisher
            )

            return JsonResponse({'message': 'object created.'}, status=201)
        else:
            return JsonResponse({'error': 'invalid data.'}, status=404)
    

class BookDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    