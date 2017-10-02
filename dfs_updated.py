from node import Node

ip = [[1,2],[3],[]]
end = [[],[],[1,2,3]]
visited = [ip]
trace = []
found = False
moves = [ip]

# root = Node()
# root.state = ip
def disp(moves):
    for move in moves:
        print move

def get_moves(state, end, found):
    if found:
        return moves
    if state[0]:
        if found:
            return moves
        if not state[1]:
            move = [state[0][1:],[state[0][0]],state[2]]
            moves.append(move)
            if move not in visited:
                visited.append(move)
                if move == end:
                    disp(moves)
                    print 'Yay!!'
                    exit()
                    found = True

                    get_moves(move, end, found)
        else:
            if state[1][0] > state[0][0]:
                move = [state[0][1:],[state[0][0]] + state[1],state[2]]
                moves.append(move)
                if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        print 'Yay!!'
                        exit()
                        found = True
                    get_moves(move, end, found)

        if not state[2]:
            move = [state[0][1:],state[1],[state[0][0]]]
            moves.append(move)
            if move not in visited:
                visited.append(move)
                if move == end:
                    disp(moves)
                    print 'Yay!!'
                    exit()
                    found = True
                get_moves(move, end, found)
        else:
            if state[2][0] > state[0][0]:
                move = [state[0][1:],state[1],[state[0][0]] + state[2]]
                moves.append(move)
                if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        print 'Yay!!'
                        exit()
                        found = True
                    get_moves(move, end, found)
    if state[1]:
        if found:
            return moves
        if not state[0]:
            move = [[state[1][0]],state[1][1:],state[2]]
            moves.append(move)
            if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        print 'Yay!!'
                        exit()
                        found = True
                    get_moves(move, end, found)
        else:
            if state[0][0] > state[1][0]:
                move = [[state[1][0]] + state[0],state[1][1:],state[2]]
                moves.append(move)
                if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        print 'Yay!!'
                        exit()
                        found = True
                    get_moves(move, end, found)
        if not state[2]:
            move = [state[0],state[1][1:],[state[1][0]]]
            moves.append(move)
            if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        print 'Yay!!'
                        exit()
                        found = True
                    get_moves(move, end, found)
        else:
            if state[2][0] > state[1][0]:
                move = [state[0],state[1][1:],[state[1][0]] + state[2]]
                moves.append(move)
                if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        print 'Yay!!'
                        exit()
                        found = True
                    get_moves(move, end, found)
    if state[2]:
        if found:
            return moves
        if not state[0]:
            move = [[state[2][0]],state[1],state[2][1:]]
            moves.append(move)
            if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        print 'Yay!!'
                        exit()
                        found = True
                    get_moves(move, end, found)
        else:
            if state[0][0] > state[2][0]:
                move = [[state[2][0]] + state[0],state[1],state[2][1:]]
                moves.append(move)
                if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        print 'Yay!!'
                        exit()
                        found = True
                    get_moves(move, end, found)
        if not state[1]:
            move = [state[0],[state[2][0]],state[2][1:]]
            moves.append(move)
            if move not in visited:
                visited.append(move)
                if move == end:
                    disp(moves)
                    print 'Yay!!'
                    exit()
                    found = True
                get_moves(move, end, found)
        else:
            if state[1][0] > state[2][0]:
                move = [state[0],[state[2][0]] + state[1],state[2][1:]]
                moves.append(move)
                if move not in visited:
                    visited.append(move)
                    if move == end:
                        disp(moves)
                        print 'Yay!!'
                        exit()
                        found = True
                    get_moves(move, end, found)
    return moves
for i in get_moves(ip, end, found):
    print i