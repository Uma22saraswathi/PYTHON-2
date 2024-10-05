#Get the key of the minimum value from a dictionary
students={ "uma":25, "saraswathi":22, "lara":19}
min_value=min(students.values())
min_keys=[key for key in students if students[key]==min_value]
print(min_keys)