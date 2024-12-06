import random
import math
# x mean true and o mean false
# x win mean 5 and o win mean 6 7 if nothing
def result(mat):

    for i in range(1,4):
        if mat[1][i]==5 and mat[2][i]==5 and mat[3][i]==5:
            return 500
        if mat[i][1]==5 and mat[i][2]==5 and mat[i][3]==5:
            return 500
    if mat[1][1]==5 and mat[2][2]==5 and mat[3][3]==5:
        return 500
    if mat[1][3]==5 and mat[2][2]==5 and mat[3][1]==5:
        return 500
    

    for i in range(1,4):
        if mat[1][i]==6 and mat[2][i]==6 and mat[3][i]==6:
            return 600
        if mat[i][1]==6 and mat[i][2]==6 and mat[i][3]==6:
            return 600
    if mat[1][1]==6 and mat[2][2]==6 and mat[3][3]==6:
        return 600
    if mat[1][3]==6 and mat[2][2]==6 and mat[3][1]==6:
        return 600
    return 700


def print_matrix(mat):

    mat1=[[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
    for i in range(4):
        for j in range(4):
            if mat[i][j]==5:
                mat1[i][j]="x"
            elif mat[i][j]==6:
                mat1[i][j]="o"
            elif mat[i][j]==7:
                mat1[i][j]=" "
            else:
                mat1[i][j]="0"
    print((mat1[1][1])+" | "+(mat1[1][2])+" | "+(mat1[1][3])+"\n")
    print((mat1[2][1])+" | "+(mat1[2][2])+" | "+(mat1[2][3])+"\n")
    print((mat1[3][1])+" | "+(mat1[3][2])+" | "+(mat1[3][3])+"\n")


#0 for tie 1 for win and -1 for loss
# x False o=true
def ai(mat,used,pos,turn):
    i=0
    j=0
    
    temp=[[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
   

    temp = [row[:] for row in mat]
    
    
    change_mat(temp,pos,turn)
    
    temp2 = used.copy()
    temp2.append(pos)
    if result(temp)==600:
        return 1
    elif result(temp)==500:
        return -1
            
    y=0

    if turn==True:
        best_case=1
        
    else:
        best_case=-1
        

    for i in range(1,10):
 
        if i not in temp2:
            y= ai(temp,temp2,i,not(turn))
            if best_case==y:
                return best_case
        
    return 0        

           
            
            



def change_mat(mat,given,chance):
   
    if (given%3)!=0:

        if chance==True:
            mat[(given//3)+1][given%3]=5
        else:
            mat[(given//3)+1][given%3]=6

    if given==3 or given==6 or given==9:
        if chance==True:
            mat[int(given/3)][3]=5
        else:
            mat[int(given/3)][3]=6




Z=None
print("Tic-Tac-Toe Game")
print("Position numbering:")
print("1 | 2 | 3")

print("4 | 5 | 6")

print("7 | 8 | 9")



print("For whole game numbering will be in this order\n")

count =0
used=[]

mat=[[0,0,0,0],[0,7,7,7],[0,7,7,7],[0,7,7,7]]
print_matrix(mat)

while result(mat) == 700 and count!=9:
    #print_matrix(mat)
    print("your Turn")
    while True:
        
        try:
            given = int(input("Enter a number between 1 and 9: "))
        
            if 1 <= given <= 9:
                 break  # Exit the loop if the input is valid
            else:
                print("Invalid Input. Please enter a number between 1 and 9.")
    
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

    count = count +1

    chance=True
    change_mat(mat,given,chance)

    used.append(given)
    print_matrix(mat)
    max=-1
    if count<9:
        i=1
        while i<10:
            if count==1 and 5 not in used:
                computer=5
                break
            if i not in used:
                
                temp = [row[:] for row in mat]
                y=ai(temp,used,i,not(chance))
                if y>=max:
                    max=y
                    computer=i
            i=i+1
        

               
        chance = False
        change_mat(mat,computer,chance)
    used.append(computer)

    count = count +1


    print("computer's turn")
    print_matrix(mat)
    y= result(mat)
    if y==500:
        print("You won")
        break
    if y==600:
        print("You Lose")
        break
    if count==9:
        print("Its a Tie")
        break
    
    


