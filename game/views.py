from django.shortcuts import render
from .models import Game
# Create your views here.

def game_view(request):
    games=Game.objects.all()
    return render(request,'game/game.html',{'games':games})