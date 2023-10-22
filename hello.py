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
