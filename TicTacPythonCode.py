
import time
import copy

global AICalls

class TicTax:

  TicTacBoard = [["-","-","-"],["-","-","-"],["-","-","-"]]
  Move = 0
  GameOver = False
  BoardCounter = 0

  depthDict = {}

  UniqueID = 0


  def __init__(self,Board):
    self.TicTacBoard = Board
    self.Move = 0


  def TicTaxMove(self,y,x,Piece,TicB):
    #print("ins")
    if(TicB.TicTacBoard[x][y]=="-"):
      #print("ins2")
      TicB.TicTacBoard[x][y]=Piece
      
      return True
    return False


  def MiniMaxAI(self,TicB,Depth,Piece,BestXMove,BestOMove):


    # Handle the base case 
    # TODO: adjust 1 or -1 to correct mod relation

    GOver = TicB.GameOverTest(Piece)
    
    if(GOver[0] == True):
      # Evaluate a win with a 1 or a 0 
      #print("depth 1")
      if(Depth>-1):
        if(Depth%2==0):
          
          return [-1,[8,8]]

        if(Depth%2==1):
        
          return [1,[8,8]]

      
    # Not a win, handles draws 
    # Must occur after gameover mod test 
    # other wise it will send false positive on win 

    if(Depth==0):
       
      return [0,[8,8]]


    # find moves 

    Move = []
    for x in range(0,3,1):
      for y in range(0,3,1):
        if(TicB.TicTacBoard[x][y]=="-"):
          Move.append([y,x]) 


    TicCopies = [0]
    for x in range(len(Move)):
      
      TicBC = TicTax(copy.deepcopy(TicB.TicTacBoard))
      
      TicCopies.append(TicBC)
      
    if(Depth%2==0):
      TicCopies.append([-2,[0,0]])
    else:
      TicCopies.append([2,[0,0]])
    
    TicB.depthDict.update({Depth:TicCopies})
    

    if(Piece=="X"):
      
      #do all moves for "X"
      for x in Move:
             
        pointer = TicB.depthDict.get(Depth)[0]
        TicB.depthDict.get(Depth)[pointer+1].TicTaxMove(x[0],x[1],"X",TicB.depthDict.get(Depth)[pointer+1])
        ORetValue = self.MiniMaxAI(TicB.depthDict.get(Depth)[pointer+1],Depth-1,"O",BestXMove,BestOMove)

               
        if(ORetValue[0] > TicB.depthDict.get(Depth)[-1][0]):
          
          
          TicB.depthDict.get(Depth)[-1] = [ORetValue[0],x]
          

       
          

        TicB.depthDict.get(Depth)[0] += 1
      
        
          


      return TicB.depthDict.get(Depth)[-1]


    if(Piece=="O"):
      #print("inside O")
     
      for x in Move:


        pointer = TicB.depthDict.get(Depth)[0]

        TicB.depthDict.get(Depth)[pointer+1].TicTaxMove(x[0],x[1],"O",TicB.depthDict.get(Depth)[pointer+1])
        
        XRetValue = self.MiniMaxAI(TicB.depthDict.get(Depth)[pointer+1],Depth-1,"X",BestXMove,BestOMove)


        
        if(XRetValue[0] < TicB.depthDict.get(Depth)[-1][0]):
          
          TicB.depthDict.get(Depth)[-1] = [XRetValue[0],x]
        
        
         
         
        TicB.depthDict.get(Depth)[0] += 1

      return TicB.depthDict.get(Depth)[-1]



  def GameOverTest(self,Piece):
    
    GameOver = [False,"n"]
    # 3 for loops

    #checks horizontal rows

    #print("t 1")
    
    for x in range(0,3,1):
     

      if(self.TicTacBoard[x][0]=="-"):
        
        break

      for y in range(1,3,1):
        if(self.TicTacBoard[x][y]!=self.TicTacBoard[x][y-1]):
          BreakLoop = 1
          break
        #print("GO 1")
        if(y==2):
          GameOver = [True,Piece]

    #print(GameOver)
    #checks vertical rows
    #print("t 2")
    BreakLoop = 0
    for y in range(len(self.TicTacBoard)):      

      if(self.TicTacBoard[0][y]=="-"):
        BreakLoop = 1
        break
      for x in range(0,2,1):
        if(self.TicTacBoard[x][y]!=self.TicTacBoard[x+1][y]):
          BreakLoop = 1
          break
     #   print("go 2")
        if(x==1):
          GameOver = [True,Piece]

    #print(GameOver)
    #print("t 3")
    # Checks L\R diagonal

    BreakLoop = 0
    for x in range(1,3,1):
      if(self.TicTacBoard[x][x]=="-"):
        BreakLoop = 1
        break
      if(self.TicTacBoard[x][x]!=self.TicTacBoard[x-1][x-1]):
        BreakLoop = 1
        break

      #print("Go 3")
      if(x==2):
        GameOver = [True,Piece]
    

    #print(GameOver)
    #print("t 4")
    # Checks L/R diagonal

    RightCurser = 2
    BreakLoop = 0
    for y in range(1,3,1):
      if(self.TicTacBoard[RightCurser][y-1]=="-"):
        BreakLoop = 1
        break
      if(self.TicTacBoard[RightCurser][y-1]!=self.TicTacBoard[RightCurser-1][y]):
        BreakLoop = 1
        break
      RightCurser = RightCurser - 1  
      
      #print("Go4")
      if(x==2):
        GameOver = [True,Piece]
      
    return GameOver

 

def main():

  TicTacBoardY = [["-","-","-"],["-","-","-"],["-","-","-"]]

  
  AICalls = 0

  print("hellow owrld")
  TicTac = TicTax(copy.deepcopy(TicTacBoardY))
  GameOver = [False,"n"]
  TicTac.Move = 0
  print(TicTac.TicTacBoard)


  while(GameOver[0]==False and TicTac.Move<=8):

    

    if(TicTac.Move%2==0):
     
      x = int(input("enter Horizontal Row Number: "))
      y = int(input("enter Vertical Column Number: "))

      if(TicTac.TicTaxMove(y,x,"O",TicTac)):
        print("O's move")
        print(TicTac.TicTacBoard)
      else:
        continue
        

    if(TicTac.Move%2==1):

      

      # might need to adjust the 9 to an 8 
      Depth = 9 - TicTac.Move
     
      TicTac.depthDict = {}
      TicTac.BoardCounter = 0
      
      TicT = TicTax(copy.deepcopy(TicTac.TicTacBoard))
      
    
     
      AICalls = 0

      BestXMove = [-2,[0,0]]
      BestOMove = [2,[0,0]]
      
      AI = TicTac.MiniMaxAI(TicT,Depth,"X",BestXMove,BestOMove)
     
      print(TicTac.Move)
      if(TicTac.TicTaxMove(AI[1][0],AI[1][1],"X",TicTac)):
        print("X's Move")
        print(TicTac.TicTacBoard)
      else:
        continue
     
        
     


    GameOver = TicTac.GameOverTest("n")
    
    TicTac.Move = TicTac.Move + 1
    
    
    #print("time Sleep")
    #time.sleep(3)
  

  print("Game Over")


main()

