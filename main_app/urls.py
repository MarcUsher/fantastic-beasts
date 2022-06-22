from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('beasts/', views.beasts_index, name='index'), # Replaced with CBV ListView below
    path('beasts/', views.BeastList.as_view(), name="index"),
    path('beasts/<int:beast_id>/', views.beasts_detail, name='detail'),
    path('beasts/create/', views.BeastCreate.as_view(), name='beast_create'),
    path('beasts/<int:pk>/update/', views.BeastUpdate.as_view(), name='beast_update'),
    path('beasts/<int:pk>/delete/', views.BeastDelete.as_view(), name='beast_delete'),
]
