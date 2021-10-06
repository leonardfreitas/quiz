from commands import COMMAND_EXIT, COMMAND_CREATE_PLAYER
from settings import GAME_NAME, LANG, LANGS

run = True

players = []

while run:
    command = input(f"{GAME_NAME} >> ")

    if command == COMMAND_EXIT:
        run = False

    if command == COMMAND_CREATE_PLAYER:
        message = LANGS[LANG]["create_user"]
        name = input(f"{message}: ")
