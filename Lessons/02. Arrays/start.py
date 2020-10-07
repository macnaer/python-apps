num = [8, 3, 5, 4, 4, 6, [4, False]]
print(num)
print("type => ", type(num))

num[2] = "white"
print(num)
print("=======================")
print(num[6][1])
print(num[-1])

print("*********************************")

for item in num:
    print(item)

print("Length => ", len(num))
new_item = int(input("Enter number append ===>>> "))
num.append(new_item)
print(num)
num.pop(6)
print(num)
print("===================INCERT=================")
ins = input("Enter value")
ins_index = int(input("Enter index ===>>> "))
num.insert(ins_index, ins)
print(num)
num1 = [4, 65, 23, 5, 346, 457, 657, 657, 58, 678, 6]
num1.reverse()
print(num1)
num1.sort()
print(num1)
