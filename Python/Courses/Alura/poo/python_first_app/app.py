import os

restaurants = [
    {'name':'Praça', 'category':'Japanese', 'active':False}, 
    {'name':'Pizza Suprema', 'category':'Pizza', 'active':True},
    {'name':'Cantina', 'category':'Italian', 'active':False}
    ]

def show_name():
    """This function shows the name of the application"""
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def show_menu():
    """This function shows the menu of the application"""
    print("1. Register restaurant")
    print("2. List restaurants")
    print("3. Reataurant status")
    print("4. Close\n")

def close_app():
    """This function closes the application"""
    subtitle("Closing application")
    print("Goodbye!")

def return_to_menu():
    """This function returns to the main menu
    
    output: return to the main menu"""
    input("Press enter to return to the menu")
    main()    

def invalid_option():
    """This function shows an invalid option message
    
    output: return to the main menu"""
    print("Invalid option\n")
    return_to_menu()

def subtitle(texto):
    """This function shows a subtitle
    
    input: str - subtitle text"""
    os.system("clear")
    print(texto)
    print("")

def register_restaurant():
    """This function registers a restaurant
    
    input: restaurant name, restaurant category
    
    output: add a new restaurant to the list"""
    subtitle("Registering restaurant")
    restaurant_name = input(f"Enter the restaurant name: ")
    restaurant_category = input(f"Enter the {restaurant_name} category: ")
    restaurant_data = {'name':restaurant_name, 'category':restaurant_category, 'active':False}
    restaurants.append(restaurant_data)
    print(f"The restaurant {restaurant_name} was registered successfully\n")
    
    return_to_menu()

def list_restaurants():
    """This function lists the restaurants
    
    output: list of restaurants"""
    subtitle("Listing restaurants")

    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_category = restaurant['category']
        restaurant_active = 'Active' if restaurant['active'] else 'Inactive'
        print(f"- {restaurant_name.ljust(20)} | {restaurant_category.ljust(20)} | {restaurant_active}")
    print("")

    return_to_menu()

def restaurant_status():
    """This function changes the restaurant status
    
    input: restaurant name
    
    output: change the restaurant status"""
    subtitle("Changing restaurant status")
    restaurant_name = input("Enter the restaurant name: ")
    restaurant_founded = False

    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            restaurant_founded = True
            restaurant['active'] = not restaurant['active']
            print(f"The restaurant {restaurant_name} is now {'active' if restaurant['active'] else 'inactive'}")
            return_to_menu()
    if not restaurant_founded:
        print(f"The restaurant {restaurant_name} was not found")
        return_to_menu()

def choose_option():
    """This function chooses the option
    
    input: Client option

    output: Option chosen by the client
    
    """
    try:
        client_option = int (input("Choose an option: "))

        if client_option == 1:
            register_restaurant()
        elif client_option == 2:
            list_restaurants()
        elif client_option == 3:
            restaurant_status()
        elif client_option == 4:
            close_app()
        else:
            invalid_option()
    except:
        invalid_option()

def main():
    """This function is the main function of the application"""
    os.system("clear")
    show_name()
    show_menu()
    choose_option()

if __name__ == "__main__":
    main()
