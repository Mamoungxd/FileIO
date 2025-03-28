
# File I/O Utility

A Python program that provides two simple file-related utilities:
1. Count the number of words and lines in a text file.
2. Create and save a CSV file from user-provided data.

## Features

- **Word & Line Counter:**  
  Reads any `.txt` file and counts the number of words and lines.

- **CSV File Creator:**  
  Allows the user to enter custom data and save it as a `.csv` file interactively.

- **Help System:**  
  Provides help topics from a `help_info.txt` file.

## Requirements

- Python 3.x

## How to Use

1. **Run the program:**
    ```bash
    python File_IO.py
    ```

2. **Choose an option from the menu:**
    - `1` to count words and lines in a `.txt` file.
    - `2` to create a CSV file.
    - `3` to exit.

3. **For CSV creation, commands include:**
    - `c<column>r<row> <data>` → to insert data.
    - `save` → to save the CSV file.
    - `clear` → to clear all data.
    - `kill` → to terminate and return to the menu.
    - `help` → to access help topics from `help_info.txt`.

## Notes

- Ensure `help_info.txt` is in the same directory if you intend to use the help command in CSV creator.
- File encoding expected: `utf8`
