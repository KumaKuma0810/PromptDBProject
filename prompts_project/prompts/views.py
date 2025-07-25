from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

class PromptListCreateView(APIView):
    def get(self, request):
        prompts = Prompts.objects.all()
        serializers = PromptSerializers(prompts, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post (self, request):
        serializers = PromptSerializers(data=request.data)

        if serializers.is_valid():
            serializers.save()
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PromptDetailView(APIView):
    def get(self, request, pk):
        prompt = get_object_or_404(Prompt, pk=pk)
        serializers = PromptSerializers(prompt)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self,request, pk):
        prompt = get_object_or_404(Prompt, pk=pk)
        serializers = PromptSerializers(prompt, data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Частичное обновление 
        """

        prompt = get_object_or_404(Prompt, pk=pk)
        serializers = PromptSerializers(prompt, data=request.data, partial=True)

        if serializers.is_valid():
            serializers.new()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        prompt = get_object_or_404(Prompt, pk)
        prompt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

