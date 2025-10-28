#task 1

def caching_fibonacci():
    cache = {}

    def fibonacci(n: int) -> int:
        """Recursively computes the n-th Fibonacci number with caching"""
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))  
print(fib(15))  
print(fib(20))  

#task 2
import re
from typing import Callable

def generator_numbers(text: str):
    """
    Generator function that yields all real numbers in the text.
    Assumes numbers are separated by spaces.
    """
    pattern = r'\b\d+\.\d+|\b\d+\b'
    
    for match in re.findall(pattern, text):
        yield float(match)

def sum_profit(text: str, func: Callable):
    """
    Calculates the total sum of numbers in the text using the provided generator function.
    """
    total = sum(func(text))
    return total

text = ("The total income of the employee consists of several parts: "
        "1000.01 as base salary, supplemented by additional revenue 27.45 and 324.00 dollars.")

total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")

#task 4
contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Please provide all required arguments."
    return inner

@input_error
def add_contact(args, contacts):
    """Add a contact to the contacts dictionary."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    """Return the phone number for the given contact."""
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def show_all(contacts):
    """Return all contacts as formatted string."""
    if not contacts:
        return "No contacts yet."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def handler(command_line):
    parts = command_line.split()
    command = parts[0].lower()
    args = parts[1:]
    
    if command == "add":
        return add_contact(args, contacts)
    elif command == "phone":
        return get_phone(args, contacts)
    elif command == "all":
        return show_all(contacts)
    elif command in ["exit", "close", "goodbye"]:
        return "Goodbye!"
    else:
        return "Unknown command."

def main():
    while True:
        command_line = input("Enter a command: ")
        result = handler(command_line)
        print(result)
        if result == "Goodbye!":
            break

if __name__ == "__main__":
    main()


