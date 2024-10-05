#remove empty string
print("Task : 15 remove empty string ")
text_list=["","python","","is","best"," "]
print("original list : ", str(text_list))
while(""in text_list):
    text_list.remove("")
print("modify list is : ",str(text_list))    