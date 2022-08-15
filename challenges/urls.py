from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='challenges_index'), # /challenges/
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name='path_name')
] 