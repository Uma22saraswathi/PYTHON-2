#Find the sum of the series up to n terms
n = int(input("Enter the number of terms: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i  # Add the current term to the total sum
print("The sum of the first", n, "natural numbers is:", total_sum)
