product = {
"name" : "Notebook",
"price" : 50,
"stock" : 10
}
print(product["name"])
print(product["stock"])
product["stock"] = 25
print(product["stock"])
product["color"] = "blue"
print(product["color"])

for key in product:
    print( product[key])