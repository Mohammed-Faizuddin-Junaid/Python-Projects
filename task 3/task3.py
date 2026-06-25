# Importing libraries 
import numpy as np    
# Defining an empty matrix to add the rows in the form of list
def get_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    matrix = []
# converting input  strings into matrix.
    for i in range(rows):
       row = list(map(int, input("Enter row: ").split()))
       matrix.append(row)
    return matrix
# Creating Matrix Opreation Menu
while True:
    print("Welcome to Matrix Operations Tool")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Transpose")
    print("5. Inverse")
    print("6. Determinant")
    print("7. Exit")
# Takes the user input.    
    choice = input("Enter your choice: ")
    
    if choice == "7":
        print("Goodbye!")
        break
# Performs Addition Matrix 
    if choice == "1":
       matrix_a = get_matrix("Matrix A")   # Defined function
       matrix_b = get_matrix("Matrix B")   #  Defined  function
       A = np.array(matrix_a)              # numpy function
       B = np.array(matrix_b)              # numpy function
       result = A + B
       print("Result:")
       print(result)
# Performs Subtraction Matrix 
    elif choice == "2":
       matrix_a = get_matrix("Matrix A")   # Defined function
       matrix_b = get_matrix("Matrix B")   #  Defined  function
       A = np.array(matrix_a)              # numpy function
       B = np.array(matrix_b)              # numpy function
       result = A - B
       print("Result:")
       print(result)
# Performs Multiplication Matrix 
    elif choice == "3":
       matrix_a = get_matrix("Matrix A")   # Defined function
       matrix_b = get_matrix("Matrix B")   #  Defined  function
       A = np.array(matrix_a)              # numpy function
       B = np.array(matrix_b)              # numpy function
       result = np.dot(A,B)
       print("Result:")
       print(result)
# Performs Transpose Matrix 
    elif choice == "4":
       matrix_a = get_matrix("Matrix A")   # Defined function
       A = np.array(matrix_a)              # numpy function 
       result = np.transpose(A) 
       print("Result:")
       print(result)   
# Performs  Matrix Inverse 
    elif choice == "5":
       matrix_a = get_matrix("Matrix A")   # Defined function
       A = np.array(matrix_a, dtype=float)
       if A.shape[0] != A.shape[1]:
          print("Error : Matrix must be square for Inverse")           
       else:  
          result = np.linalg.inv(A)
          print("Result:")
          print(result)   
# Performs Determinant Matrix 
    elif choice == "6":
       matrix_a = get_matrix("Matrix A")   # Defined function
       A = np.array(matrix_a, dtype=float)
       if A.shape[0] != A.shape[1]:
          print("Error : Matrix must be square for Determinant")           
       else: 
         result = np.linalg.det(A)
         print("Result:")
         print(result)
    else:
       print("Invalid choice. Please enter 1-7")      
       
