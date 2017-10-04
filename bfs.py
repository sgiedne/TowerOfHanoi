'''
Worked by Siddharath Muthukumaran (SME0261) & Santhosh Subramanian (SSL4520)

This file performs Breadth First Search for a given input and end state
input - input state (list of list) and end state (list of list of list)
output - trace of the tree

Fields:
visited - It represents the nodes that are visited.
bfsQ - Stores all the children in a queue


'''

#ip = [[1,2,],[3,4],[]]
#end = [[],[],[1,2,3,4]]
visited = []
bfsQ = []
count = 0

'''
This method is used to display all the moves once the solution is found

Field:
moves - list of list of list [[[],[],[]], [[],[],[]], [[],[],[]]] - trace of the final output
'''
def disp(moves):
    for move in moves:
        print move

'''
This is the implements the bfs using queue technique.

Fields:
bdfQ - input state - [[],[],[]]
end - output state - [[],[],[]]

Approach:
    1. Add the input node to the queue
    2. Before poping a node from the queue, get all the moves/childrens and add it to the queue.
    3. Check if end state is obtained once a move is populated for a node. Also, mark each node as visited once a move is generated
'''
def solveBfs(bfsQ, end):
    count = 0    
    while bfsQ:
        count = count + 1
        currState = bfsQ[-1]
        del bfsQ[-1]
        moves = get_moves(currState, end, count)
        bfsQ = moves + bfsQ

'''
This method gets the current state and determines the first move using that current state.
Using that move, generate the next possible move for that. 
The process goes on until the end state is achieved and the each time a move is generated it will be marked visited.

state - current state or the node - [[],[],[]]
end - end state - [[],[],[]]
count - number steps to obtain the result
'''
def get_moves(state, end, count):
    moves = []
    print state
    if state == end:
        print 'BFS - Solution found'
        print 'No of steps taken to solve BFS: ',
        print count
        exit()    
    if state[0]:
        if not state[1]:
            move = [state[0][1:],[state[0][0]],state[2]]
            
            if move not in visited:
                moves.append(move)
                visited.append(move)
        else:
            if state[1][0] > state[0][0]:
                move = [state[0][1:],[state[0][0]] + state[1],state[2]]
                
                if move not in visited:
                    moves.append(move)
                    visited.append(move)

        if not state[2]:
            move = [state[0][1:],state[1],[state[0][0]]]
            
            if move not in visited:
                moves.append(move)
                visited.append(move)
        else:
            if state[2][0] > state[0][0]:
                move = [state[0][1:],state[1],[state[0][0]] + state[2]]
                
                if move not in visited:
                    moves.append(move)
                    visited.append(move)
    if state[1]:
        if not state[0]:
            move = [[state[1][0]],state[1][1:],state[2]]
            
            if move not in visited:
                moves.append(move)
                visited.append(move)
        else:
            if state[0][0] > state[1][0]:
                move = [[state[1][0]] + state[0],state[1][1:],state[2]]
                
                if move not in visited:
                    moves.append(move)
                    visited.append(move)
        if not state[2]:
            move = [state[0],state[1][1:],[state[1][0]]]
            
            if move not in visited:
                moves.append(move)
                visited.append(move)
        else:
            if state[2][0] > state[1][0]:
                move = [state[0],state[1][1:],[state[1][0]] + state[2]]
                
                if move not in visited:
                    moves.append(move)
                    visited.append(move)
    if state[2]:
        if not state[0]:
            move = [[state[2][0]],state[1],state[2][1:]]            
            if move not in visited:
                moves.append(move)
                visited.append(move)
        else:
            if state[0][0] > state[2][0]:
                move = [[state[2][0]] + state[0],state[1],state[2][1:]]                
                if move not in visited:
                    moves.append(move)
                    visited.append(move)
        if not state[1]:
            move = [state[0],[state[2][0]],state[2][1:]]            
            if move not in visited:
                moves.append(move)
                visited.append(move)
        else:
            if state[1][0] > state[2][0]:
                move = [state[0],[state[2][0]] + state[1],state[2][1:]]                
                if move not in visited:
                    moves.append(move)
                    visited.append(move)
    return moves


'''
This is the base method to call the bfs implementation

Fields:
ip - input state - [[],[],[]]
end - output state - [[],[],[]]
'''
def call_bfs(ip, end):
    visited.append(ip)
    bfsQ.append(ip)
    solveBfs(bfsQ, end)