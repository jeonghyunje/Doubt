from django.db import models

class GameRoom(models.Model):
    code = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_started = models.BooleanField(default=False)
    current_turn = models.IntegerField(default=0)

    def __str__(self):
        return f"GameRoom {self.code}"


class Player(models.Model):
    name = models.CharField(max_length=100)
    room = models.ForeignKey(GameRoom, on_delete=models.CASCADE, related_name='players')
    is_host = models.BooleanField(default=False)
    order = models.IntegerField()  # 몇 번째 순서인지

    def __str__(self):
        return f"{self.name} in Room {self.room.code}"


class Card(models.Model):
    value = models.CharField(max_length=20)  # 예: 'A', '2', ..., 'K'
    suit = models.CharField(max_length=10)   # 예: 'hearts', 'spades'
    owner = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    room = models.ForeignKey(GameRoom, on_delete=models.CASCADE, related_name='cards')
    is_hidden = models.BooleanField(default=False)  # 현재 카드가 보이지 않는 상태인지

    def __str__(self):
        return f"{self.value} of {self.suit}"
