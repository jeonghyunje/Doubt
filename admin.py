from django.contrib import admin
from .models import GameRoom, Player, Card

admin.site.register(GameRoom)
admin.site.register(Player)
admin.site.register(Card)