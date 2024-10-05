
num_terms = 10
a, b = 0, 1 #first two terms in the Fibonacci series.
for _ in range(num_terms):# it is a loop statement, ithu num_terms times nadakkum.
    print(a) # print(a) na current Fibonacci term-a print pannum. a ipo 0 iru kku, 
    temp = a + b #temp la a and b values-a add pannitu store pannirukkom. Ithu next term-a calculate panra value.

    a = b
    b = temp