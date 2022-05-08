from django.urls import path
from JOBS import views

app_name = 'jobs'

urlpatterns = [
    path('', views.JOBSView.as_view(), name='lista_jobs'),
    path('adaugare/', views.CreateJOBSView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateJOBSView.as_view(), name='modifica'),
    path('<int:pk>/stergere/', views.delete_JOBS, name='sterge'),
    path('<int:pk>/activeaza/', views.activate_JOBS, name='activeaza'),
]