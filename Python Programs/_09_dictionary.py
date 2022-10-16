# Key value pair

d = {}
print(type(d))

d1 = { "Food": "Burger", "Vehicle": "Bike" }
print(d1)

print(d1["Food"])

d2 = {"Sahil" : "Bike", "Rohan" : "Car", "John" : {"Two-Wheeler" : "Scooter", "Four-Wheeler" : "Car"}}
print(d2["John"])
print(d2["John"]["Four-Wheeler"])

# Adding value in dict
d2["Michel"] = "Boat"

d2[20] = "Nothing"

print(d2)