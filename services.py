from random import choice

from settings import get_message, OPTIONS_BY_QUESTION, SCORE_BY_QUESTION
from database import players, questions
from utils import divider

# adiciona um novo jogador do tipo dict na lista players
def create_player():
    divider()
    message = get_message("create_user")
    name = input(f"{message}: ")
    new_player = {"name": name, "score": 0}
    players.append(new_player)
    divider()


# lista os jogadores da lista players
def list_players():
    divider()
    for player in players:
        template = "{} - {}"
        print(template.format(player["name"], str(player["score"])))
    divider()


# adiciona uma nova questão do tipo dict na lista questions
def create_question():
    divider()
    message = get_message("create_question")
    question = input(f"{message}: ")
    new_question = {"question": question, "options": []} # cria o dict da question
    
    for i in range(0, OPTIONS_BY_QUESTION):
        number = i + 1
        new_option = create_option(number) # chama a função de criar uma opção para a questão
        new_question["options"].append(new_option)
    
    message_correct_option = get_message("correct_option")
    option_correct = int(input(f"{message_correct_option}: ")) # solicita a resposta correta

    # busca a opção opção selecionada a cima e atribui como correta
    for option in new_question["options"]:
        if option["number"] == option_correct:
            option["correct"] = True
            break # para parar a execução do for

    questions.append(new_question) # adiciona o dict na lista
    divider()


def create_option(number):
    message_option = get_message("create_option")
    option = input(f"{message_option} {number}: ")
    new_option = {"number": number, "option": option, "correct": False}
    return new_option


def list_questions():
    divider()
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            template_option = "{}. {}" # cria um template
            # insere no template os valores da opção para exibição
            message = template_option.format(option["number"], option["option"]) 
            
            # caso seja a opção correta insere a sinalização [X]
            if option["correct"]:
                message += " [X]"
    
            print(message)
    divider()


def play():
    divider()
    message = get_message("select_player")
    player_name = input(f"{message}: ")

    player = {}
    for p in players: # busca qual jogador foi selecionado
        if p["name"] == player_name:
            player = p # atualiza a variável player quando achar o jogar com nome digitado na variável player_name

    question = choice(questions)
    print(question["question"])
    for option in question["options"]:
        template_option = "{}. {}"
        message = template_option.format(option["number"], option["option"])
        print(message)

    option_selected_message = get_message("correct_option")
    option_player = int(input(f"{option_selected_message}: ")) # o jogar responde

    option_selected = {}
    # busca a opção do jogador
    for option in question["options"]:
        if option["number"] == option_player:
            option_selected = option
            break
    
    # testa se a opção do jogador está correta
    if option_selected["correct"]:
        player["score"] += SCORE_BY_QUESTION
    else: # caso não esteja exibimos a correta
        for option in question["options"]:
            if option["correct"]:
                message_correct_option = get_message("correct_option")
                option_correct = option["option"]
                print(f"{message_correct_option}: {option_correct}")
    
    divider()