from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path("client/", views.ClientList.as_view()),
    path("client/<int:pk>/", views.ClientDetail.as_view()),
    path("project/", views.ProjectList.as_view()),
    path("project/<int:pk>/", views.ProjectDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)