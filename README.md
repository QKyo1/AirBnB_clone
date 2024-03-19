# AirBnB Clone Command Interpreter

## Description

This project is part of building an AirBnB clone. The first step involves creating a command interpreter to manage AirBnB objects. This command interpreter will serve as the backbone for future development, including HTML/CSS templating, database storage, API integration, and front-end development.

## Command Interpreter

The command interpreter allows users to interact with AirBnB objects through a command-line interface. It provides functionalities for creating, updating, deleting, and querying various objects such as users, states, cities, places, etc.

### How to Start

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the command `./console.py` to start the command interpreter.

### How to Use

Once the command interpreter is running, you can use the following commands:

- `create <class_name>`: Create a new instance of the specified class.
- `show <class_name> <id>`: Show details of a specific instance.
- `update <class_name> <id> <attribute_name> "<new_value>"`: Update an attribute of a specific instance.
- `destroy <class_name> <id>`: Delete a specific instance.
- `all <class_name>`: Show all instances of a specific class or all classes.
- `quit` or `EOF`: Exit the command interpreter.

### Examples

Here are some examples of how to use the command interpreter:

1. Create a new user:
   ```
   (hbnb) create User
   ```

2. Show details of a user:
   ```
   (hbnb) show User 123
   ```

3. Update a user's email:
   ```
   (hbnb) update User 123 email "newemail@example.com"
   ```

4. Delete a user:
   ```
   (hbnb) destroy User 123
   ```

5. Show all instances of a class:
   ```
   (hbnb) all User
   ```

6. Exit the command interpreter:
   ```
   (hbnb) quit
   ```

Feel free to explore more commands and functionalities within the command interpreter for managing AirBnB objects efficiently.

For more details on the AirBnB concept and project structure, please refer to the AirBnB concept page.