import sys

def listunlist(s):
    clean = s.replace("left", "").replace("right", "")
    clean = clean.replace("\\", "")
    nums = [float(x) for x in clean.strip("[]").split(",")]
    return nums

y = input("y -> ")
x = input("x -> ")

y = listunlist(y)
x = listunlist(x)

print(y)
print(x)

lenX = len(x)
lenY = len(y)

if lenX != lenY:
    sys.exit("The length of x and y are not equal!")

dic = {}
for i in range(lenX):
    dic[x[i]] = y[i]

print("")
print(dic)

x.sort()

reorderY = []

for i in range(lenX):
    reorderY.append(dic[x[i]])

print("")
print("X:")
print(x)
print("")
print("Y:")
print(reorderY)