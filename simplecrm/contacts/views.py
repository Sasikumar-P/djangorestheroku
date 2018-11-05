from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from contacts.models import Contact
from contacts.serializers import ContactSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class ContactListAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    #permission_classes = (IsAdminUser,)
