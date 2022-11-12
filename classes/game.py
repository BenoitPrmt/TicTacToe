from classes.board import Board
from classes.player import Player

class TicTacToe:
    def __init__(self) -> None:
        self.board = Board()
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.current_player = self.player1

    def play(self) -> None:
        while True:
            self.board.display()
            self.current_player.move(self.board)
            if self.board.is_game_over():
                self.board.display()
                print("Game Over! " + ("Player " + self.current_player.get_symbol() +
                      " wins!" if self.board.winner else "It's a tie!"))
                break
            self.switch_players()

    def switch_players(self) -> None:
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

