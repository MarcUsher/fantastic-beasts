from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('beasts/', views.beasts_index, name='index'), # Replaced with CBV ListView below

    # Beast paths
    path('beasts/', views.BeastList.as_view(), name="beast_index"),
    path('beasts/<int:beast_id>/', views.beasts_detail, name='beast_detail'),
    path('beasts/create/', views.BeastCreate.as_view(), name='beast_create'),
    path('beasts/<int:pk>/update/', views.BeastUpdate.as_view(), name='beast_update'),
    path('beasts/<int:pk>/delete/', views.BeastDelete.as_view(), name='beast_delete'),

    # Walk paths
    path('beasts/<int:beast_id>/add_walk', views.add_walk, name='add_walk'),

    # Location paths
    path('locations/', views.LocationList.as_view(), name='location_index'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='location_detail'),
    path('locations/create/', views.LocationCreate.as_view(), name='location_create'),
    path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='location_update'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='location_delete'),

    # Associate location with a beast (M:M)
    path('beasts/<int:beast_id>/assoc_location/<int:location_id>/', views.assoc_location, name='assoc_location'),

    # Disassociate location from beast (M:M)
    path('beasts/<int:beast_id>/disassoc_location/<int:location_id>/', views.disassoc_location, name='disassoc_location'),
]
