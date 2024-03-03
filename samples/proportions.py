# Calculate proportions
# n1 / d1 = n2 / d2

# Put a zero in for unknown values: 

n1 = 1
d1 = 2
n2 = 4
d2 = 0

if n2==0:
    answer = (d2 * n1) / d1
    print("n2 = ", answer)

if d2==0:
    answer = (n2 * d1) / n1
    print("d2 = ", answer)