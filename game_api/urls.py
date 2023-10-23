from django.urls import path
from .views import RegisterView, LoginView, CreateGameView, GetBoardView, UpdateBoardView, ListGamesView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('create-game/', CreateGameView.as_view()),
    path('get-board/', GetBoardView.as_view(), name='get-board'),
    path('update-board/', UpdateBoardView.as_view()),
    path('list-games/', ListGamesView.as_view()),
]