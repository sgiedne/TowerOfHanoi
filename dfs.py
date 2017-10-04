'''
Worked by Siddharth Muthukumaran (SME0261) & Santhosh Subramanian (SSL4520)

This file performs Depth First Search for a given input and end state
input - input state (list of list) and end state (list of list of list)
output - trace of the tree

Fields:
visited - It represents the nodes that are visited.
moves - It represents the trace of the final output
'''

ip = [[1,2,3,4],[],[]]
end = [[],[4],[1,2,3]]
visited = []
moves = []

'''
This method is used to display all the moves once the solution is found

Field:
moves - list of list of list [[[],[],[]], [[],[],[]], [[],[],[]]] - trace of the final output
'''
def disp(moves):
    count = 0
    for move in moves:
        count += 1
        print move
    print 'DFS - Solution found'
    print 'No of steps taken to solved DFS: ',
    print count
'''
This method gets the current state and determines the first move using that current state.
Using that move, generate the next possible move for that.
The process goes on until the end state is achieved and the each time a move is generated it will be marked visited.

state - current state or the node - [[],[],[]]
end - end state - [[],[],[]]
'''
def get_moves(state, end):
    if state[0]:
        if not state[1]:
            move = [state[0][1:],[state[0][0]],state[2]]
            moves.append(move)
            if move not in visited:
                visited.append(move)
                if move == end:
                    disp(moves)
                    exit()
                get_moves(move, end)
        else:
            if state[1][0] > state[0][0]:
                move = [state[0][1:],[state[0][0]] + state[1],state[2]]
                moves.append(move)
                if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        exit()
                    get_moves(move, end)

        if not state[2]:
            move = [state[0][1:],state[1],[state[0][0]]]
            moves.append(move)
            if move not in visited:
                visited.append(move)
                if move == end:
                    disp(moves)
                    exit()
                get_moves(move, end)
        else:
            if state[2][0] > state[0][0]:
                move = [state[0][1:],state[1],[state[0][0]] + state[2]]
                moves.append(move)
                if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        exit()
                    get_moves(move, end)
    if state[1]:
        if not state[0]:
            move = [[state[1][0]],state[1][1:],state[2]]
            moves.append(move)
            if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        exit()
                    get_moves(move, end)
        else:
            if state[0][0] > state[1][0]:
                move = [[state[1][0]] + state[0],state[1][1:],state[2]]
                moves.append(move)
                if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        exit()
                    get_moves(move, end)
        if not state[2]:
            move = [state[0],state[1][1:],[state[1][0]]]
            moves.append(move)
            if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        exit()
                    get_moves(move, end)
        else:
            if state[2][0] > state[1][0]:
                move = [state[0],state[1][1:],[state[1][0]] + state[2]]
                moves.append(move)
                if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        exit()
                    get_moves(move, end)
    if state[2]:
        if not state[0]:
            move = [[state[2][0]],state[1],state[2][1:]]
            moves.append(move)
            if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        exit()
                    get_moves(move, end)
        else:
            if state[0][0] > state[2][0]:
                move = [[state[2][0]] + state[0],state[1],state[2][1:]]
                moves.append(move)
                if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        exit()
                    get_moves(move, end)
        if not state[1]:
            move = [state[0],[state[2][0]],state[2][1:]]
            moves.append(move)
            if move not in visited:
                visited.append(move)
                if move == end:
                    disp(moves)
                    exit()
                get_moves(move, end)
        else:
            if state[1][0] > state[2][0]:
                move = [state[0],[state[2][0]] + state[1],state[2][1:]]
                moves.append(move)
                if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        exit()
                    get_moves(move, end)
    return moves

'''
This is the base method to call the dfs implementation

Fields:
ip - input state - [[],[],[]]
end - output state - [[],[],[]]
'''
def call_dfs(ip, end):
    visited.append(ip)
    moves.append(ip)
    get_moves(ip, end)

call_dfs(ip, end)
