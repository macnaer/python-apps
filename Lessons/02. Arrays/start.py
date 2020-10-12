# num = [8, 3, 5, 4, 4, 6, [4, False]]
# print(num)
# print("type => ", type(num))

# num[2] = "white"
# print(num)
# print("=======================")
# print(num[6][1])
# print(num[-1])

# print("*********************************")

# for item in num:
#     print(item)

# print("Length => ", len(num))
# new_item = int(input("Enter number append ===>>> "))
# num.append(new_item)
# print(num)
# num.pop(6)
# print(num)
# print("===================INCERT=================")
# ins = input("Enter value")
# ins_index = int(input("Enter index ===>>> "))
# num.insert(ins_index, ins)
# print(num)
# num1 = [4, 65, 23, 5, 346, 457, 657, 657, 58, 678, 6]
# num1.reverse()
# print(num1)
# num1.sort()
# print(num1)


# ========================== Tuple =======================#
# currency = (2, 4, 5, 6, 7, 7, 8)
# print("type => ", type(currency))
# print(currency)
# for item in currency:
#     print(item)

# print("By index =>> ", currency[0])
# import requests

# URL = "https://api.covid19api.com/summary"
# covid19 = requests.get(URL)
# covid19 = covid19.json()

# for item in covid19["Countries"]:
#     print(item['Country'])


#========================Dictionary==================#
countries = {"UA": "Ukraine", "US": "United States",
             "IT": "Italy", "FR": "France"}

for key in countries:
    country = countries[key]
    print(key, " = ", country)

countries['IT'] = "Italy2"
print(countries['IT'])
del(countries["IT"])

print("=================================")
for key in countries:
    country = countries[key]
    print(key, " = ", country)

new_countries = {"En": "England", "FN": "Finland"}
countries.update(new_countries)

print("=============After update===============")

for key in countries:
    country = countries[key]
    print(key, " = ", country)
