from django.urls import path
from . import views

app_name = 'maintenance'

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.CarList.as_view(), name='cars'),
    path('car/add', views.CarCreate.as_view(), name='car-create'),
    path('car/<int:pk>', views.CarDetail.as_view(), name='car-detail'),
    path('car/<int:pk>/update', views.CarUpdate.as_view(), name='car-update'),
    path('car/<int:pk>/delete', views.CarDelete.as_view(), name='car-delete'),
]
