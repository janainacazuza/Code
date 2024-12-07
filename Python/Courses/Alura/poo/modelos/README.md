# Restaurant Evaluation App

This project explores the fundamentals of Object-Oriented Programming (OOP) in Python by building a simple application for managing restaurant evaluations. The app demonstrates the use of classes, methods, and properties to create an organized and extensible structure for a real-world scenario.

## Features
- **Manage Restaurants**: Add restaurants with attributes such as name and category.
- **Activate/Deactivate Restaurants**: Toggle the active status of restaurants.
- **Add Evaluations**: Add customer evaluations with scores.
- **Calculate Average Ratings**: Automatically compute the average score of evaluations.
- **List Restaurants**: Display all registered restaurants with their details, including name, category, status, and average score.

## Project Structure
The project is divided into three main files:
1. **`restaurant.py`**  
   Contains the `Restaurant` class, which handles restaurant information, status, and evaluations.

2. **`evaluation.py`**  
   Defines the `Evaluation` class, which represents individual customer evaluations.

3. **`main_app.py`**  
   Contains the main script to demonstrate the functionality of the application.

## How to Use
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Run the main script:
   ```bash
   python main_app.py
   ```

3. Observe the list of restaurants and their details in the output.

## Example Code
```python
# Creating a new restaurant
restaurant_praca = Restaurant('Praça', 'Gourmet')

# Adding evaluations
restaurant_praca.add_evaluation('John', 5)
restaurant_praca.add_evaluation('Alice', 4)

# Toggling restaurant status
restaurant_praca.restaurant_status()

# Listing all restaurants
Restaurant.list_restaurants()
```

## Requirements
- Python 3.8 or higher

## Concepts Covered
This project introduces and demonstrates:
- Class definitions and constructors (`__init__`)
- Instance attributes and methods
- Class methods (`@classmethod`)
- Properties and getters (`@property`)
- Encapsulation and abstraction in OOP
- Basic validation logic

## Future Improvements
- Add persistence to store restaurant and evaluation data.
- Create a user interface (CLI or GUI) for better interaction.
- Introduce additional features, such as filtering restaurants by category or rating.

## License
This project is for educational purposes and is distributed under the MIT License.
