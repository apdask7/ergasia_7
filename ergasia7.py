#ΕΡΓΑΣΙΑ 7: ΤΡΙΛΙΖΑ

import random
while True:
        #SYMBOL SELECTION
        print("Select your sympol: X or O? ")
        symbol_pl=str(input())
        while symbol_pl!="O" and symbol_pl!="X" and symbol_pl!="o" and symbol_pl!="x":
                print("Wrong symbol! Try again")
                print("Select your symbol: X or O?")
                symbol_pl=str(input())
        

        if symbol_pl=="x" or symbol_pl=="X":
                symbol_cpu="O"
                symbol_pl="X"
        else:
                symbol_cpu="X"
                symbol_pl="O"

#WHO PLAYS FIRST
        order=random.randint(0, 1)
        if order==0:
                print("You play first!")
        else:
                print("CPU plays first!")



#CREATING GAME'S LIST        
        game=[[" "," "," "],[" "," "," "],[" "," "," "]]
#TICTACTOE DRAW
        if order==0:
                print(game[0][0] , "|", game[0][1],  "| " , game[0][2])
                print("------------")
                print(game[1][0] ,"|"  ,game[1][1]  ,"|",  game[1][2])
                print("------------")
                print(game[2][0] ,"|",  game[2][1] , "|" , game[2][2])
       
       
#GAME      
        m=0
        m=int(m)
        while True:
                if order==0:
                        while True:
                                sthlh=int(input("Give column number!: "))
                                while sthlh<1 or sthlh>3:
                                        print("Column's number must be from 1 to 3")
                                        sthlh=int(input("Give column number!: "))

                                grammh=int(input("Give row number!: "))
                                while grammh<1 or grammh>3:
                                        print("Row's number must be from 1 to 3")
                                        grammh=int(input("Give row number!: "))

                                if game[grammh-1][sthlh-1]==" ":
                                        game[grammh-1][sthlh-1]=symbol_pl
                                        m+=1
                                        order=1
                                        break
                                else:
                                        print("Error! Try again.")

                if order==1:
                        while True:
                                grammh=random.randint(0,2)
                                sthlh=random.randint(0,2)
                        
                                if game[grammh][sthlh]==" ":
                                        game[grammh][sthlh]=symbol_cpu
                                        m+=1
                                        order=0
                                        break
                
#TICTACTOE DRAW
        
                print(game[0][0] , "|", game[0][1],  "| " , game[0][2])
                print("------------")
                print(game[1][0] ,"|"  ,game[1][1]  ,"|",  game[1][2])
                print("------------")
                print(game[2][0] ,"|",  game[2][1] , "|" , game[2][2])
#CHECK IF PLAYER WON!
                key=False
                for i in range(3):
                        if ((game[i][0]==symbol_pl and game[i][1]==symbol_pl and game[i][2]==symbol_pl) or
                        (game[0][i]==symbol_pl and game[1][i]==symbol_pl and game[2][i]==symbol_pl)):
                                print("You won!")
                                key=True    
                    
                if ((game[0][0]==symbol_pl and game[1][1]==symbol_pl and game[2][2]==symbol_pl) or
                (game[0][2]==symbol_pl and game[1][1]==symbol_pl and game[2][0]==symbol_pl)):
                        print("You won!")
                        key=True

#CHECK IF CPU WON!

                for i in range(3):
                        if ((game[i][0]==symbol_cpu and game[i][1]==symbol_cpu and game[i][2]==symbol_cpu) or
                        (game[0][i]==symbol_cpu and game[1][i]==symbol_cpu and game[2][i]==symbol_cpu)):
                                print("You lost!")
                                key=True
       
                        
                if ((game[0][0]==symbol_cpu and game[1][1]==symbol_cpu and game[1][1]==symbol_cpu) or
                (game[0][2]==symbol_cpu and game[1][1]==symbol_cpu and game[2][0]==symbol_cpu)):
                        print("You lost!")
                        key=True
#CHECK FOR TIE
                if key==False and m==9:
                        print("Tie!")
                        break
                elif key==True:
                        break
                
#RESTART GAME
        answer=str(input("Press 'ENTER' to play again!"))
        if answer!="":
                break
                
        
      
