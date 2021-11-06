"""An interactive tic tac toe game."""
from termcolor import colored

class Player:
    """A two-player game"""

    def __init__(self, name: str, token: str, color: str):
        self.color = color  # color for the token, improves playability
        self.name = colored(name, self.color)  # name of player
        self.token = colored(token, self.color)  # whether player is X or O on the board


class Move:
    """A move has one player and one board."""

    def __init__(self, author: str, position: int):
        self.author = author  # who made the move
        self.position = position  # where the move is placed on the board


class Board:
    """A board has up to 9 moves.
    
    I have chosen this format for moves: {position: token}
    where unoccupied spaces values are the same as the dict key.
    Here's what one looks like midway through a game:
    {1: '\x1b[31mX\x1b[0m', 2: '\x1b[32mO\x1b[0m', 3: '\x1b[31mX\x1b[0m', 
    4: '\x1b[32mO\x1b[0m', 5: '\x1b[31mX\x1b[0m', 6: '\x1b[32mO\x1b[0m', 
    7: 7, 8: 8, 9: 9}
    So, if token is an int, it's a legal choice for gameplay. If not,
    reject it and help the player choose again.
    """

    moves = None  # all the moves currently on the board

    def __init__(self):
        self.moves = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

    def display(self):
        """prints out the board for users to see it."""
        print("\n", self.moves[1], self.moves[2], self.moves[3],
              "\n", self.moves[4], self.moves[5], self.moves[6],
              "\n", self.moves[7], self.moves[8], self.moves[9])

    def add_move(self, player):
        """takes a player object as an argument, adds it to moves attribute
        
        Also, we must handle 2 invalid replies: strings and occupied ints.
        """
        valid_reply_int = self.validate_reply(player)
        move_instance = Move(author=player, position=valid_reply_int)
        self.moves[move_instance.position] = player.token

    def validate_reply(self, player):
        legal_moves_ints = []
        legal_moves_strings = []
        for value in self.moves:
            try:
                int(self.moves[value])
                legal_moves_ints.append(self.moves[value])  # They're already ints
                legal_moves_strings.append(str(self.moves[value]))
            except ValueError:
                continue
        reply = input(f"{player.name}, please select a number:")
        while reply not in legal_moves_strings:  # Because input() always yields STRINGS
            reply = input(f"Try again, {player.name}. Please select an available position: {legal_moves_ints}")
        return int(reply)


class Game:
    """A game has one board.
    A game has two players.
    A game declares when the game is won, or a draw. Either way, gameplay ends.

    We can use ints and strings to differentiate occupied spaces.
    """

    def __init__(self, player1, player2):
        self.player1 = player1  # first player in game
        self.player2 = player2  # second player in game
        self.board_instance = Board()
        winner_token = self.gameplay_loop()
        self.print_endgame_messages(winner_token)
        # started_at: when the game started
        # finished_at: when the game ended

    def gameplay_loop(self):
        turns = 0
        while self.check_for_winner() is None:
            turns += 1
            if turns % 2 != 0:
                current_player = self.player1
            else:
                current_player = self.player2
            self.next_player(current_player)
        return self.check_for_winner()

    def check_for_winner(self):
        """End the game if a winner is declared, or a draw when board is full)
        
        There are 7 possible configurations for winning, plus a draw.
        """
        if (self.board_instance.moves[1] == self.board_instance.moves[2] == self.board_instance.moves[3]) or (
            self.board_instance.moves[1] == self.board_instance.moves[4] == self.board_instance.moves[7]) or (
                self.board_instance.moves[1] == self.board_instance.moves[5] == self.board_instance.moves[9]):
            return self.board_instance.moves[1]  # The winning token
        elif (self.board_instance.moves[2] == self.board_instance.moves[5] == self.board_instance.moves[8]):
            return self.board_instance.moves[2]  # The winning token
        elif (self.board_instance.moves[3] == self.board_instance.moves[6] == self.board_instance.moves[9]) or (
            self.board_instance.moves[3] == self.board_instance.moves[5] == self.board_instance.moves[7]):
            return self.board_instance.moves[3]  # The winning token
        elif (self.board_instance.moves[4] == self.board_instance.moves[5] == self.board_instance.moves[6]):
            return self.board_instance.moves[4]  # The winning token
        elif (self.board_instance.moves[7] == self.board_instance.moves[8] == self.board_instance.moves[9]):
            return self.board_instance.moves[7]  # The winning token
        elif all(isinstance(x, str) for x in self.board_instance.moves.values()):
            # No winner, but all strings means game is a draw
            return "D"  # It's a draw.
        else:
            return  # No winner yet. Gameplay continues.

    def next_player(self, current_player):
        self.board_instance.display()
        self.board_instance.add_move(current_player)

    def print_endgame_messages(self, winner_token):
        if winner_token == self.player1.token:
            game_result = f"\n\nThree {winner_token}s in a row!"
            congratulations = f"Congratulations, {self.player1.name}!"
        elif winner_token == self.player2.token:
            game_result = f"\n\nThree {winner_token}s in a row!"
            congratulations = f"Congratulations, {self.player2.name}!"
        else:
            game_result = f"\n\nIt's a draw!"
            congratulations = f"Nobody wins!"
        print(f"{game_result} {congratulations}")
        self.board_instance.display()

# Allowable colors are grey, red, green, yellow, blue, magenta, cyan, white
Game(Player("Ken", 'X', 'magenta'), Player("Jerry", 'O', 'cyan'))
