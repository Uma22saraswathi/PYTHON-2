#Change the value of a key in a nested dictionary
car= {
    "brand":"ford",
    "model":"mustang",
    "year": 1964
    
}
x = car.values()
car["year"]=2018
print(x)