from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('players/', views.players_index, name='index'),
    path('players/<int:player_id>/', views.players_detail, name='detail'),
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete'),
    path('players/<int:player_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('players/<int:player_id>/assoc_shoe/<int:shoe_id>/', views.assoc_shoe, name='assoc_shoe'),
    path('players/<int:player_id>/unassoc_shoe/<int:shoe_id>/', views.unassoc_shoe, name='unassoc_shoe'),
    path('shoes/', views.ShoeList.as_view(), name='shoes_index'),
    path('shoes/<int:pk>/', views.ShoeDetail.as_view(), name='shoes_detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoes_update'),
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoes_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]