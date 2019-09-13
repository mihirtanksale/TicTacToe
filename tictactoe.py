import os
os.system("cls")

class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print (" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print ("-----------")
        print (" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print ("-----------")
        print (" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player
        #else :
         #   return 1

    def win(self, player):

        for combo in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False
            if result == True:
                return True
        return False

    def tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

    def reset(self):
         self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def ai_move(self, player):

        #if player == "X":
         #   enemy = "O"
        #if player == "O":
         #   enemy = "X"

    #if center is null then fill it first
        if self.cells[5] == " ":
            self.update_cell(5,player)
    #AI can win
        elif self.cells[1] == " ":
            self.update_cell(1,player)

        elif self.cells[3] == " ":
            self.update_cell(3,player)

        elif self.cells[7] == " ":
            self.update_cell(7,player)

        elif self.cells[9] == " ":
            self.update_cell(9,player)

    #AI blocks
    def ai_block(self,player):
        #win ai
        if self.cells[1]==self.cells[2]=="O" and self.cells[3]==" ":
            #if self.cells[3]==" ":
                self.update_cell(3,player)
        elif self.cells[2]==self.cells[3]=="O" and self.cells[1]==" ":
            #if self.cells[1]==" ":
                self.update_cell(1,player)
        elif self.cells[1]==self.cells[3]=="O" and self.cells[2]==" ":
            #if self.cells[2]==" ":
                self.update_cell(2,player)


        elif self.cells[4]==self.cells[5]=="O" and self.cells[6]==" ":
            #if self.cells[6]==" ":
                self.update_cell(6,player)
        elif self.cells[5]==self.cells[6]=="O" and self.cells[4]==" ":
            #if self.cells[4]==" ":
                self.update_cell(4,player)
        elif self.cells[4]==self.cells[6]=="O" and self.cells[5]==" ":
            #if self.cells[5]==" ":
                self.update_cell(5,player)

        elif self.cells[7]==self.cells[8]=="O" and self.cells[9]==" ":
            #if self.cells[9]==" ":
                self.update_cell(9,player)
        elif self.cells[8]==self.cells[9]=="O" and self.cells[7]==" ":
            #if self.cells[7]==" ":
                self.update_cell(7,player)
        elif self.cells[7]==self.cells[9]=="O" and self.cells[8]==" ":
            #if self.cells[8]==" ":
                self.update_cell(8,player)

        elif self.cells[1]==self.cells[4]=="O" and self.cells[7]==" ":
            #if self.cells[7]==" ":
                self.update_cell(7,player)
        elif self.cells[4]==self.cells[7]=="O" and self.cells[1]==" ":
            #if self.cells[1]==" ":
                self.update_cell(1,player)
        elif self.cells[1]==self.cells[7]=="O" and self.cells[4]==" ":
            #if self.cells[4]==" ":
                self.update_cell(4,player)

        elif self.cells[2]==self.cells[5]=="O" and self.cells[8]==" ":
            #if self.cells[8]==" ":
                self.update_cell(8,player)
        elif self.cells[5]==self.cells[8]=="O" and self.cells[2]==" ":
            #if self.cells[2]==" ":
                self.update_cell(2,player)
        elif self.cells[2]==self.cells[8]=="O" and self.cells[5]==" ":
            #if self.cells[5]==" ":
                self.update_cell(5,player)

        elif self.cells[3]==self.cells[6]=="O" and self.cells[9]==" ":
            #if self.cells[9]==" ":
                self.update_cell(9,player)
        elif self.cells[6]==self.cells[9]=="O" and self.cells[3]==" ":
            #if self.cells[3]==" ":
                self.update_cell(3,player)
        elif self.cells[3]==self.cells[9]=="O" and self.cells[6]==" ":
            #if self.cells[6]==" ":
                self.update_cell(6,player)

        elif self.cells[1]==self.cells[5]=="O" and self.cells[9]==" ":
            #if self.cells[9]==" ":
                self.update_cell(9,player)
        elif self.cells[5]==self.cells[9]=="O" and self.cells[1]==" ":
            #if self.cells[1]==" ":
                self.update_cell(1,player)
        elif self.cells[1]==self.cells[9]=="O" and self.cells[5]==" ":
            #if self.cells[5]==" ":
                self.update_cell(5,player)

        elif self.cells[3]==self.cells[5]=="O" and self.cells[7]==" ":
            #if self.cells[7]==" ":
                self.update_cell(7,player)
        elif self.cells[7]==self.cells[5]=="O" and self.cells[3]==" ":
            #if self.cells[3]==" ":
                self.update_cell(3,player)
        elif self.cells[3]==self.cells[7]=="O" and self.cells[5]==" ":
            #if self.cells[5]==" ":
                self.update_cell(5,player)

        #blocking
        elif self.cells[1]==self.cells[2]=="X" and self.cells[3]==" ":
            #if self.cells[3]==" ":
                self.update_cell(3,player)
        elif self.cells[2]==self.cells[3]=="X" and self.cells[1]==" ":
            #if self.cells[1]==" ":
                self.update_cell(1,player)
        elif self.cells[1]==self.cells[3]=="X" and self.cells[2]==" ":
            #if self.cells[2]==" ":
                self.update_cell(2,player)

        elif self.cells[4]==self.cells[5]=="X" and self.cells[6]==" ":
            #if self.cells[6]==" ":
                self.update_cell(6,player)
        elif self.cells[5]==self.cells[6]=="X" and self.cells[4]==" ":
            #if self.cells[4]==" ":
                self.update_cell(4,player)
        elif self.cells[4]==self.cells[6]=="X" and self.cells[5]==" ":
            #if self.cells[5]==" ":
                self.update_cell(5,player)

        elif self.cells[7]==self.cells[8]=="X" and self.cells[9]==" ":
            #if self.cells[9]==" ":
                self.update_cell(9,player)
        elif self.cells[8]==self.cells[9]=="X" and self.cells[7]==" ":
            #if self.cells[7]==" ":
                self.update_cell(7,player)
        elif self.cells[7]==self.cells[9]=="X" and self.cells[8]==" ":
            #if self.cells[8]==" ":
                self.update_cell(8,player)

        elif self.cells[1]==self.cells[4]=="X" and self.cells[7]==" ":
            #if self.cells[7]==" ":
                self.update_cell(7,player)
        elif self.cells[4]==self.cells[7]=="X" and self.cells[1]==" ":
            #if self.cells[1]==" ":
                self.update_cell(1,player)
        elif self.cells[1]==self.cells[7]=="X" and self.cells[4]==" ":
            #if self.cells[4]==" ":
                self.update_cell(4,player)

        elif self.cells[2]==self.cells[5]=="X" and self.cells[8]==" ":
            #if self.cells[8]==" ":
                self.update_cell(8,player)
        elif self.cells[5]==self.cells[8]=="X" and self.cells[2]==" ":
            #if self.cells[2]==" ":
                self.update_cell(2,player)
        elif self.cells[2]==self.cells[8]=="X" and self.cells[5]==" ":
            #if self.cells[5]==" ":
                self.update_cell(5,player)

        elif self.cells[3]==self.cells[6]=="X" and self.cells[9]==" ":
            #if self.cells[9]==" ":
                self.update_cell(9,player)
        elif self.cells[6]==self.cells[9]=="X" and self.cells[3]==" ":
            #if self.cells[3]==" ":
                self.update_cell(3,player)
        elif self.cells[3]==self.cells[9]=="X" and self.cells[6]==" ":
            #if self.cells[6]==" ":
                self.update_cell(6,player)

        elif self.cells[1]==self.cells[5]=="X" and self.cells[9]==" ":
            #if self.cells[9]==" ":
                self.update_cell(9,player)
        elif self.cells[5]==self.cells[9]=="X" and self.cells[1]==" ":
            #if self.cells[1]==" ":
                self.update_cell(1,player)
        elif self.cells[1]==self.cells[9]=="X" and self.cells[5]==" ":
            #if self.cells[5]==" ":
                self.update_cell(5,player)

        elif self.cells[3]==self.cells[5]=="X" and self.cells[7]==" ":
            #if self.cells[7]==" ":
                self.update_cell(7,player)
        elif self.cells[5]==self.cells[7]=="X" and self.cells[3]==" ":
            #if self.cells[3]==" ":
                self.update_cell(3,player)
        elif self.cells[3]==self.cells[7]=="X" and self.cells[5]==" ":
            #if self.cells[5]==" ":
                self.update_cell(5,player)
        else:
            if self.cells[5] == " ":
                self.update_cell(5,player)

            elif self.cells[1] == " ":
                self.update_cell(1,player)

            elif self.cells[3] == " ":
                self.update_cell(3,player)

            elif self.cells[7] == " ":
                self.update_cell(7,player)

            elif self.cells[9] == " ":
                self.update_cell(9,player)

        #timpass
        """
        elif self.cells[5] == " ":
            self.update_cell(5,player)

        elif self.cells[1] == " ":
            self.update_cell(1,player)

        elif self.cells[3] == " ":
            self.update_cell(3,player)

        elif self.cells[7] == " ":
            self.update_cell(7,player)

        elif self.cells[9] == " ":
            self.update_cell(9,player)

        """
board=Board()
#board.display()

def print_header():
    print ("Welcome to TIC TAC TOE")

def refresh_screen():
    os.system("cls")
    print_header()
    board.display()
#i=-1
#while True:
 #   i=i+1

for i in range(0,9):
    #choice = raw_input("\n You want X OR O").upper()
    refresh_screen()

    #Get X input
    x_choice = int(raw_input("\nX) Choose 1-9"))
    #Update board
    #check = board.update_cell(x_choice, "X")
    board.update_cell(x_choice, "X")

    #while check == 1 :
     #   print ("INVALID INPUT")
      #  i=i-1
       # x_choice = int(raw_input("\nX) Choose 1-9"))
        #Update board
        #check = board.update_cell(x_choice, "X")


    #RFRESH SCREEN
    refresh_screen()

    #check for x win
    if board.win("X"):
        print ("\n hurra X win !!!!!\n")
        play_again = raw_input("Would you like to play one more time? (Y/N)").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    #check for Tie game
    if board.tie():
        print ("\n Tie game !!!!!\n")
        play_again = raw_input("Would you like to play one more time? (Y/N)").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

     #Get O input
    #o_choice = int(raw_input("\nO) Choose 1-9"))5

    if i==0 :
        board.ai_move("O")
    else :
        #check = board.ai_block("O")
        board.ai_block("O")
        #if check == 1:
         #   print("problem")


    #REFRESH SCREEN
    refresh_screen()#When O wins it does not show last step


    #Update board
    #board.update_cell(o_choice, "O")

    #check for O win
    if board.win("O"):
        print ("\n Computer Wins !!!!!\n")
        play_again = raw_input("Would you like to play one more time? (Y/N)").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
         #check for Tie game
    if board.tie():
        print ("\n Tie game !!!!!\n")
        play_again = raw_input("Would you like to play one more time? (Y/N)").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
