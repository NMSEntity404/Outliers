import random

nums = {}
usedNums = []
times = 2

for i in range(times):
    print("Minimum?")
    num = int(input("> ").lower().strip())
    nums["mi" + str(times)] = num
    print("Maximum?")
    num = int(input("> ").strip().lower())
    nums["ma" + str(times)] = num
    
while True:
    print("")
    currentNums = []
    for i in range(times):
        num = random.randint(nums["mi" + str(times)], nums["ma" + str(times)])
        try:
            while num in usedNums[i]:
                print("Regenerating " + str(num) + "...")
                num = random.randint(nums["mi" + str(times)], nums["ma" + str(times)])
        except IndexError:
            while num in usedNums:
                print("Regenerating " + str(num) + "...")
                num = random.randint(nums["mi" + str(times)], nums["ma" + str(times)])
        currentNums.append(num)
        print(num)
    usedNums.append(currentNums)
    print("")
    print("Again with the same numbers? [y]")
    true = input("> ")
    if true != "y":
        break
    
print(usedNums)