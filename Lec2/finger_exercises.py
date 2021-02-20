#############################
## Finger Exercise 1 and 2 ##
#############################

# # Ask the user for ten integers
# integers = []
# for i in range(10):
#     integers.append(int(input("Enter integer number " + str(i+1) + ": ")))

# # Determine the largest odd integer in integers
# largest_odd = 0
# for i in integers:
#     if i % 2 == 1 and i > largest_odd:
#         largest_odd = i

# # Print the largest odd, or if there's no odds
# if largest_odd != 0:
#     print("The largest odd integer is:", largest_odd)
# else:
#     print("None of these numbers are odd")

#######################
## Finger Exercise 3 ##
#######################

# Given a string of comma-separated decimals, print the sum
s = "1.23,2.4,3.123"

sum = 0
index_start = 0
index_end = 0
for c in s:
    if c == ",":
        sum += float(s[index_start:index_end])
        index_start = index_end+1
    index_end += 1 
sum += float(s[index_start:len(s)])
print(sum)