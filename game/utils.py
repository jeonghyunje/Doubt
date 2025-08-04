import random
import string

def generate_room_code(length=8):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
