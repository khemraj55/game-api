from http.client import responses
from uuid import uuid4
from django.http import Http404, JsonResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import status
from .models import User, Game
from .serializers import UserSerializer, GameSerializer
from .utils import is_palindrome
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'User created successfully'})
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CreateGameView(APIView):
    def post(self, request):
        user = request.user
        game = Game.objects.create(user=user, game_id=str(uuid4()), string="")
        serializer = GameSerializer(game)
        return JsonResponse(serializer.data)

class GetBoardView(APIView):
    def post(self, request):
        game_id = request.data.get('game_id')

        try:
            game = Game.objects.get(game_id=game_id)
            serializer = GameSerializer(game)
            return JsonResponse(serializer.data)
        except Game.DoesNotExist:
            return JsonResponse({'error': 'Game not found'}, status=status.HTTP_404_NOT_FOUND)
    
class UpdateBoardView(APIView):
    def post(self, request):
        game_id = request.data.get('game_id')
        character = request.data.get('character')

        try:
            game = get_object_or_404(Game, id=game_id)
            game.string += character

            if len(game.string) == 6:
                game.is_palindrome = is_palindrome(game.string)

            game.save()

            serializer = GameSerializer(game)
            return JsonResponse(serializer.data)
        except Http404:
            return JsonResponse({'error': 'Game not found'}, status=status.HTTP_404_NOT_FOUND)

class ListGamesView(APIView):
    def get(self, request):
        user = request.user
        games = Game.objects.filter(user=user)
        serializers = GameSerializer(games, many=True)
        return JsonResponse(serializers.data, safe=False)