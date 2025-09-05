from django.contrib import admin   # <-- add this line
from django.http import JsonResponse
from django.urls import path
from core.views import ClientListCreateView, ClientDetailView, ProjectCreateView, UserProjectsView

from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Django Machine test"})


urlpatterns = [
    path('', home),  # Root URL
    path('admin/', admin.site.urls),  # Admin panel
    path('clients/', ClientListCreateView.as_view()),
    path('clients/<int:pk>/', ClientDetailView.as_view()),
    path('clients/<int:pk>/projects/', ProjectCreateView.as_view()),
    path('projects/', UserProjectsView.as_view()),
]
