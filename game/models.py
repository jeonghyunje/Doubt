from django.db import models

class GameRoom(models.Model):
    code = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_started = models.BooleanField(default=False)
    current_turn = models.IntegerField(default=0)

    def __str__(self):
        return f"GameRoom {self.code}"


class Player(models.Model):
    name = models.CharField(max_length=20)
    room = models.ForeignKey(GameRoom, on_delete=models.CASCADE, related_name='players')
    is_host = models.BooleanField(default=False)
    order = models.IntegerField()  # 몇 번째 순서인지

    def __str__(self):
        return f"{self.name} in Room {self.room.code}"


class Card(models.Model):
    SUITS = [('♠', 'Spades'), ('♥', 'Hearts'), ('♦', 'Diamonds'), ('♣', 'Clubs')]
    RANKS = [(str(n), str(n)) for n in range(2, 11)] + [('J', 'Jack'), ('Q', 'Queen'), ('K', 'King'), ('A', 'Ace')]

    suit = models.CharField(max_length=1, choices=SUITS)
    rank = models.CharField(max_length=2, choices=RANKS)
    owner = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    is_face_down = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.value}{self.suit}"