#Delete a list of keys from a dictionary
student={
    "name":"uma",
    "age":21,
    "roll no":54,
    "school":"tilak"
}
keys_to_delete=["roll no","school"]
for i in keys_to_delete:
    if i in student:
        del student[i]
print(student)        