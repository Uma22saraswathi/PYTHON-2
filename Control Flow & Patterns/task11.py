#Write a program to display all prime numbers within a range
start = 1
end = 25

for num in range(start, end + 1):
    if num > 1: # all prime #s are greater than 1
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)