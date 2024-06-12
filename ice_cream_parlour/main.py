from functions import (
    add_seasonal_flavor, add_ingredient, add_customer_suggestion, 
    add_allergen, add_to_cart, get_seasonal_flavors, search_seasonal_flavors, get_cart
)

def main():
    while True:
        print("\nWelcome to the Ice Cream Parlor Cafe!")
        print("1. View Seasonal Flavors")
        print("2. Search Seasonal Flavors")
        print("3. Add Allergen")
        print("4. View Cart")
        print("5. Add to Cart")
        print("6. Exit")
        
        choice = input("Please choose an option: ")

        if choice == '1':
            flavors = get_seasonal_flavors()
            print("\nSeasonal Flavors:")
            for flavor in flavors:
                print(f"ID: {flavor[0]}, Flavor: {flavor[1]}, Description: {flavor[2]}, Availability: {flavor[3]}")

        elif choice == '2':
            keyword = input("Enter a keyword to search: ")
            flavors = search_seasonal_flavors(keyword)
            print("\nSearch Results:")
            for flavor in flavors:
                print(f"ID: {flavor[0]}, Flavor: {flavor[1]}, Description: {flavor[2]}, Availability: {flavor[3]}")

        elif choice == '3':
            allergen = input("Enter the name of the allergen: ")
            add_allergen(allergen)
            print(f"Allergen '{allergen}' added successfully.")

        elif choice == '4':
            cart_items = get_cart()
            print("\nYour Cart:")
            for item in cart_items:
                print(f"ID: {item[0]}, Product: {item[1]}")

        elif choice == '5':
            product_name = input("Enter the product name to add to cart: ")
            add_to_cart(product_name)
            print(f"Product '{product_name}' added to cart.")

        elif choice == '6':
            print("Thank you for visiting the Ice Cream Parlor Cafe!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
