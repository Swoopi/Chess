import random

pieceScore = {"K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "p": 1}
knightScores = [[1, 1, 1, 1, 1, 1, 1, 1],
                [1, 2, 2, 2, 2, 2, 2, 1],
                [1, 2, 3, 3, 3, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 3, 3, 3, 2, 1],
                [1, 2, 2, 2, 2, 2, 2, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]]
bishopScores = [[4, 3, 2, 1, 1, 2, 3, 4],
                [3, 4, 3, 2, 2, 3, 4, 3],
                [2, 3, 4, 3, 3, 4, 3, 2],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [2, 3, 4, 3, 3, 4, 3, 2],
                [3, 4, 3, 2, 2, 3, 4, 3],
                [4, 3, 2, 1, 1, 2, 3, 4]]
queenScores = [[1, 1, 1, 3, 1, 1, 1, 1],
                [1, 2, 3, 3, 3, 1, 1, 1],
                [1, 3, 3, 3, 3, 3, 2, 1],
                [1, 3, 3, 3, 3, 3, 3, 1],
                [1, 2, 3, 3, 3, 3, 2, 1],
                [1, 1, 3, 3, 3, 3, 1, 1],
                [1, 1, 1, 3, 3, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]]
rookScores = [[4, 3, 4, 4, 4, 4, 3, 4],
                [4, 4, 4, 4, 4, 4, 4, 4],
                [1, 1, 2, 3, 3, 2, 1, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 1, 2, 3, 3, 2, 1, 1],
                [4, 4, 4, 4, 4, 4, 4, 4],
                [4, 3, 4, 4, 4, 4, 3, 4]]
whitePawnScores = [[8, 8, 8, 8, 8, 8, 8, 8],
                    [5, 5, 5, 5, 5, 5, 5, 5],
                    [1, 1, 2, 3, 3, 2, 1, 1],
                    [1, 1, 2, 4, 4, 2, 1, 1],
                    [1, 1, 2, 5, 5, 2, 1, 1],
                    [1, 1, 2, 4, 4, 2, 1, 1],
                    [1, 1, 2, 3, 3, 2, 1, 1],
                    [8, 8, 8, 8, 8, 8, 8, 8]]
blackPawnScores = [[8, 8, 8, 8, 8, 8, 8, 8],
                    [1, 1, 2, 3, 3, 2, 1, 1],
                    [1, 1, 2, 4, 4, 2, 1, 1],
                    [1, 1, 2, 5, 5, 2, 1, 1],
                    [1, 1, 2, 4, 4, 2, 1, 1],
                    [1, 1, 2, 3, 3, 2, 1, 1],
                    [5, 5, 5, 5, 5, 5, 5, 5],
                    [8, 8, 8, 8, 8, 8, 8, 8]]

piecePositionScores = {"N": knightScores, "B": bishopScores, "Q": queenScores, "R": rookScores, "wP": whitePawnScores, "bP": blackPawnScores}
CHECKMATE = 1000
STALEMATE = 0
DEPTH = 2


def findRandomMove(validMoves):
    # Returns a random mome
    return validMoves[random.randint(0, len(validMoves)-1)]

def findBestMove(gs, validMoves, returnQueue):
    global nextMove, counter
    nextMove = None
    random.shuffle(validMoves)
    counter = 0
    #findMoveMinMax(gs, validMoves, DEPTH, gs.whiteToMove)
    findMoveNegaMaxAlphaBeta(gs, validMoves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.whiteToMove else -1)
    returnQueue.put(nextMove)

def findBestMoveMinMax(gs, validMoves):
    global nextMove
    nextMove = None
    random.shuffle(validMoves)
    #findMoveNegaMax(gs, validMoves, DEPTH, 1 if gs.whiteToMove else -1)
    return nextMove

def findMoveNegaMaxAlphaBeta(gs, validMoves, depth, alpha, beta, turnMultiplier):
    global nextMove, counter
    counter += 1
    if depth == 0:
        return turnMultiplier * scoreBoard(gs)
    
    #move ordering - implement later
    #orderMoves(validMoves)

    
    maxScore = -CHECKMATE
    for move in validMoves:
        gs.makeMove(move)
        nextMoves = gs.getValidMoves()
        score = -findMoveNegaMaxAlphaBeta(gs, nextMoves, depth-1, -beta, -alpha, -turnMultiplier)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move

        gs.undoMove()
        if maxScore > alpha: #prune
            alpha = maxScore
        if alpha >= beta:
            break

    return maxScore


def findMoveMinMax(gs, validMoves, depth, whiteToMove=True):
    global nextMove, counter
    counter += 1
    if depth == 0:
        return scoreMaterial(gs.board)
    if whiteToMove:
        maxScore = -CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveMinMax(gs, nextMoves, depth-1, False)
            if score > maxScore:
                maxScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return maxScore
    else:
        minScore = CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveMinMax(gs, nextMoves, depth-1, True)
            if score < minScore:
                minScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return minScore

def scoreBoard(gs):
    if gs.checkMate:
        if gs.whiteToMove:
            return -CHECKMATE
        else:
            return CHECKMATE
    elif gs.staleMate:
        return STALEMATE
    score = 0
    for row in range(len(gs.board)):
        for col in range(len(gs.board[row])):
            square = gs.board[row][col]
            if square != "--":
                piecePositionScore = 0
                if square[1] != "K":
                    if square[1] == "N":
                        piecePositionScore = knightScores[row][col]
                    elif square[1] == "B":
                        piecePositionScore = bishopScores[row][col]
                    elif square[1] == "Q":
                        piecePositionScore = queenScores[row][col]
                    elif square[1] == "R":
                        piecePositionScore = rookScores[row][col]
                    elif square[1] == "p":
                        piecePositionScore = whitePawnScores[row][col] if square[0] == "w" else blackPawnScores[row][col]

            if square[0] == "w":
                score += pieceScore[square[1]] + piecePositionScore * .1
            elif square[0] == "b":
                score -= pieceScore[square[1]] + piecePositionScore * .1
    return score

def scoreMaterial(board):
    score = 0
    for row in board:
        for square in row:
            if square[0] == "w":
                score += pieceScore[square[1]]
            elif square[0] == "b":
                score -= pieceScore[square[1]]
    return score

