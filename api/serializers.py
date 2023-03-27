from rest_framework import serializers
from api.models import Client,Project


#create serializers here

# Client serislizer
class ClientSerializer(serializers.ModelSerializer):
    client_id=serializers.ReadOnlyField()
    class Meta:
        model=Client
        fields="__all__"
        
        
# Project serislizer
class ProjectSerializer(serializers.ModelSerializer):
    project_id=serializers.ReadOnlyField()    
    class Meta:
        model=Project
        fields="__all__"