VALID_X = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}

BLACK = "black"
WHITE = "white"


def canMove(piece: str, pos_from: str, pos_to: str, colour: str = WHITE, output_board=True) -> bool:
    def validate_pos(pos):
        if len(pos) != 2:
            return False

        if pos[0].upper() not in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            return False

        if pos[1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            return False

        return True

    def chessCoordToTextCoord(pos) -> tuple:
        # Assume validation
        return VALID_X[pos[0].upper()], int(pos[1])

    if not(validate_pos(pos_from)) or not (validate_pos(pos_to)):
        print("Invalid positional input. Input must be A-H 1-8. e.g. G4")
        raise TypeError("Invalid positional input. Input must be A-H 1-8. e.g. G4")

    # Convert chess to tuple
    pos_from = chessCoordToTextCoord(pos_from)
    pos_to = chessCoordToTextCoord(pos_to)

    if piece.lower() == "rook":
        return canRookMove(pos_from, pos_to, colour=colour, output_board=output_board)
    elif piece.lower() == "bishop":
        return canBishopMove(pos_from, pos_to, colour=colour, output_board=output_board)
    elif piece.lower() == "knight":
        return canKnightMove(pos_from, pos_to, colour=colour, output_board=output_board)
    elif piece.lower() == "king":
        return canKingMove(pos_from, pos_to, colour=colour, output_board=output_board)
    elif piece.lower() == "queen":
        return canQueenMove(pos_from, pos_to, colour=colour, output_board=output_board)
    elif piece.lower() == "pawn":
        return canPawnMove(pos_from, pos_to, colour=colour, output_board=output_board)
    else:
        return None


def canRookMove(pos_from: tuple, pos_to: tuple, colour: str = WHITE, output_board=True) -> bool:
    if output_board:
        pops = {}
        # All valid positions
        for row in range(1, 9):
            pops[(pos_from[0], row)] = "O"

        for col in range(1, 9):
            pops[(col, pos_from[1])] = "O"

        # Current position
        pops[(pos_from[0], pos_from[1])] = "R"

        # Too pos
        if (pos_from[0] == pos_to[0] or pos_from[1] == pos_to[1]) and pos_from != pos_to:
            pops[(pos_to[0], pos_to[1])] = "W"
        else:
            pops[(pos_to[0], pos_to[1])] = "X"

        print_board(pops)

    return (pos_from[0] == pos_to[0] or pos_from[1] == pos_to[1]) and pos_from != pos_to


def canBishopMove(pos_from: tuple, pos_to: tuple, colour: str = WHITE, output_board=True) -> bool:
    if output_board:
        pops = {}
        # All valid positions
        for row in range(1, 9):
            for col in range(1, 9):
                if abs(row - pos_from[1]) == abs(col - pos_from[0]):
                    pops[(col, row)] = "O"

        # Current pos
        pops[(pos_from[0], pos_from[1])] = "B"

        # New location
        if abs(pos_from[0] - pos_to[0]) == abs(pos_from[1] - pos_to[1]) and pos_from != pos_to:
            pops[(pos_to[0], pos_to[1])] = "W"
        else:
            pops[(pos_to[0], pos_to[1])] = "X"
        print_board(pops)

    return abs(pos_from[0] - pos_to[0]) == abs(pos_from[1] - pos_to[1]) and pos_from != pos_to


def canKnightMove(pos_from: tuple, pos_to: tuple, colour: str = WHITE, output_board=True) -> bool:
    if output_board:
        pops = {}
        # Get all valid positions
        for row in range(1, 9):
            for col in range(1, 9):
                # it's dirty, but it works
                if canKnightMove(pos_from, (col, row), output_board=False):
                    pops[(col, row)] = "O"
        # Current location
        pops[(pos_from[0], pos_from[1])] = "k"

        # New pos
        # Still dirty
        if canKnightMove(pos_from, pos_to, output_board=False):
            pops[(pos_to[0], pos_to[1])] = "W"
        else:
            pops[(pos_to[0], pos_to[1])] = "X"

        print_board(pops)

    if abs(pos_to[1] - pos_from[1]) == 2:
        return abs(pos_from[0] - pos_to[0]) == 1 and pos_from != pos_to and pos_from != pos_to
    elif abs(pos_to[0] - pos_from[0]) == 2:
        return abs(pos_from[1] - pos_to[1]) == 1 and pos_from != pos_to and pos_from != pos_to

    return False


def canKingMove(pos_from: tuple, pos_to: tuple, colour: str = WHITE, output_board=True) -> bool:
    if output_board:
        pops = {}
        for row in range(1, 9):
            for col in range(1, 9):
                # it's dirty, but it works
                if canKingMove(pos_from, (col, row), output_board=False):
                    pops[(col, row)] = "O"

        pops[(pos_from[0], pos_from[1])] = "K"

        # Still dirty
        if canKingMove(pos_from, pos_to, output_board=False):
            pops[(pos_to[0], pos_to[1])] = "W"
        else:
            pops[(pos_to[0], pos_to[1])] = "X"

        print_board(pops)
    return -1 <= pos_from[0] - pos_to[0] <= 1 and -1 <= pos_from[1] - pos_to[1] <= 1 and pos_from != pos_to


def canQueenMove(pos_from: tuple, pos_to: tuple, colour: str = WHITE, output_board=True) -> bool:
    if output_board:
        pops = {}
        for row in range(1, 9):
            for col in range(1, 9):
                # it's dirty, but it works
                if canQueenMove(pos_from, (col, row), output_board=False):
                    pops[(col, row)] = "O"

        pops[(pos_from[0], pos_from[1])] = "Q"

        # Still dirty
        if canQueenMove(pos_from, pos_to, output_board=False):
            pops[(pos_to[0], pos_to[1])] = "W"
        else:
            pops[(pos_to[0], pos_to[1])] = "X"

        print_board(pops)
    return canBishopMove(pos_from, pos_to, output_board=False) or canRookMove(pos_from, pos_to, output_board=False)


def canPawnMove(pos_from: tuple, pos_to: tuple, colour: str = WHITE, output_board=True) -> bool:
    if output_board:
        pops = {}
        for row in range(1, 9):
            for col in range(1, 9):
                # it's dirty, but it works
                try:
                    if canPawnMove(pos_from, (col, row), colour=colour, output_board=False):
                        pops[(col, row)] = "O"
                except TypeError as err:
                    pass
        pops[(pos_from[0], pos_from[1])] = "P"

        # Still dirty
        if canPawnMove(pos_from, pos_to, colour=colour, output_board=False):
            pops[(pos_to[0], pos_to[1])] = "W"
        else:
            pops[(pos_to[0], pos_to[1])] = "X"

        print_board(pops)
    if colour == WHITE:
        if pos_from[1] == 1:
            raise TypeError("Invalid starting position.")
        elif pos_from[1] == 2:
            return 0 < pos_to[1] - pos_from[1] <= 2 and pos_from[0] == pos_to[0] and pos_from != pos_to
        else:
            return 0 < pos_from[1] - pos_to[1] <= 1 and pos_from[0] == pos_to[0] and pos_from != pos_to
    elif colour == BLACK:
        if pos_from[1] == 8:
            raise TypeError("Invalid starting position.")
        elif pos_from[1] == 7:
            return 0 < pos_from[1] - pos_to[1] <= 2 and pos_from[0] == pos_to[0] and pos_from != pos_to
        else:
            return 0 < pos_from[1] - pos_to[1] <= 1 and pos_from[0] == pos_to[0] and pos_from != pos_to
    else:
        raise TypeError(f"colour can only be {BLACK} or {WHITE}. '{colour}' was given.")


def print_board(pops={}):
    print("Key: K-King, Q-Queen, B-Bishop, k-knight, R-Rook, P-Pawn")
    print("\tPotential Move's: O, Your Invalid Move: X, Your Valid Move: W")
    print("|" + "---|"*7 + "---|")
    for i in range(8):
        row = 8 - i

        for col in range(1, 9):
            if (col, row) in pops:
                print("| " + pops[(col, row)] + " ", end="")
            else:
                print("|   ", end="")
        print("|")

        print("|" + "---|"*7 + "---|")


if __name__ == "__main__":
    print(canMove("pawn", "e2", "e4", colour=WHITE))
