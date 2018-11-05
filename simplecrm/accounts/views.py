from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from accounts.models import Account
from accounts.serializers import AccountSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class AccountListAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    #permission_classes = (IsAdminUser,)