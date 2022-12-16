"""
Leo Gordon
12/4/22

>>> arr = np.array([[8,2,7,1,5,4,3,9,6],[9,6,5,3,2,7,1,4,8],[3,4,1,6,8,9,7,5,2],[5,9,3,4,6,8,2,7,1],[4,7,2,5,1,3,6,8,9],[6,1,8,9,7,2,4,3,5],[7,8,6,2,3,5,9,1,4],[1,5,4,7,9,6,8,2,3],[2,3,9,8,4,1,5,6,7]])

>>> s=sudokuboard(arr,1)


>>> assert s.incol(1,2)

>>> assert s.inrow(1,2)

>>> assert s.incell(1,1,1)
"""
import numpy as np
import copy
import random




class cell():
    def __init__(self,val):
        self.rep = val
        if self.rep == None:
            self.candidates = [i for i in range(1,9) if type(i)==int] #fill with candidates
        else:
            self.candidates = []
    def getcands(self):
        return self.candidates

class sudokuboard():
    def __init__(self,arr,diff) -> None:
        self.rep = np.array(arr,dtype=cell)
        for i in enumerate(arr):
            for j in enumerate(i[1]):
                k=int(j[1])
                self.rep[i[0],j[0]] = cell(k) #converting board to cells
        self.candidate_map()
        self.diff = diff
        
    def reduce(self):
        while self.diff != 0: #removing cells for difficulty
            arr2 = copy.deepcopy(self.rep) #we do this so that when the board is to difficult to be solvable we have a copy
            a = random.randint(0,8) #x-random
            b = random.randint(0,8) #y-random
            if str(self.rep[a,b].rep) in ("123456789"): #remove a single cell
                self.rep[a,b].rep = None
                self.rep[a,b].candidates = [i for i in range(1,9) if type(i)==int] #fill with candidates
                self.candidate_map() #generate candidate map
            s2=copy.deepcopy(s)
            self.candidate_map()
            for i in range(0,9):
                arr3 = []
                for j in range(0,9):
                    if (s2.rep[i,j].rep) != None:
                        arr3.append(s2.rep[i,j].rep)
                    else:
                        arr3.append(s2.rep[i,j].candidates)
                print(arr3)
            print("\n")
            if self.solver() == False:
                self.diff = 0
                self.rep = arr2
                self.candidate_map()
                return self.rep



    def incell(self,value:int,bigcellx,bigcelly): #Finds if the value is in a given cell, cells go left to right ([0,0],[1,0],[2,0],[0,1]), returns true, and if so, where location is given a cell in the bigcell
        bigcell=[self.rep[bigcellx*3+0,bigcelly*3+0],self.rep[bigcellx*3+1,bigcelly*3+0],self.rep[bigcellx*3+2,bigcelly*3+0],self.rep[bigcellx*3+0,bigcelly*3+1],self.rep[bigcellx*3+0,bigcelly*3+2],self.rep[bigcellx*3+1,bigcelly*3+1],self.rep[bigcellx*3+2,bigcelly*3+1],self.rep[bigcellx*3+1,bigcelly*3+2],self.rep[bigcellx*3+2,bigcelly*3+2]]
        for i in bigcell: #testing for i in the .rep of the cells in there
            if i.rep == value:
                return True
        return False

    def inrow(self,row:int,value:int): #return true if item is in the row
        for i in self.rep[row,:]:
            if i.rep == value:
                return True
        return False
    def incol(self,col:int,value:int): #return true if item is in the col, alongside where
        for i in self.rep[:,col]:
            if i.rep == value:
                return True
        return False
    def candidate_map(self): #if it doesn't have a value, give it candidates
        for i in range(0,8): #x pos
                for j in range(0,8): # y pos
                    if self.rep[i,j].rep == None: #if it's an empty cell
                        self.rep[i,j].candidates=[i for i in range(1,9) if type(i)==int] #write new candidates in this caused me much distress
                        for k in range(1,9): #itterate through values
                            if self.inrow(i,k): #if its in the row, then we remove it, but we can't just remove it, since thats not how this works
                                if k in self.rep[i,j].candidates:
                                    self.rep[i,j].candidates.remove(k)
                        for k in range(1,9): #itterate through values
                                if self.incol(j,k): #if its in the row, then we remove it, but we can't just remove it, since thats not how this works
                                    if k in self.rep[i,j].candidates: #
                                        self.rep[i,j].candidates.remove(k)
                        for k in range(1,9): #itterate through values
                                if self.incell(k,int(np.floor(i/3)),int(np.floor(j/3))): #if its in the cell, then we remove it, but we can't just remove it, since thats not how this works
                                    if k in self.rep[i,j].candidates:
                                        self.rep[i,j].candidates.remove(k)
    def solver(self): #solves a sudokuboard, if there are no possible further step to solve, then return false
        counter = 0
        for i in range(0,9): #this algorithm is a little dumb, and could be improved to make way better and cooler sudokus, but this is for another project down the line
            for j in range(0,9): #if the cell has only 1 candidate, then we can do something cool
                if self.rep[i,j].rep == None: #counting the number of empty cells remaining
                    counter = counter + 1 
                if counter == 30+(self.diff*5): # if there are 30 empty cells
                    return False

                        
                #find if there are any other empty cells there, and if it is the only one with 

arr = np.array([[8,2,7,1,5,4,3,9,6],[9,6,5,3,2,7,1,4,8],[3,4,1,6,8,9,7,5,2],[5,9,3,4,6,8,2,7,1],[4,7,2,5,1,3,6,8,9],[6,1,8,9,7,2,4,3,5],[7,8,6,2,3,5,9,1,4],[1,5,4,7,9,6,8,2,3],[2,3,9,8,4,1,5,6,7]])
print(arr)
s=sudokuboard(arr,1)
s.reduce()

        
if __name__ == "__main__":
    import doctest
    doctest.testmod()