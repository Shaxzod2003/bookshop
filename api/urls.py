from django.urls import path
from . import views


urlpatterns = [
    path('customers/', views.CustomersView.as_view()), # create, get all
    path('customers/<int:pk>/', views.CustomerDetailsView.as_view()), # get, update, delete
    path('customers/<int:pk>/contact/', views.ContactsView.as_view()), # get, update, delete, create
    path('publishers/', views.PublishersView.as_view()), # create, get all
    path('publishers/<int:pk>/', views.PublisherDetailView.as_view()), # get, update, delete
    path('languages/', views.LanguagesView.as_view()), # create, get all
    path('languages/<int:pk>/', views.LanguageDetailView.as_view()), # get, update, delete
    path('books/', views.BooksView.as_view()), # create, get all
    path('books/<int:pk>/', views.BookDetailView.as_view()), # get, update, delete
]