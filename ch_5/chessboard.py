chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', "9h" : "bqueen", '5h': 'bqueen', '3e': 'wking', }
# count = {}

def isValidChessBoard(dic):
    rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    columns = [1, 2, 3, 4, 5, 6, 7, 8]
    pieces = {"king" : 2, "queen" : 2, "bishop" : 4, "rook" : 4, "knight" : 4, 'pawn' : 16}
    counter = {}
    for k, v in dic.items():
    #Testing the keys
        (a, b) = list(k)
        if int(a) in columns:
            if b in rows:
                # return True
                print("Valid key!", a,b)
        else:
            print("invalid key", a, b)
            print("********************")
            print("Improper chess board")
            break

    #Testing the values
    for k, v in dic.items():
        if v[0] == "w" or v[0] == "b":
            #for p_k, p_v in pieces:
            if v[1:] in pieces:
                counter.setdefault(v[1:], 0)
                counter[v[1:]] += 1
    print(counter)
    for c_k, c_v in counter.items():
        if c_v <= pieces[c_k]:
            # return True
            print("valid number of values for:", c_k, c_v)
        else:
            print("Invalid number of values :", c_k, c_v)
            print("**************************************")
            print("improper chess board")
            break



isValidChessBoard(chessBoard)
