from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from leads.models import Lead
from leads.serializers import LeadSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class LeadListAPIView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    #permission_classes = (IsAdminUser,)