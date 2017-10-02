from node import Node

ip = [[3,4],[1,5],[2,6,7]]
visited = []
trace = []

# root = Node()
# root.state = ip

def get_moves(state):
    moves = []
    if state[0]:
        if not state[1]:
            move = [state[0][1:],[state[0][0]],state[2]]
            moves.append(move)
        else:
            if state[1][0] > state[0][0]:
                move = [state[0][1:],[state[0][0]] + state[1],state[2]]
                moves.append(move)
        if not state[2]:
            move = [state[0][1:],state[1],[state[0][0]]]
            moves.append(move)
        else:
            if state[2][0] > state[0][0]:
                move = [state[0][1:],state[1],[state[0][0]] + state[2]]
                moves.append(move)
    if state[1]:
        if not state[0]:
            move = [[state[1][0]],state[1][1:],state[2]]
            moves.append(move)
        else:
            if state[0][0] > state[1][0]:
                move = [[state[1][0]] + state[0],state[1][1:],state[2]]
                moves.append(move)
        if not state[2]:
            move = [state[0],state[1][1:],[state[1][0]]]
            moves.append(move)
        else:
            if state[2][0] > state[1][0]:
                move = [state[0],state[1][1:],[state[1][0]] + state[2]]
                moves.append(move)
    if state[2]:
        if not state[0]:
            move = [[state[2][0]],state[1],state[2][1:]]
            moves.append(move)
        else:
            if state[0][0] > state[2][0]:
                move = [[state[2][0]] + state[0],state[1],state[2][1:]]
                moves.append(move)
        if not state[1]:
            move = [state[0],[state[2][0]],state[2][1:]]
            moves.append(move)
        else:
            if state[1][0] > state[2][0]:
                move = [state[0],[state[2][0]],state[2][1:]]
                moves.append(move)
    return moves

for i in get_moves(ip):
    print i
