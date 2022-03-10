#Fibonacci Numbers until a user defined point
n = int(input("Please enter a number until you'd like to get Fibonacci Numbers:"))
fibonacci = [1, 1]
i = 0
j = 1
while i < n and j < n:
 fibonacci.append(fibonacci[i] + fibonacci[j])
 if fibonacci[-1] >= n:
   break
 i += 1
 j += 1
print(fibonacci)
