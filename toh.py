from node import Node

ip = [[1,2,3,4],[],[]]
op = [[],[4],[1,2,3]]
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
    all_visited = True
    heuristic_dict = {}
    for move in moves:
        if move not in visited:
            all_visited = False
            peg_sum = abs(sum(move[0]) - sum(op[0])) + abs(sum(move[1]) - sum(op[1])) + abs(sum(move[2]) - sum(op[2]))
            heuristic_dict[peg_sum] = move

    if all_visited:
        return None

    min_sum = min(heuristic_dict.keys())
    best_move = heuristic_dict[min_sum]
    return best_move

# print find_best_move([[[2],[1,3],[4,5]],[[2],[3],[1,4,5]],[[1,2],[],[3,4,5]]],[[],[],[1,2,3,4,5]])

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

root = Node()
root.state = ip
bestfs(root,op)
