from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# to store all of the coordinates of the game board
class Position(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["x", "y"],
                name="unique_board_position"
            )
        ]

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def get_absolute_url(self):
        #Returns the URL to access a particular instance of the model.
        return reverse('position-detail', args=[str(self.id)])
    
# to keep track of the two ends, the size of the game board, 
# the two players, who's turn it is, when the game was started, and if the game is over.
class Game(models.Model):
    board_size = models.IntegerField()

    end_1 = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        related_name="game_end_1"
    )

    end_2 = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        related_name="game_end_2"
    )

    player_1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="game_player_1"
    )

    player_2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="game_player_2"
    )

    current_turn = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="game_current_turn"
    )

    started_at = models.DateTimeField(auto_now_add=True)
    is_game_over = models.BooleanField(default=False)

    def __str__(self):
        return f"Game {self.id} ({self.player_1} vs {self.player_2})"
    
    def get_absolute_url(self):
        #Returns the URL to access a particular instance of the model.
        return reverse('game-detail', args=[str(self.id)])
    
# to store the player, the positions of the move from a to b, 
# the time it was made, and the game it belongs to.
class Move(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="moves"
    )

    player = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    time = models.DateTimeField(auto_now_add=True)

    a = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        related_name="move_start"
    )
    
    b = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        related_name="move_end"
    )

    class Meta:
        ordering = ["time"]

    def __str__(self):
        return f"{self.player} : {self.a} to {self.b}"
    
    def get_absolute_url(self):
        #Returns the URL to access a particular instance of the model.
        return reverse('move-detail', args=[str(self.id)])