class Player:
    def __init__(self, symbol) -> None:
        self.symbol = symbol

    def move(self, board) -> None:
        while True:
            move = input(f"Player {self.symbol}, enter your move: ")
            if move.isdigit() and 0 < int(move) < 10:
                move = int(move) - 1
                if board.board[move] == "-":
                    board.board[move] = self.symbol
                    break
                else:
                    print("That space is already taken.")
            else:
                print("Please enter a number between 1 and 9.")

    def get_symbol(self) -> int:
        return self.symbol