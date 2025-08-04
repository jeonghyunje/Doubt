from django.http import JsonResponse
from .models import GameRoom
from .utils import generate_room_code

def create_room(request):
    code = generate_room_code()

    # 중복 방지
    while GameRoom.objects.filter(code=code).exists():
        code = generate_room_code()

    room = GameRoom.objects.create(code=code)
    return JsonResponse({'room_code': room.code})