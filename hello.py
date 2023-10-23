from typing import Any

name: str = "Numan Abubakar"
father_name: str = "Muhammad Abubakar"
age: int = 21

# f-string
card2: str = f"""
My Information
Name: {name}
Father Name: {father_name}
age: {age}
"""
# without f-string
card: str = """
My Information
Name : {}
Father Name : {}
age : {}
""".format(name, father_name, age)
# print(card)

message: str = f""" Hello {name}, Hope you are doing best! """
# print(message)
name_lstrip = "                  numan abubakar                      "
print(name_lstrip.lstrip())
print(name_lstrip.rstrip())
print(name_lstrip.strip())

#  list (array)

names: list[str] = ["ALi", "Umar", "Abdullah"]
print(*names)  # using * for printing all members

print(names[:2:1])
characters: list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(characters)
# defualt slicing go from left to right
print(characters[0:2])  # 0= include : index 2-1 = 1
print(characters[:2])  # not pass any number = all
print(characters[-26:-24])  # 0= include : index -24-1 = -25
print(characters[0:2:1])  # 0= include : index 2-1 = 1
print(characters[0:2:])  # 0= include : index 2-1 = 1
print(names)

del names[1]  # delete 1 index element

print(names)
a : str = print("Pakistan") # none-return function
print(a)

# ->                    0        1         2
names2 : list[Any] = ["Qasim","Sir Zia", "Sir Inam", 20, True]
# <-                    -3     -2          -1

del names2[3]
print(names2)
names : list[str] = ['a','b']

names.append("Sir Zia")# add element in last
names.append("Sir Inam") # add element in last
names.append("Qasim")# add element in last

print(names)