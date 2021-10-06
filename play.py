from commands import COMMAND_EXIT
from settings import GAME_NAME

run = True

while run:
    command = input(f"{GAME_NAME} >> ")

    if command == COMMAND_EXIT:
        run = False
