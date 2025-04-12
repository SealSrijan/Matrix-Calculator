def matrix_addition(a,b):
    print("Matrix addition →")
    print("A + B =")
    for i in range (a_rows):
        for j in range (a_columns):
            print(a[i][j] + b[i][j], end = "\t")
        print()
    return 

def matrix_substraction(a, b):
    print("Matrix subtraction →")
    print("A - B =")
    for i in range (a_rows):
        for j in range (a_columns):
            print(a[i][j] - b[i][j], end = "\t")
        print()

def scalar_multiplication(a, b):
    print("Scalar multiplication →")
    scalar_a = int(input("Enter scalar: "))
    print("A *", scalar_a, "→")
    for i in range (a_rows):
        for j in range (a_columns):
            print(a[i][j] * scalar_a, end = "\t")
        print()
    scalar_b = int(input("Enter scalar for B: "))
    print("B *", scalar_b, "→")
    for i in range (b_rows):
        for j in range (b_columns):
            print(b[i][j] * scalar_b, end = "\t")
        print()

print("Matrix calculator","\nby Srijan\n")
ans = int(input("1. Matrix addition\n2. Matrix subtraction\n3. Both\n4. Scalar Multiplication\n5. Exit\nEnter your choice: "))
print("For 1st matrix (A) →")
a_rows = int(input("Enter number of rows: "))
a_columns = int(input("Enter number of columns: "))
a = []
for i in range(a_rows):
    row = []
    for j in range(a_columns):
        row.append(int(input("Enter number: ")))
    a.append(row)

print("\nA →\n")
for i in range(a_rows):
    for j in range(a_columns):
        print(a[i][j], end="\t")
    print()

print("\nFor 2nd matrix (B) →")
b_rows = int(input("Enter number of rows: "))
b_columns = int(input("Enter number of columns: "))
b = []
for i in range(b_rows):
    row = []
    for j in range(b_columns):
        row.append(int(input("Enter number: ")))
    b.append(row)

print("\nB →\n")
for i in range(b_rows):
    for j in range(b_columns):
        print(b[i][j], end="\t")
    print()

if ans >= 1 and ans <= 3:
    if a_rows == b_rows and a_columns == b_columns:
        print("Matrix addition and subtraction possible")
    else:
        print("Matrix addition and subtraction not possible")
        exit()

if ans == 5:
    print("Exiting...")
    exit()
elif ans == 1:
    # print("Matrix addition")
    matrix_addition(a, b)
elif ans == 2:
    # print("Matrix subtraction")
    matrix_substraction(a, b)
elif ans == 3:
    # print("Matrix addition and subtraction")
    matrix_addition(a, b)
    matrix_substraction(a, b)
elif ans == 4:
    scalar_multiplication(a, b)
else:
    print("Invalid choice")
    exit()
