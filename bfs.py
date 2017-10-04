from node import Node

ip = [[1,2,],[3,4],[]]
end = [[],[],[1,2,3,4]]
visited = [ip]
trace = []
found = False
bfsQ = [ip]
count = 0


def disp(moves):
    for move in moves:
        print move
def solveBfs(bfsQ):
    count = 0
    while bfsQ:
        count = count + 1
        currState = bfsQ[-1]
        del bfsQ[-1]
        moves = get_moves(currState, end, found, count)
        bfsQ = moves + bfsQ
def get_moves(state, end, found, count):
    moves = []
    print state
    if state == end:
        #disp(moves)
        print 'Yay!!'
        print count
        exit()
        #found = True
    if found:
        return moves
    if state[0]:
        if found:
            return moves
        if not state[1]:
            move = [state[0][1:],[state[0][0]],state[2]]
            
            if move not in visited:
                moves.append(move)
                visited.append(move)
                #if move == end:
                    #disp(moves)
                    #print 'Yay!!'
                    #exit()
                    #found = True

                #get_moves(move, end, found)
        else:
            if state[1][0] > state[0][0]:
                move = [state[0][1:],[state[0][0]] + state[1],state[2]]
                
                if move not in visited:
                    moves.append(move)
                    visited.append(move)
                    #if move == end:
                        #disp(moves)
                        #print 'Yay!!'
                        #exit()
                        #found = True
                    #get_moves(move, end, found)

        if not state[2]:
            move = [state[0][1:],state[1],[state[0][0]]]
            
            if move not in visited:
                moves.append(move)
                visited.append(move)
                #if move == end:
                    #disp(moves)
                    #print 'Yay!!'
                    #exit()
                    #found = True
                #get_moves(move, end, found)
        else:
            if state[2][0] > state[0][0]:
                move = [state[0][1:],state[1],[state[0][0]] + state[2]]
                
                if move not in visited:
                    moves.append(move)
                    visited.append(move)
                    #if move == end:
                        #disp(moves)
                        #print 'Yay!!'
                        #exit()
                        #found = True
                    #get_moves(move, end, found)
    if state[1]:
        if found:
            return moves
        if not state[0]:
            move = [[state[1][0]],state[1][1:],state[2]]
            
            if move not in visited:
                moves.append(move)
                visited.append(move)
                #if move == end:
                    #disp(moves)
                    #print 'Yay!!'
                    #exit()
                    #found = True
                #get_moves(move, end, found)
        else:
            if state[0][0] > state[1][0]:
                move = [[state[1][0]] + state[0],state[1][1:],state[2]]
                
                if move not in visited:
                    moves.append(move)
                    visited.append(move)
                    #if move == end:
                        #disp(moves)
                        #print 'Yay!!'
                        #exit()
                        #found = True
                    #get_moves(move, end, found)
        if not state[2]:
            move = [state[0],state[1][1:],[state[1][0]]]
            
            if move not in visited:
                moves.append(move)
                visited.append(move)
                #if move == end:
                    #disp(moves)
                    #print 'Yay!!'
                    #exit()
                    #found = True
                #get_moves(move, end, found)
        else:
            if state[2][0] > state[1][0]:
                move = [state[0],state[1][1:],[state[1][0]] + state[2]]
                
                if move not in visited:
                    moves.append(move)
                    visited.append(move)
                    #if move == end:
                        #disp(moves)
                        #print 'Yay!!'
                        #exit()
                        #found = True
                    #get_moves(move, end, found)
    if state[2]:
        if found:
            return moves
        if not state[0]:
            move = [[state[2][0]],state[1],state[2][1:]]
            
            if move not in visited:
                moves.append(move)
                visited.append(move)
                #if move == end:
                    #disp(moves)
                    #print 'Yay!!'
                    #exit()
                    #found = True
                #get_moves(move, end, found)
        else:
            if state[0][0] > state[2][0]:
                move = [[state[2][0]] + state[0],state[1],state[2][1:]]
                
                if move not in visited:
                    moves.append(move)
                    visited.append(move)
                    #if move == end:
                        #disp(moves)
                        #print 'Yay!!'
                        #exit()
                        #found = True
                    #get_moves(move, end, found)
        if not state[1]:
            move = [state[0],[state[2][0]],state[2][1:]]
            
            if move not in visited:
                moves.append(move)
                visited.append(move)
                #if move == end:
                    #disp(moves)
                    #print 'Yay!!'
                    #exit()
                    #found = True
                #get_moves(move, end, found)
        else:
            if state[1][0] > state[2][0]:
                move = [state[0],[state[2][0]] + state[1],state[2][1:]]
                
                if move not in visited:
                    moves.append(move)
                    visited.append(move)
                    #if move == end:
                        #disp(moves)
                        #print 'Yay!!'
                        #exit()
                        #found = True
                    #get_moves(move, end, found)
    return moves
#for i in get_moves(ip, end, found):
 #   print i
solveBfs(bfsQ)