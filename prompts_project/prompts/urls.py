from django.urls import path
from .views import *

urlpatterns = [
        path('prompts', PromptListCreateView.as_view(), name='prompt-list'),
        path('prompts/<int:pk>', PromptDetailView.as_view(), name='prompt_detail'),
]
