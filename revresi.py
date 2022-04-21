import tkinter as tk
import tkinter.font as font
import numpy as np
import random as rd
import time
import copy

def place(Array,candidate,next):
    if check(Array,candidate,next)==False:
        return Array
    column = candidate//8
    row = candidate%8
    Array[column,row]=next
    for i in range(-1,2):
        for j in range(-1,2):
            if 0<=column+i and column+i<=7 and 0<=row+j and row+j<=7:
                if Array[column+i,row+j]==next*-1:
                    Array = continue_check(Array,column+i,row+j,i,j,next)             
    return Array

def continue_check(Array,column,row,i,j,next):
    column_temp=column
    row_temp=row
    while Array[column,row]==next*-1:
        column+=i
        row+=j
        if column < 0 or column > 7 or row  <0 or row > 7:
            return Array
    if Array[column,row]==0:
        return Array
    else:
        while Array[column_temp,row_temp]==next*-1:
            Array[column_temp,row_temp] = next
            column_temp+=i
            row_temp+=j
        return Array

        return Array
    
def check(Array,candidate,next):
    column = candidate//8
    row = candidate%8
    if column>7 or row>7 or column<0 or row<0:
        return False
    elif Array[column,row]!=0:
        return False
    else:
        for i in range(-1,2):
            for j in range(-1,2):
                if 0<=column+i and column+i<=7 and 0<=row+j and row+j<=7 and Array[column+i,row+j]==next*-1:
                    if c_check(Array,column+i,row+j,i,j,next)==True:
                        return True
        return False

def c_check(Array,column,row,i,j,next):
    while Array[column,row]==next*-1:
        column+=i
        row+=j
        if column<0 or column>7 or row<0 or row>7:
            return False
    if Array[column,row]==0:
        return False
    elif Array[column,row]==next:
        return True

def create_Array():
    Array=np.zeros((8,8))
    Array[27//8,27%8]=Array[36//8,36%8]=1
    Array[28//8,28%8]=Array[35//8,35%8]=-1
    return Array

def Pass_check(Array,next):
    for i in range(0,64):
        if check(Array,i,next)==True:
            return False
    #print("Pass")
    return True

def count(Array):
    black=white=0
    #self.txt.delete(0,tk.END)
    for i in range(0,8):
        for j in range(0,8):
            if Array[i,j]==1:
               black+=1
            elif Array[i,j]==-1:
                white+=1
    if black>white:
          #self.txt.insert(tk.END,'黒の勝ち')
          print("黒の勝ち")
          #self.win+=1
    elif white>black:
           #self.txt.insert(tk.END,'白の勝ち')
           print("白の勝ち")
    else:
        #self.txt.insert(tk.END,'引き分けもしくは判定不能')
        print("引き分けもしくは判定不能")
    print(black-white)
    return black-white

def cpu_turn3(Array,next):
    Max = [0,0]
    a = []
    value=[30,-12,0,-1,-1,0,-12,30,-12,-15,-3,-3,-3,-3,-15,-12,0,-3,0,-1,-1,0,-3,0,-1,-3,-1,-1,-1,-1,-3,-1,-1,-3,-1,-1,-1,-1,-3,-1,0,-3,0,-1,-1,0,-3,0,-12,-15,-3,-3,-3,-3,-15,-12,30,-12,0,-1,-1,0,-12,30]
    #Array_1 = copy.copy(Array)
    for i in range(0,64):
        count=0
        if check(Array,i,next)==True:
            temp_A = copy.copy(Array)
            temp_A = place(temp_A,i,next)
            for j in range(0,64):
                if check(temp_A,j,next*-1)==True:
                    count+=1
            if Max[0] <= count:
                Max[0] = count
                a.append(i)
    val=-100
    for k in range(len(a)):
        if value[a[k]] > val:
            val = value[a[k]]
            turn = a[k]
    if check(Array,turn,next)==True:
        Array = place(Array,turn,next)
    return Array

def cpu_random(Array,next):
    i = rd.randint(0,64)
    count=0
    while check(Array,i,next)==False:
        i = rd.randint(0,64)
        count+=1
        if count> 10000:
            return Array
    #print(i,"rand")
    Array = place(Array,i,next)
    return Array

def main():
    for i in range(0,100):
        Array = copy.copy(create_Array())
        Pass = 0
        next = 1
        while Pass<2:
            #print("先行")
            if Pass_check(Array,next)==True:
                Pass+=1
            else:
                Pass=0
                Array = copy.copy(cpu_turn3(Array,next))
                #print(Array)
            next*=-1
            #print("後攻")
            if Pass_check(Array,next)==True:
                Pass+=1
            else:
                Pass=0
                Array = copy.copy(cpu_random(Array,next))
                #print(Array)
            next*=-1
        #print(Array)
        count(Array)
    
    print("終わり")

if __name__ == "__main__":
    main()