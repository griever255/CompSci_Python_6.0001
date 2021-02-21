# ## Write a function isIn that:
# # Accepts two strings as inputs
# # Returns True if either string occurs anywhere in the other,
# # otherwise returns False

# def isIn(str_a, str_b):
#     """
#     Compares two strings.
#     Returns True if either string is in the other, False otherwise
#     """
#     if str_a in str_b or str_b in str_a:
#         return True
#     else:
#         return False

# first_str = input("Enter the first string: ")
# second_str = input("Enter the second string: ")
# print(isIn(first_str, second_str))

# ## Recursion with Fibonacci sequence
# def fib(n):
#     """assumes n an int >= 0
#     Returns Fibonacci of n, number of calls"""
#     # global numCalls 
#     # numCalls += 1
#     if n == 0 or n == 1:
#         return 1, 1
#     else:
#         fib1, numCalls1 = fib(n-1)
#         fib2, numCalls2 = fib(n-2)
#         return fib1 + fib2, numCalls1 + numCalls2 + 1

# def testFib(n):
#     for i in range(n+1):
#         # global numCalls
#         # numCalls = 0
#         print(f"fib of {i} = {fib(i)[0]}")
#         print(f"fib called {fib(i)[1]}")
# testFib(10)

## Write a file 
# nameHandle = open("kids", "w")
# for i in range(2):
#     name = input("Enter name: ")
#     nameHandle.write(f"{name} \n")
# nameHandle.close()

## Append the file
# nameHandle = open("kids", "a")
# nameHandle.write("David\n")
# nameHandle.write("Andrea\n")
# nameHandle.close()

## Read a file
nameHandle = open("kids", "r")
for line in nameHandle:
    print(line[:-1])
nameHandle.close()