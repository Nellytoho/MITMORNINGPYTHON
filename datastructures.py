# List datastructure
# A list enables you to change data
myclassmate = ["Nelly", "Joy", "Faith", "Daniel"]
mynos = [4, 9, 20, 3, 1, 50, -9]
myclassmate[0] = "Daniel"
print(myclassmate)

mynos.sort()
myclassmate.append(" Cynthia")
myclassmate.insert(2, "Michael")
print(myclassmate)
print(mynos)

myclassmate = ["Nelly", "Joy", "Faith", "Daniel"]

# for loop
for myclassmate in myclassmate:
    print(myclassmate)
# this is a tuple
countries = ("Kenya", "Uganda", "Tanzania", "Burundi")
print(countries)
# sets datastructures

cars = {"Toyota", "Nissan", "Mercedes", "Subaru", "Rangerover"}
print(cars)

# for loops
cars = {"Toyota", "Nissan", "Mercedes", "Subaru", "Rangerover"}
for cars in cars:
    print(cars)

# Dictionaries datastructures

matunda = {"price": 50, "color": "Yellow","Name": "banana"}
for matunda in matunda:
    print(matunda)

bei=matunda["price"]
matunda["shape"]= "oval"
print(bei)
