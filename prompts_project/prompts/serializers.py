from rest_framework import serializers
from .models import *

class PromptSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fileds = "__all__"
        
