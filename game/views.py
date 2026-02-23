from django.shortcuts import render

from .models import Game, Move, Position

def index(request):
    """View function for home page"""

    num_games = Game.objects.count()
    num_active_games = Game.objects.filter(is_game_over=False).count()
    num_finished_games = Game.objects.filter(is_game_over=True).count()

    context = {
        "num_games": num_games,
        "num_active_games": num_active_games,
        "num_finished_games": num_finished_games,
    }

    return render(request, "index.html", context)
