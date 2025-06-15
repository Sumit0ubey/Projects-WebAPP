from django.urls import path

from .views import home, advanceSearch, project

urlpatterns = [
    path('', home, name='Home'),
    path('aq', advanceSearch, name='Advance'),
    path('<int:id>', project, name='Project'),
]
