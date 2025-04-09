"""
File I/O Utility Program

This program provides two main features:
1. Count the number of words and lines in a text file.
2. Create and save a CSV file from user-provided data.

Dependencies:
- help_info.txt (for CSV help command)

Author: SlightlyOffset

Version: 1.01
"""

import os
import csv
from string import Template

def main():
    def CountWL():
        '''
        Counts the number of words and lines in a text file.

        The function prompts the user for the full path to a text file and then calculates
        and displays the word count and line count.

        Input:
            - User provides the full file path via input().

        Output:
            - Prints the word count and line count to the console.

        Error Handling:
            - Invalid file extension: Displays an error message if the file is not a .txt file.
            - FileNotFoundError: Handles cases where the specified file does not exist.
            - PermissionError: Handles cases where the program lacks permission to access the file.
            - UnicodeDecodeError: Handles cases where the file cannot be decoded using utf8.
        '''
        print("\nWords and lines counter.")
        
        while True:
            print("\nEnter 'stop' to exit")
            file_path = input("Enter full path to text file: ")
            
            if file_path.lower().strip() == "stop":
                print("\nStopping...")
                break
            
            if file_path.endswith(".txt"):
                try:
                    with open(file_path, 'r', encoding="utf8") as file:
                        content = file.read()       # File cursor at EOF
                        word_count = len(content.split())
                        file.seek(0)        # Reset file cursor to start
                        line_count = 0
                        for line_count, line in enumerate(file, 1):
                            pass
                        
                        print(f"\nWord count: {word_count} {'word' if word_count == 1 else 'words'}\nLine count: {line_count} {'line' if line_count == 1 else 'lines'}")
                        
                except FileNotFoundError:
                    print("\nError: File not exist.")
                    
                except PermissionError:
                    print("\nError: Access denied.")
                    
                except UnicodeDecodeError:
                    print("\nError: Unable to decode the file correctly. Ensure that the file is encoded in utf8 and try again.")
                    
            else:
                print("\nError: Provided file is not in txt extension. Try again.")
            
    def MakeCSV():
        '''
        Creates a CSV file from user-provided data.

        This function allows the user to specify the number of columns and rows for a CSV file,
        enter data into the file using a command-line-like interface, and then save the data
        to a CSV file.

        Input:
            - User inputs the number of columns and rows.
            - User enters data using commands like 'c1r1 Hello!'.
            - User uses commands like 'save', 'clear', 'help', and 'kill'.

        Output:
            - Creates a CSV file with the user-specified data.
            - Prints messages to the console based on user commands and errors.

        Error Handling:
            - ValueError: Handles invalid input for column and row numbers.
            - ValueError, IndexError: Handles invalid position input.
            - Exception: Handles errors during file saving.
        '''
        def help():
            '''
            Displays help information to the user.

            Reads help information from 'help_info.txt' and displays it based on the user's choice.

            Input:
                - User selects a help topic by entering a number.

            Output:
                - Prints the selected help topic to the console.

            Error Handling:
                - FileNotFoundError: Handles cases where 'help_info.txt' is not found.
                - UnicodeDecodeError: Handles cases where 'help_info.txt' cannot be decoded using utf8.
            '''
            try:
                with open("help_info.txt", "r", encoding="utf8") as file:
                    help_content = file.read()
            except FileNotFoundError:
                print("Error: help_info.txt not found.")
                return
            except UnicodeDecodeError:
                print("Error: Unable to decode help_info.txt correctly. help_info.txt not encoded in utf8.")
                return

            help_map = {}
            help_blocks = help_content.split("\n\n")  # Help topics are separated by double newlines

            for block in help_blocks:
                lines = block.split("\n")
                if len(lines) >= 2:
                    key = lines[0].strip()
                    help_map[key] = "\n".join(lines[1:])

            print("What do you need help with?")
            for key, value in help_map.items():
                print(f"{key}. {value.splitlines()[0]}") #print the first line of the value only.
            print(f"{len(help_map)+1}. Nothing.")

            while True:
                try:
                    choice = int(input("Enter the topic number: "))
                    if 1 <= choice <= len(help_map):
                        key = str(choice)
                        print("\n" + help_map[key] + "\n")
                        break
                    elif choice == len(help_map) + 1:
                        print("\nExiting help...")
                        break
                    else:
                        print("Invalid choice. Please enter a valid topic number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            input("Press 'Enter' to continue...")
            
        data_list = []
        
        print("\nMake a CSV from list.")
        
        while True:
            try:
                print("\nHow many columns do you need?")
                columns = int(input("Enter here: "))
                print("\nHow many rows do you need?")
                rows = int(input("Enter here: "))
                break
                
            except ValueError:
                print("Error: Accept integer value only.")
                
        # Initial list setup by user input
        data_list = [["" for _ in range(columns)] for _ in range(rows)]
        
        print("To enter data specify position in column and row\nlike c1r1 to access column 1, row 1.")
        print("Then separate with space and enter data.")
        print("Example: c1r1 Hello!\n")
        print("Type 'kill' to terminate the program.")
        print("Type 'save' to save CSV file.")
        print("Type 'help' if needed.")
        
        while True:
            '''
            The loop print out the list for the user to interact with.
            '''
            for row in data_list:
                print("|".join(f"{cell:10}" for cell in row))
        
            command = input("\nCommand: ")
            
            match command.strip().lower():
                case "help":
                    help()
                
                case "save":
                    '''
                    This block will save the data into csv file with name from user.
                    '''
                    filename = input("\nEnter file name to save as CSV: ")
                    template = Template(f"{filename}$format")
                    try:
                        with open(template.substitute(format=".csv"), "w", newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerows(data_list)
                        print(f"\nFile saved as {template.substitute(format='.csv')}")
                        break
                        
                    except Exception as e:
                        print(f"\nError: Cannot save {template.substitute(format='.csv')} as {e}\n")
                        break
                
                case "clear":
                    data_list.clear()
                    data_list = [["" for _ in range(columns)] for _ in range(rows)]
                    
                case "kill":
                    print("\nKilling the process...")
                    print("\nReturning to menu...")
                    return
                
                case _:
                    try:
                        position, data = command.split(" ", 1)
                        col_row = position.lower().strip()
                        col = int(col_row[1:col_row.find("r")]) - 1
                        row = int(col_row[col_row.find("r") + 1:]) - 1
                        
                        if 0 <= col < columns and 0 <= row < rows:
                            data_list[row][col] = data
                        else:
                            print("\nError: Invalid position input.\n")
                            
                    except ValueError:
                        print("\nError: Invalid command input.\n")
                    except IndexError:
                        print("\nError: Invalid position input.\n")
                
    """
    Display the main menu for the File I/O utility.

    Allows the user to choose between counting words/lines in a file or
    creating a CSV file. Exits the program on request.
    """
    def menu():
        ops_map = {
        "1" : CountWL,
        "2" : MakeCSV
        }
        
        print("This is a file IO program. You either...")
        while True:
            print("\nMenu:\n1. Count number of words and line in a file.\n2. Make a CSV from list.\n3. Exit")
            operation = input("Enter here(number): ")
            
            if operation.strip().lower() == "3":
                print("\nExiting...")
                return
                
            if operation.strip().lower() not in ops_map:
                print("\nError: Non-existing operation.")
                
            else:    
                ops_map[operation.strip().lower()]()
                
    menu()
    
if __name__ == "__main__":
    main()