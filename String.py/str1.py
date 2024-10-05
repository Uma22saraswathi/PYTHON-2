# string
#Create a string made of the first, middle, and last character
print("String Task : 1 : Create a string made of the first, middle, and last character : ")
s1 = "Americas"
s2 = "Japan"
def fun(str1,str2):
    l1 = int(len(str1)/2)
    l2 = int(len(str2)/2)
    
    S = str1[0]+str2[0] +str1[l1]+ str2[l2]+str1[-1]+str2[-1]
    return S
result = fun('Americas','Japan')
print(result)
print("_____________________________________________________________")









    
  


