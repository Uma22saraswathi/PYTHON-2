original_list = ["python","is"," ","a","programming"," "," language"]
print (original_list)
def not_whitespace(s):
    return s.strip() != ""
updated_list = list(filter(not_whitespace, original_list))
print(updated_list)