from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer): #give us json
    class Meta:
        # which model will get serialized by this call
        model=Todo
        # which fields should be included
        fields=['id', 'subject', 'details']