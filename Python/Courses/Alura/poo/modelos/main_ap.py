from restaurant import Restaurant

restaurant_praca = Restaurant('Praça', 'Gourmet')
restaurant_praca.add_evaluation('John', 8)
restaurant_praca.add_evaluation('Alice', 9)
restaurant_praca.add_evaluation('Bob', 7)

restaurant_praca.restaurant_status()

def main():
    """Main function."""
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()