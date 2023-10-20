name: str = "Numan Abubakar"
father_name: str = "Muhammad Abubakar"
age: int = 21


# card:str = f"""
# My Information
# Name : {name}
# Father Name : {father_name}
# age : {age}
# """
card: str = """
My Information
Name : {}
Father Name : {}
age : {}
""".format(name, father_name, age)
print(card)
