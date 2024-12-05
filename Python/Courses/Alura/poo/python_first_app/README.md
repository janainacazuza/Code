
# Python Beginner's Course: Restaurant Management Application

This project was developed as part of an introductory Python course to teach basic programming concepts. It implements a simple terminal application to manage restaurants, covering topics such as list and dictionary manipulation, code structuring with functions, and control flow.

## 🚀 Features

- **Register restaurants**: Add new restaurants to the system with a name and category.
- **List restaurants**: View all registered restaurants with their respective status (active/inactive).
- **Change status**: Update a restaurant's status to "active" or "inactive."
- **Close application**: Exit the program in a controlled manner.

---

## 🛠️ Technologies Used

- **Python 3.x**
- Python standard libraries:
  - `os`: to clear the terminal.

---

## 📖 What I Learned

This project helped me practice:

1. **List and dictionary manipulation** to store and process data.
2. **Using functions** to organize code and improve reusability.
3. **Control flow** with conditionals (`if/else`) and loops (`for`).
4. **Exception handling** to capture errors during program execution.
5. Initial practices in **terminal interface design**.

---

## 📋 How to Use

1. Ensure you have **Python 3.x** installed on your computer.
2. Clone this repository:

   ```bash
   git clone https://github.com/janainacazuza/python-beginner-course.git
   ```

3. Navigate to the project directory:

   ```bash
   cd python-beginner-course
   ```

4. Run the program:

   ```bash
   python main.py
   ```

---

## ⚙️ Features in Detail

### Main Menu

The program presents a menu with four options:

1. **Register a restaurant**: Allows you to add a restaurant with its name and category.
2. **List restaurants**: Displays a table of all restaurants, their categories, and statuses.
3. **Change restaurant status**: Activates or deactivates an existing restaurant.
4. **Close application**: Ends the program.

---

## 📝 Code Structure

The code is organized into functions to improve readability and maintainability. Here is an overview of the main functions:

| Function                | Description                                                                 |
|-------------------------|---------------------------------------------------------------------------|
| `show_name()`           | Displays the application's name in the terminal.                         |
| `show_menu()`           | Shows the application's main menu.                                       |
| `register_restaurant()` | Allows the registration of a new restaurant.                             |
| `list_restaurants()`    | Lists all registered restaurants with their name, category, and status.  |
| `restaurant_status()`   | Changes the status (active/inactive) of an existing restaurant.          |
| `close_app()`           | Closes the application with a farewell message.                         |
| `choose_option()`       | Reads and executes the user's selected option from the main menu.        |
| `main()`                | Main function that coordinates the program's flow.                      |

---

## 🛑 Possible Future Improvements

- Add data persistence (save restaurants to a file).
- Implement more robust input validations.
- Improve the interface with colors and a more organized layout.

---

## 📄 License

This project is free to use and modify. Feel free to use it as a base for your studies or projects.

---

## 👩‍💻 Contact

If you have any questions or suggestions, feel free to reach out:

- **Email**: <janainamartinscazuza@gmail.com>
- **GitHub**: [janainacazuza](https://github.com/janainacazuza)
