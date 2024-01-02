# Игра крестики нолики

# Автор:  Мещеряков Илья

# Инструкция к игре

EMPTY = " "
TIE = " Ничья "
NUM_SQUARES = 9

def display_instruct():
    print(
        """      Вам представлена класическая всеми извесная игра крестики нолики.
Ваши интелектуальные и стратегические навыки сойдутся в битве с процессором компьютера.
Чтобы сделать ход, введите число от 0 до 8. Числа соотвеьсьуют полям доски - так, как 
показанно ниже:
        0 | 1 | 2 
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
Приготовтесь к бою ведь компьютер не знает пощады! Удачи!
P.S Не пугайтесь если компьютер будет не уважительно к вам 
обращаться, он часто побеждает и поэтому зазнался, 
мы это исправим в следуйщем обновлении)))""")


def ask_yes_no(question):
    """ Заданет вопрос с ответом 'да' или 'нет'. """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """ Просит ввести число из диапозона. """
    response = None
    while response not in range(low, high):
        response = int(input(question))
        return response


def pieces():
    """ Определяет принадлежность первого хода."""
    go_first = ask_yes_no(" Хоешь оставить за собой первый ход, кожанный? (y/n): ")
    if go_first == "y":
        print(" Ну то ж, даю тебе фору: играй крестикамию. ")
        human = "X"
        computer = "O"
    else:
        print("Твоя нерешительность тебя погубит... Буду начинать я.")
    human = "O"
    computer = "X"
    return human, computer


def new_board():
    """ Создает новую игровую доску. """
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """ Отображает игровую доску на экране. """
    print(board[0], "|", board[1], "|", board[2])
    print("___" * 3)
    print(board[3], "|", board[4], "|", board[5])
    print("___" * 3)
    print(board[6], "|", board[7], "|", board[8])


def legal_moves(board):
    """ Создает список доступных ходов. """
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """ Определяет  победителя в игре. """
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    """ Получает ход человека """
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = input("Твой ход. Выбери одно из полей (0 - 8):")
        try:
            move = int(move)
        except ValueError:
            print(" Кожаный, это не не число. Попробуйте еще раз.")
            continue
        if move not in legal:
            print("Боже как ты глуп, это поле уже занято. Выбери другое.")
    print("Океееей...")
    return move


def computer_move(board, computer, human):
    """ Делает ход за компьютерного противника. """
    # создаем рабочую копию доски потому что функция будет менять некоторые значени в списке
    board = board[:]
    # создадим поля от лучшего хода к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print(" Я выбираю поле номер", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        # если в следуйщем ходу выйграет компьютер берем его
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        # если следующим ходом побеждает чел блокируем ход
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
        # а так же поскольку ни одна из сторон не может победить
        # выберем лучшее из ходов
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """ Осуществляет переход хода """
    if turn == "X":
        return "O"
    else:
        return "X"

    # функция используется для того, чтобы чередовать ходы игроков
def congrat_winner(the_winner, computer, human):
    """ Выявляет победителя """
    if the_winner != TIE:
        print("ТРИ", the_winner, "В РЯД!!!")
    else:
        print(" Ваши силы равны! Ничья! ")
    if the_winner == computer:
        print(" Как я  думал, победа осталась за мной." " ТЫ, ЧУШПАН! ")
    elif the_winner == human:
        print(
            " НЕТ-НЕТ-НЕТ, ЭТОГО НЕ МОЖЕТ БЫТЬ! У тебя получилось меня выйграть? Но как? \n"
            "Ладно, поздравляю тбя с победой но не стоит расслаблять булки, мы еще встретимся!")
    elif the_winner == TIE:
        print("Ха, ничья. Можешь радоваться и этому, кожаный")


def finish():
    display_instruct()
    computer, human = pieces()
    turn = "X"
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
finish()
input(" Нажмите Enter, чтобы выйти.")