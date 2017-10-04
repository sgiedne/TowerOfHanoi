from node import Node

'''
Worked by Siddharath Muthukumaran (SME0261) & Santhosh Subramanian (SSL4520)
This file performs Best First Search for a given input and end state
input - input state (list of list) and end state (list of list of list)
output - end state - visited_order (field_name) - represents the trace throught the tree

Fields:
visited - It presents the nodes that are visited and also the trace of the final output
'''

ip = [[1,2,3,4],[],[]]
op = [[],[4],[1,2,3]]
visited = []

'''
The method takes the current state and generate the possible moves for that state.
input - current state - [[1,2],[],[]]
output - possible moves - [[[2],[1],[]], [[2],[],[1]]]

Fields:
state - current state - list of list - [[],[],[]]
moves - ouput - list of list of list- [[[],[],[]], [[],[],[]]]

Approach:
a possible value is added to a moves based on two conditions
    1. if a pole is empty, then take the disc from the pole that has disc and directly place it in an empty pole.
    2. if a pole is not empty, check if the size of the disc is less than the size of the disc that is already present, before adding.
'''
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

'''
This method is used to print the list of all traces till the desired state is reached
'''
def print_trace(trace):
    for t in trace:
        print t

'''
This method is used to find the best possible move out of all the available moves for a node.

Fields:
moves - list of all available moves - [[[],[],[]], [[],[],[]]]
op - end state - [[],[],[]]

Approach:
For a given move, calculate the absolute difference between sums of value of the disks present in each pole respectively.
Then, proceed with a move that has minimum value

'''
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

'''
This method is used to calculate the best possible trace for a given input state and end state.
If solution exists, it will print "Solution found" and the trace for that solution
else it will print "No solution exists"

Fields:
n - input state or any state - list of list - [[],[],[]]
op - output state - [[],[],[]]

'''
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
