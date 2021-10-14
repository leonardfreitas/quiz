from database import players

# adiciona um novo jogador do tipo dict na lista players
def create_player(name):
    if len(str(name)) >= 3:
        new_player = {"name": name, "score": 0}
        players.append(new_player)
        return "Jogador cadastrado com sucesso"
    else:
        return "Nome inválido"


# lista os jogadores da lista players
def list_players():
    return players
