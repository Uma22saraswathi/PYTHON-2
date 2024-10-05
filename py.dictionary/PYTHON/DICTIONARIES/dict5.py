# Create a dictionary by extracting specific keys from a given dictionary
student={
    "Name" : "Uma",
    "Roll no" : 54,
    "city":"chenai"
}
Keys=["Name","Roll no"]
n={y:student[y]for y in Keys}
print(n)
