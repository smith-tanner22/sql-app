# app.py is for the user

import database

# The menu prompt is how the user will interact with the database
MENU_PROMPT = """
-- Cheese App --

Please choose one of these options:

1) Add a new cheese.
2) See all cheese.
3) Find a cheese by name.
4) See which way to eat cheese is the best.
5) Delete a cheese.
6) Exit.

Your selection: """

# the function menu connects to the database and provides a way for the user to interact with the database
def menu():
    connection = database.connect() # connects to the database
    database.create_tables(connection)

    # basically going to run this statement until the user types 6 (exits the app)
    while (user_input := input(MENU_PROMPT)) != "6":

        if user_input == "1": # if user types 1
            name = input("Enter cheese name: ") # gets the name
            method = input("Enter how you've ate the cheese: ") # gets the method
            rating = int(input("Enter your rating score (0-100): ")) # gets the rating

            database.add_cheese(connection, name, method, rating) # stores this in the database

        elif user_input == "2": # if user types 2
            cheeses = database.get_all_cheeses(connection) # gets all the cheeses so far in the database

            # loops through the table and displays the cheeses
            for cheese in cheeses:
                print(f"{cheese[1]} ({cheese[2]}) - {cheese[3]}/100")

        elif user_input == "3": # if user types 3
            name = input("Enter cheese name to find: ") # gets the name to find
            cheeses = database.get_cheeses_by_name(connection, name) # gets the cheeses from the database

            # loops through the table and displays the cheese that was searched for
            for cheese in cheeses:
                print(f"{cheese[1]} ({cheese[2]}) - {cheese[3]}/100")

        elif user_input == "4": # if user types 4
            name = input("Enter cheese name to find: ") # gets the name to find
            best_method = database.get_best_eat_for_cheese(connection, name) # gets the best method out of the cheeses with the same names

            print(f"The best way to eat for {name} is: {best_method[2]}")

        elif user_input == "5":
            name = input("Enter cheese name to delete: ") # gets the name to find
            database.delete_cheese(connection, name) # deletes the name

            print(f"Deleted {name} from cheeses table.")
            cheeses = database.get_all_cheeses(connection) # gets the updated cheese list

            print("Updated List: ")
            print()
            for cheese in cheeses: # refreshes list without name
                print(f"{cheese[1]} ({cheese[2]}) - {cheese[3]}/100")

        else: # if user tries to type anything else
            print("Invalid input, please try again.")

menu()