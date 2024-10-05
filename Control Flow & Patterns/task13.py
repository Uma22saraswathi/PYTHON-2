#Find the factorial of a given number
num = 5 #num nu oru variable,  factorial find panna pora number. 
factorial = 1 #factorial-nu oru variable create pannirukkom,initially ithu 1 set pannirukku.Idha multiplypannitu result calculate
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")
