primes = [2, 3, 5, 7, 11]
print("Sum of", primes, "=", sum(primes))

print("Maximum of", primes, "=", max(primes))

print("Minimum of", primes, "=", min(primes))

print("Addding 13 to", primes, end="  = ")
primes.append(13)
print(primes)

print("Extending", primes, end=" = ")
primes.extend([17, 19, 23, 29])
print(primes)

print("Reversing", primes, end=" = ")
primes.reverse()
print(primes)

print("Popping last element of", primes, end=" = ")
primes.pop()
print(primes)

print("Popping 2nd element of", primes, end=" = ")
primes.pop(1)
print(primes)

print("Count of 29 in", primes, "=", primes.count(29))

print("Index of 11 in", primes, "=", primes.index(11))

print("Inserting 31 at index 0 in", primes, end= " = ")
primes.insert(0, 31)
print(primes)

print("Removing 13 from", primes, end=" = ")
primes.remove(13)
print(primes)

print("Length of", primes, "=", len(primes))

print("Sorting", primes, "in ascending order = ", sorted(primes))

print("Sorting", primes, "in descending order = ", sorted(primes, reverse=True))

primes_sqaures = list(map(lambda prime: prime * prime, primes))
print("Zipping", primes, "and", primes_sqaures, "=", list(zip(primes, primes_sqaures)))