#pattern
n=int(input("enter a number of rows")) #user to enter a number
for row in range (n,0,-1):
    for column in range(1,row+1):
        print(column, end=" ") # end=" " separated by a space.

    print() #This line prints a newline 

