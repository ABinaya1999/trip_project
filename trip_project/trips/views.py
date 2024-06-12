from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from  .models import Trip, ExpenseTracker
from .serializers import TripSerializer, TripRetrieveUpdateDestroySerializer, ExpenseTrackerSerializer, ExpenseTrackerRetrieveUpdateDestroySerializer

# Create your views here.
class TripAPIView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    
class TripRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripRetrieveUpdateDestroySerializer


class ExpenseTrackerAPIView(ListCreateAPIView):
    queryset = ExpenseTracker.objects.all()
    serializer_class = ExpenseTrackerSerializer
    
class ExpenseTrackerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ExpenseTracker.objects.all()
    serializer_class = ExpenseTrackerRetrieveUpdateDestroySerializer
    
    