"""An interactive tic tac toe game."""


class Player:
    """A two-player game"""

    def __init__(self, name, game_piece):
        self.name = name  # name of player
        self.game_piece = game_piece  # whether player is X or O on the board


class Move:
    """A move has one player and one board."""

    def __init__(self, author: str, position: list):
        self.author = author  # who made the move
        self.position = position  # where the move is placed on the board


class Board:
    """A board has up to 9 moves."""

    def __init__(self, moves):
        self.moves = moves  # all the moves currently on the board

    def display(board):
        """prints out the board for users to see it."""
        print("\n", board[0], board[1], board[2],
              "\n", board[3], board[4], board[5],
              "\n", board[6], board[7], board[8])

    def add_move(move_choice: int, ):
        """takes a move as an argument, adds it to moves attribute"""
        if move_choice not in range(9):
            print("Choose again")
        pass


class Game:
    """A game has one board.
    A game has two players.
    A game declares when the game is won, or a draw. Either way, gameplay ends.

    2 ways: [[], [], []] or [1, 2, 3, 4, 5, 6, 7, 8, 9]
    I like establishing this board: board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    We can use ints and strings to differentiate occupied spaces
    """

    def __init__(self, player1, player2):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # the playing board for the game
        self.player1 = player1  # first player in game
        self.player2 = player2  # second player in game
        # started_at: when the game started
        # finished_at: when the game ended

    def check_for_winner(self):
        """End the game if a winner is declared, or a draw when board is full)"""
        if (self.board[0] == self.board[1] == self.board[2]) or (self.board[0] == self.board[3] == self.board[6]) or (self.board[0] == self.board[4] == self.board[8]):
            return f"{self.board[0]} wins."
        elif (self.board[1] == self.board[4] == self.board[7]):
            return f"{self.board[1]} wins."
        elif (self.board[2] == self.board[5] == self.board[8]) or (self.board[2] == self.board[4] == self.board[6]):
            return f"{self.board[2]} wins."
        elif (self.board[3] == self.board[4] == self.board[5]):
            return f"{self.board[3]} wins."
        elif (self.board[6] == self.board[7] == self.board[8]):
            return f"{self.board[6]} wins."
        elif all(isinstance(x, str) for x in self.board):
            # No winner, but all strings means game is a draw
            return "It's a draw."
        else:
            return


    def next_player(self, current_player):
        Board.display(self.board)
        # Handle 2 invalid replies: strings and occupied ints.
        reply = self.validate_reply(input(f"{current_player.name}, please select a number:"), current_player)
        self.board[(reply-1)] = current_player.game_piece

    def validate_reply(self, reply, player):
        legal_moves_ints = []
        legal_moves_strings = []
        for index_ in range(9):
            if isinstance(self.board[index_], int):
                legal_moves_ints.append(self.board[index_])
                legal_moves_strings.append(str(self.board[index_]))
        while reply not in legal_moves_strings:
            reply = input(f"Try again, {player.name}. Please select an available number: {legal_moves_ints}")
        return int(reply)


def play_game():
    game_instance = Game(Player("Fred", "X"), Player("Joe", "O"))
    
    turns = 0
    while game_instance.check_for_winner() is None:
        turns += 1
        if turns % 2 == 0:
            current_player = game_instance.player1
        else:
            current_player = game_instance.player2
        game_instance.next_player(current_player)

    endgame_result = game_instance.check_for_winner()
    if game_instance.player1.game_piece in endgame_result:
        winner_name = game_instance.player1.name
    elif game_instance.player2.game_piece in endgame_result:
        winner_name = game_instance.player2.name
    else:
        winner_name = "no one"
    
    print(f"\n\n{endgame_result} Congratulations, {winner_name}!")
    Board.display(game_instance.board)

play_game()
