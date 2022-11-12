class Board:
    def __init__(self) -> None:
        self.board = ["-"] * 9
        self.player = 1
        self.game_over = False
        self.winner = None

    def display(self) -> None:
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def is_game_over(self) -> bool:
        if self.board[0] == self.board[1] == self.board[2] != "-":
            self.winner = self.board[0]
            return True

        elif self.board[3] == self.board[4] == self.board[5] != "-":
            self.winner = self.board[3]
            return True

        elif self.board[6] == self.board[7] == self.board[8] != "-":
            self.winner = self.board[6]
            return True

        elif self.board[0] == self.board[3] == self.board[6] != "-":
            self.winner = self.board[0]
            return True

        elif self.board[1] == self.board[4] == self.board[7] != "-":
            self.winner = self.board[1]
            return True

        elif self.board[2] == self.board[5] == self.board[8] != "-":
            self.winner = self.board[2]
            return True

        elif self.board[0] == self.board[4] == self.board[8] != "-":
            self.winner = self.board[0]
            return True

        elif self.board[2] == self.board[4] == self.board[6] != "-":
            self.winner = self.board[2]
            return True

        elif "-" not in self.board:
            return True
