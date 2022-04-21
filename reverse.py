import tkinter as tk
import tkinter.font as font
import numpy as np
import random as rd
import time
import copy

class App(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        Array=self.create_Array()
        Pass=0
        next=1
        master.title("オセロ")
        master.geometry("1000x1000")
        self.txt = tk.Entry(width=50)
        
        #if self.check(B,63,-1)==True:
            #print("True")
        #else:
            #print("False")
        
        while Pass<2:
            print("先行")
            if self.Pass_check(Array,next)==True:
                Pass+=1
            else:
                Pass=0
                
                Array = self.cpu_turn2(Array,next)
            print(Array)
            next*=-1
            print("後攻")
            if self.Pass_check(Array,next)==True:
                Pass+=1
            else:
                Pass=0
                Array = self.cpu_turn1(Array,next)
            
            print(Array)
            next*=-1
        
        self.count(Array)
        print("終わり")
        
            
    def cpu_turn(self,Array,next):
        i=0
        for i in range(0,64):
            if self.check(Array,i,next)==True:
                Array = self.place(Array,i,next)
                return Array
        return Array
        
    '''
    def print_squares(self,Array):
        num = 0
        for i in range(0,8):
            for j in range(0,8):
                if Array[i,j]==1:
                    label=tk.Label(self,text='●',bg='green',fg='black', bd=2,font=font.Font(size=30, weight='bold'), relief='groove', width=2, height=1)
                    label.grid(row=i,column=j+3)
                if Array[i,j]==-1:
                    label=tk.Label(self,text='●',bg='green',fg='white', bd=2,font=font.Font(size=30, weight='bold'), relief='groove', width=2, height=1)
                    label.grid(row=i,column=j+3)
                else:
                    label=tk.Label(self,text=num,bg='green',fg='green', bd=2,font=font.Font(size=30, weight='bold'), relief='groove', width=2, height=1)
                    label.grid(row=i,column=j+3)
                num+=1
    '''
    def place(self,Array,candidate,next):
        if self.check(Array,candidate,next)==False:
            return Array
        column = candidate//8
        row = candidate%8
        Array[column,row]=next
        for i in range(-1,2):
            for j in range(-1,2):
                if 0<=column+i and column+i<=7 and 0<=row+j and row+j<=7:
                        if Array[column+i,row+j]==next*-1:
                            Array = self.continue_check(Array,column+i,row+j,i,j,next)             
        return Array
    
    def continue_check(self,Array,column,row,i,j,next):
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

    def check(self,Array,candidate,next):
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
                        if self.c_check(Array,column+i,row+j,i,j,next)==True:
                            return True
            return False

    def c_check(self,Array,column,row,i,j,next):
        while Array[column,row]==next*-1:
            column+=i
            row+=j
            if column<0 or column>7 or row<0 or row>7:
                return False
        if Array[column,row]==0:
            return False
        elif Array[column,row]==next:
            return True

    def create_Array(self):
        Array=np.zeros((8,8))
        Array[27//8,27%8]=Array[36//8,36%8]=1
        Array[28//8,28%8]=Array[35//8,35%8]=-1
        return Array

    def Pass_check(self,Array,next):
        for i in range(0,64):
            if self.check(Array,i,next)==True:
                return False
        print("Pass")
        return True

    def count(self,Array):
        black=white=0
        self.txt.delete(0,tk.END)
        for i in range(0,8):
            for j in range(0,8):
                if Array[i,j]==1:
                   black+=1
                elif Array[i,j]==-1:
                    white+=1
        if black>white:
              self.txt.insert(tk.END,'黒の勝ち')
              print("黒の勝ち")
        elif white>black:
               self.txt.insert(tk.END,'白の勝ち')
               print("白の勝ち")
        else:
            self.txt.insert(tk.END,'引き分けもしくは判定不能')
            print("引き分けもしくは判定不能")
        return black-white


    def cpu_turn1(self,Array,next):
        Max = [0,0]
        #Array_1 = copy.copy(Array)
        for i in range(0,64):
            count=0
            if self.check(Array,i,next)==True:
                temp_A = copy.copy(Array)
                temp_A = self.place(temp_A,i,next)
                for j in range(0,64):
                    if self.check(temp_A,j,next*-1)==True:
                        count+=1
                if Max[0] <= count:
                    Max[0] = count
                    Max[1] = i
        if self.check(Array,Max[1],next)==True:
            print(Max[1],"手数マン")
            Array = self.place(Array,Max[1],next)
        return Array

    def cpu_random(self,Array,next):
        i = rd.randint(0,64)
        count=0
        while self.check(Array,i,next)==False:
            i = rd.randint(0,64)
            count+=1
            if count> 10000:
                return Array
        print(i,"rand")
        Array = self.place(Array,i,next)
        return Array
    '''
        Arrayは8x8の二次元配列
        nextは-1,1
        self.check(Array,n,next)としておけるか判定してくれる関数がある（n={0,63}）
        self.place(Array,n,next)として駒を置く関数がある
    def cpu_turn2(self,Array,next):
        ここに作って
        return Array
    '''
def main():
        win = tk.Tk()
        root = App(master=win)
        #root.mainloop()        

if __name__ == "__main__":
    main()
    
       







