from django.urls import path
from . import views

urlpatterns=[
    path("customers/", views.CustomersView.as_view()),
    path("customer/<int:pk>/", views.CustomerDetailsView.as_view()),
    path("contacts/", views.ContactsView.as_view()),
    path("contact/<int:pk>/",views.ContactsDetailsView.as_view())
]