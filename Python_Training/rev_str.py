string = input("Enter a string: ")
s = string.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))