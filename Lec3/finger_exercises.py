## Find the squareroot of a negative number
# x = -25
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = max(1.0, abs(x))
# ans = (high+low)/2.0
# while abs(ans**2-abs(x)) >= epsilon:
#     numGuesses += 1
#     if ans**2 < abs(x):
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2.0
#     print("low =", low, "high = ", high, "ans = ", ans)
# print("numGuesses =", numGuesses)
# if x > 0:
#     print(ans, "is really close to the square root of", x)
# else:
#     print(str(ans)+"i is really close to the square root of", x)

## Find the cubed root of a positive or negative number
# x = -27
# epsilon = 0.01
# numGuesses = 0
# if x > 0:
#     low = 0.0
# else:
#     low = x
# high = max(1.0, x)
# ans = (high+low)/2.0
# while abs(ans**3-x) >= epsilon:
#     numGuesses += 1
#     if ans**3 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2.0
#     print("low =", low, "high = ", high, "ans = ", ans)
# print("numGuesses =", numGuesses)
# print(ans, "is really close to the cubed root of", x)

## Find the decimal equivalent of 10011
# b = "10011"
# sum = 0
# index = 0
# for char in b[::-1]:
#     sum += int(char)*2**index
#     index += 1
# print(sum)

## Compare the Newton-Raphson method to bisection search

# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0
while abs(guess*guess - y) >= epsilon:
    guess -= ((guess**2)-y)/(2*guess)
    numGuesses += 1
print("Square root of", y, "is about", guess, "in", numGuesses, "guesses")

# Bisection search for square root
# Find x such that x**2 - 24 is within epsilon of 0
y = 24.0
low = 0
high = y
guess = (high+low)/2.0
numGuesses = 0
while abs(guess*guess-y) >= epsilon:
    if guess*guess > y:
        high = guess
    else:
        low = guess
    guess = (high+low)/2.0
    numGuesses += 1
print("Square root of", y, "is about", guess, "in", numGuesses, "guesses")