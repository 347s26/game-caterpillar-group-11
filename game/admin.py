from django.contrib import admin
from .models import Position, Game, Move

# Register your models here.
admin.site.register(Position)
admin.site.register(Game)
admin.site.register(Move)