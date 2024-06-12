from .models import Trip, ExpenseTracker
from rest_framework import serializers

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        
class TripRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
    
class ExpenseTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseTracker
        fields = '__all__'
        
class ExpenseTrackerRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseTracker
        fields = '__all__'