from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='pizza-home'),
    path('create/', views.createPizza,name='pizza-create'),
    path("delete/<str:delete_id>/", views.deletePizza,name='pizza-delete'),
    path('update/<str:update_id>/', views.updatePizza,name='pizza-update'),
    path('detail/<str:view_id>/', views.viewPizza,name='pizza-view'),
]

