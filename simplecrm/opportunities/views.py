from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from opportunities.models import Opportunity
from opportunities.serializers import OpportunitySerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class OpportunityListAPIView(generics.ListCreateAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    #permission_classes = (IsAdminUser,)