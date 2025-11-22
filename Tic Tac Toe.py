"""
player(X)
player(O)

1.alternative starts 
2.tie counts
3.win count
4.blink
"""
from tkinter import Tk
from tkinter import *
from tkinter import messagebox
import sys
import os

matrix=[
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]
playerO=0
playerX=0
tie=0
chance=0
root=Tk()
root.title("Tic tac Tao")
root.geometry("900x900")
root.config(bg='black')

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # PyInstaller temporary folder
else:
    base_path = os.path.abspath(".")

# Full path to icon inside EXE or during .py run
icon_path = os.path.join(base_path, "icon.ico")
root.iconbitmap(icon_path)

header=Frame(root,height='200',width='700',bg='black')
header.pack(side='top')
header1=Frame(header,height='100',width='700',bg='black')
header1.pack(side='top')
header2=Frame(header,height='100',width='700',bg='black')
header2.pack(side='top')

container=Frame(root,height='700',width='700',bg='white')
container.pack(padx='0',pady='0')
#header things

def check_full(matrix):
    for i in matrix:
        if '_' in i:
            return 'not full'
    return 'full'
def check(user,ch1,ch):
    x,y=user
    temp=0
    global chance,matrix
    if matrix[x][y]!='_':
        messagebox.showwarning("Warning",f'Already used')
    else:
        matrix[x][y]=ch
        btn_change(ch1)
        chance = 1 if chance==0 else 0
        for i in range(3):
            if matrix[i][0]==matrix[i][1]==matrix[i][2]!='_':
                temp=1
                break
            if matrix[0][i]==matrix[1][i]==matrix[2][i]!='_':
                temp=1
                break
        if matrix[0][0]==matrix[1][1]==matrix[2][2]!='_':
                temp=1
        if matrix[0][2]==matrix[1][1]==matrix[2][0]!='_':
                temp=1
        if check_full(matrix)=='full':
            return 2
    return temp
def clear_buttons():
    global matrix
    matrix=[
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
   ]
    btn1.config(text='')
    btn2.config(text='')
    btn3.config(text='')
    btn4.config(text='')
    btn5.config(text='')
    btn6.config(text='')
    btn7.config(text='')
    btn8.config(text='')
    btn9.config(text='')
    
def display(temp,char):
    global playerX,playerO,tie
    if temp == 1 and char == 'X':
        playerX+=1
        messagebox.showinfo("X wins","clearing")
        l_playerxscore.config(text=playerX)
        clear_buttons()
    elif temp == 1 and char == 'O':
        playerO+=1
        messagebox.showinfo("O wins","clearing")
        l_playerOscore.config(text=playerO)
        clear_buttons()
    elif temp == 2: 
        tie+=1
        messagebox.showinfo("Tie","clearing")
        l_tiescore.config(text=tie)
        clear_buttons()
    else:
        pass
def btn_change(ch):
    match ch:
        case 1:
            if chance == 0:
                btn1.config(text='X')
            else:
                btn1.config(text='O')
        case 2:
            if chance == 0:
                btn2.config(text='X') 
            else:
                btn2.config(text='O')
        case 3:
            if chance == 0:
                btn3.config(text='X') 
            else:
                btn3.config(text='O')
        case 4:
            if chance == 0:
                btn4.config(text='X') 
            else:
                btn4.config(text='O')
        case 5:
            if chance == 0:
                btn5.config(text='X') 
            else:
                btn5.config(text='O')
        case 6:
            if chance == 0:
                btn6.config(text='X') 
            else:
                btn6.config(text='O')
        case 7:
            if chance == 0:
                btn7.config(text='X') 
            else:
                btn7.config(text='O')
        case 8:
            if chance == 0:
                btn8.config(text='X') 
            else:
                btn8.config(text='O')
        case 9:
            if chance == 0:
                btn9.config(text='X') 
            else:
                btn9.config(text='O')


def change(no):
    global playerX,playerO,tie,chance
    match no:
        case 1:
            if chance == 0:
                user1=[0,0]
                temp=check(user1,no,'X') 
                display(temp,'X')
            else:
                user2=[0,0]
                temp=check(user2,no,'O')
                display(temp,'O')
        case 2:
            if chance == 0:
                user1=[0,1]
                temp=check(user1,no,'X')
                display(temp,'X') 
            else:
                user2=[0,1]
                temp=check(user2,no,'O')
                display(temp,'O')
        case 3:
            if chance == 0:
                user1=[0,2]
                temp=check(user1,no,'X')
                display(temp,'X') 
            else:
                user2=[0,2]
                temp=check(user2,no,'O')
                display(temp,'O')
        case 4:
            if chance == 0:
                user1=[1,0]
                temp=check(user1,no,'X')
                display(temp,'X') 
            else:
                user2=[1,0]
                temp=check(user2,no,'O')
                display(temp,'O')
        case 5:
            if chance == 0:
                user1=[1,1]
                temp=check(user1,no,'X')
                display(temp,'X') 
            else:
                user2=[1,1]
                temp=check(user2,no,'O')
                display(temp,'O')
        case 6:
            if chance == 0:
                user1=[1,2]
                temp=check(user1,no,'X')
                display(temp,'X') 
            else:
                user2=[1,2]
                temp=check(user2,no,'O')
                display(temp,'O')
        case 7:
            if chance == 0:
                user1=[2,0]
                temp=check(user1,no,'X')
                display(temp,'X') 
            else:
                user2=[2,0]
                temp=check(user2,no,'O')
                display(temp,'O')
        case 8:
            if chance == 0:
                user1=[2,1]
                temp=check(user1,no,'X')
                display(temp,'X') 
            else:
                user2=[2,1]
                temp=check(user2,no,'O')
                display(temp,'O')
        case 9:
            if chance == 0:
                user1=[2,2]
                temp=check(user1,no,'X')
                display(temp,'X') 
            else:
                user2=[2,2]
                temp=check(user2,no,'O')
                display(temp,'O')
        case 'win':
            pass        


container1=Frame(container,height='200',width='700',bg='white')
container1.pack()
btn1=Button(container1,text='',font=('Arial',62),bg='black',fg='white',height='2',width='5',command=lambda :change(1))
btn1.pack(side='left')
btn2=Button(container1,text='',font=('Arial',62),bg='black',fg='white',height='2',width='5',command=lambda :change(2))
btn2.pack(side='left',padx='10')
btn3=Button(container1,text='',font=('Arial',62),bg='black',fg='white',height='2',width='5',command=lambda :change(3))
btn3.pack(side='left')

container2=Frame(container,height='200',width='700',bg='white')
container2.pack(pady='10')
btn4=Button(container2,text='',font=('Arial',62),bg='black',fg='white',height='2',width='5',command=lambda :change(4))
btn4.pack(side='left')
btn5=Button(container2,text='',font=('Arial',62),bg='black',fg='white',height='2',width='5',command=lambda :change(5))
btn5.pack(side='left',padx='10')
btn6=Button(container2,text='',font=('Arial',62),bg='black',fg='white',height='2',width='5',command=lambda :change(6))
btn6.pack(side='left')


container3=Frame(container,height='200',width='700',bg='white')
container3.pack()
btn7=Button(container3,text='',font=('Arial',62),bg='black',fg='white',height='2',width='5',command=lambda :change(7))
btn7.pack(side='left')
btn8=Button(container3,text='',font=('Arial',62),bg='black',fg='white',height='2',width='5',command=lambda :change(8))
btn8.pack(side='left',padx='10')
btn9=Button(container3,text='',font=('Arial',62),bg='black',fg='white',height='2',width='5',command=lambda :change(9))
btn9.pack(side='left')
     

l_playerx = Label(header1,text='player(x):',font=('Arial',30),fg='white',bg='black')
l_playerx.pack(side=LEFT, padx=17, pady=5)
l_playerO = Label(header1,text='player(O):',font=('Arial',30),fg='white',bg='black')
l_playerO.pack(side=LEFT, padx=17, pady=5)
l_tie = Label(header1,text='ties:',font=('Arial',30),fg='white',bg='black')
l_tie.pack(side=LEFT, padx=17, pady=5)

l_playerxscore = Label(header2,text='     ',font=('Arial',30),fg='white',bg='black')
l_playerxscore.pack(side=LEFT, padx=47, pady=5)
l_playerOscore = Label(header2,text='      ',font=('Arial',30),fg='white',bg='black')
l_playerOscore.pack(side=LEFT, padx=87, pady=5)
l_tiescore = Label(header2,text='      ',font=('Arial',30),fg='white',bg='black')
l_tiescore.pack(side=LEFT, padx=30, pady=5)


root.mainloop()