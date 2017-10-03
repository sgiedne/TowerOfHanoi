from node import Node

ip = [[1],[],[]]
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
                move = [state[0],[state[2][0]] + state[1],state[2][1:]]
                moves.append(move)
    return moves

def print_trace(trace):
    for t in trace:
        print t

def find_best_move(moves,op):
    best_so_far = []
    for move in moves:

def bestfs(n,op):
    visited.append(n.state)
    moves = get_moves(n.state)
    best = find_best_move(moves,op)

    if not best:
        if n.parent == None:
            print "No solution exists"
            exit()
        else:
            bestfs(n.parent,op)

    #isited.append(best)
    if best == op:
        print_trace(visited)
        print best
        print "Solution found"
        exit()

    child = Node()
    child.state = best
    child.parent = n
    n.children.append(child)
    bestfs(child,op)
