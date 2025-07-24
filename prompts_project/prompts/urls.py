from django.urls import path
from .views import *

urlpatterns = [
        path('prompts', PromptListCreateView.as_view(), name='prompt-list'),
        path('prompts/<int:pk>', PromptRetrieveUpdateDestroyView.as_view(), name='prompt_detail'),
]
