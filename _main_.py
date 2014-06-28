#todo: make sure that all ship points have to be adjacent!!

board = []
board_size = 5
missiles = 5
for x in range(0, board_size): #initialize board
	board.append(["O"] * board_size)

def print_board():
    for y in range(0, board_size):
	    print(board[y])
    
print_board()

ship_x = []
ship_y = []
print("hider:")
size = int(input("How big do you want your ship to be?"))
for x in range(0, size):
    while True:
    	a = int(input("X?"))
    	b = int(input("Y?"))
   		#if a > board_size or b > board_size:
        #	print("Sorry, at least one value is out of the range!")
    	if True:
    		ship_x.append(a - 1)
    		ship_y.append(b - 1)
    		board[a - 1][b - 1] = "#"
    		break
    	else:
        	print("sorry, it must be adjacent")
        	#break
    
print(ship_x)
print(ship_y)
print_board()
for x in range(0, board_size):
    board[x] = ["O"] * 5
    
for x in range(0, 10):
    print("wait...")
    
print("OK, shooter, your turn!")
points = len(ship_x)
hits = 0
hit_x = []
hit_y = []
while True:
    x = int(input("X?")) - 1
    y = int(input("Y?")) - 1
    #print(hit_x)
    #print(hit_y)
    if x > board_size or y > board_size:
        print("Sorry, a value is out of range!")
    elif missiles < 1:
        print("You ran out of shots!")
        print("you lose!")
        print("the answer was:")
        for x in range(0, board_size):
            board[x] = ["O"] * 5
        for x in ship_x:
            for y in ship_y:
                board[x][y] = "#"
                
        print_board()
        break
    else:
        missiles = missiles - 1
        if x not in ship_x or y not in ship_y:
            board[x][y] = "~"
            print("Sorry, you missed!")
        else:
            board[x][y] = "X"
            hits = hits + 1
            print("You hit part of the ship!")
            missiles = missiles + 2
        hit_x.append(x)
        hit_y.append(y)    
        if hits == points:
            print_board()
            print("You win!")
            break
               
    print_board()
