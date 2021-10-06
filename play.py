from commands import (
    COMMAND_EXIT, 
    COMMAND_CREATE_PLAYER, 
    COMMAND_LIST_PLAYERS
)
from settings import GAME_NAME
from services import create_player, list_players

run = True

while run:
    command = input(f"{GAME_NAME} >> ")

    if command == COMMAND_EXIT:
        run = False

    if command == COMMAND_CREATE_PLAYER:
        create_player()

    if command == COMMAND_LIST_PLAYERS:
        list_players()
