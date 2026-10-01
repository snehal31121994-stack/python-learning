
for number in range(1, 4):
    supplier = input(f"Enter supplier {number}: ")
    product = input("What product does this supplier provide? ")
    availability = input("Is the product available? Enter yes or no: ")

    print(f"{supplier} supplies {product}.")

    if availability == "yes":
        print("Available to order.")
    else:
        print("Follow up with the supplier.")
