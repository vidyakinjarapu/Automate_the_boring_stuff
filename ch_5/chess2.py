chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3h': 'wking', '4h' : 'wqueen'}

def isValidChessBoard(dic):
    rows = [1, 2, 3, 4, 5, 6, 7, 8]
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    counter = {}
    pieces = {"king" : 2, "queen" : 2, "bishop" : 4, "rook" : 4, "knight" : 4, 'pawn' : 16}

    for k, v in dic.items():

    #Testing the keys
        (r, c) = list(k)
        if (int(r) not in rows) or (c not in columns):
            return False
            break
        #Testing Values
        if v[0] == "w" or v[0] == "b":
            if v[1:] in pieces:
                counter.setdefault(v[1:], 0)
                counter[v[1:]] += 1
        else:
            return False
            break
    # print(counter)
    for c_k, c_v in counter.items():
        if(c_v > pieces[c_k]):
            return False
            break
    return True

print(isValidChessBoard(chessBoard))
