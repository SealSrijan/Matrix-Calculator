#Functions Declaration
#-----------------------------------

#Matrix Entry
def matrix_entry():
    
    #Entry of A matrix
    print("For 1st matrix (A) →")
    a_rows = int(input("Enter number of rows: "))
    a_columns = int(input("Enter number of columns: "))
    a = []
    for i in range(a_rows):
        row = []
        for j in range(a_columns):
            row.append(int(input("Enter number: ")))
        a.append(row)

    #Displaying A
    print("\nA →\n")
    for i in range(a_rows):
        for j in range(a_columns):
            print(a[i][j], end="\t")
        print()

    #Entry of B
    print("\nFor 2nd matrix (B) →")
    b_rows = int(input("Enter number of rows: "))
    b_columns = int(input("Enter number of columns: "))
    b = []
    for i in range(b_rows):
        row = []
        for j in range(b_columns):
            row.append(int(input("Enter number: ")))
        b.append(row)

    #Displaying B
    print("\nB →\n")
    for i in range(b_rows):
        for j in range(b_columns):
            print(b[i][j], end="\t")
        print()

    return a, b, a_rows, a_columns, b_rows, b_columns

#Matrix Addition
def matrix_addition():
    a, b, a_rows, a_columns, b_rows, b_columns = matrix_entry()
    if a_rows != b_rows or a_columns != b_columns:
        print("Error: Matrices must have the same dimensions for addition.")
        return
    print("\nMatrix addition →")
    print("\nA + B =\n")
    for i in range (a_rows):
        for j in range (a_columns):
            print(a[i][j] + b[i][j], end = "\t")
        print()
    return 

#Matrix Substraction 
def matrix_substraction():
    a, b, a_rows, a_columns, b_rows, b_columns = matrix_entry()
    if a_rows != b_rows or a_columns != b_columns:
        print("Error: Matrices must have the same dimensions for subtraction.")
        return
    print("\nMatrix subtraction →")
    print("\nA - B =\n")
    for i in range (a_rows):
        for j in range (a_columns):
            print(a[i][j] - b[i][j], end = "\t")
        print()

#Scalar multiplication
def scalar_multiplication():
    a, b, a_rows, a_columns, b_rows, b_columns = matrix_entry()
    print("\nScalar multiplication →")
    scalar_a = int(input("Enter scalar: "))
    print("\nA *", scalar_a, "→")
    for i in range (a_rows):
        for j in range (a_columns):
            print(a[i][j] * scalar_a, end = "\t")
        print()
    scalar_b = int(input("\nEnter scalar for B: "))
    print("\nB *", scalar_b, "→")
    for i in range (b_rows):
        for j in range (b_columns):
            print(b[i][j] * scalar_b, end = "\t")
        print()

#Matrix Multiplication
import numpy as np
def matrix_multiplication():
    a, b, _, a_columns, b_rows, _ = matrix_entry()
    if a_columns != b_rows:
        print("Error: Columns of A must equal rows of B for multiplication.")
    
    A = np.array(a)
    B = np.array(b)
    AB = np.dot(A, B)
    print("\nMatrix Multiplication (A x B) →")
    for row in AB:
        for val in row:
            print(val, end="\t")
        print()
    return

#------------------------------------

#Loop for repetition
print("Matrix calculator","\nby Srijan")
while True:
    #Contents
    print("\n1. Matrix addition")
    print("2. Matrix subtraction")
    print("3. Both")
    print("4. Scalar Multiplication")
    print("5. Matrix Multiplication")
    print("6. Exit")
    ans = int(input("\nEnter your choice: "))

    # if-else part
    if ans == 1:
        matrix_addition()
    elif ans == 2:
        matrix_substraction()
    elif ans == 3:
        matrix_addition()
        matrix_substraction()
    elif ans == 4:
        scalar_multiplication()
    elif ans == 5:
        matrix_multiplication()
    elif ans == 6:
        print("\n\t\texiting...")
        break
    else:
        print("\nWrong choice...\t")
