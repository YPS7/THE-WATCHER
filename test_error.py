#!/usr/bin/env python3
"""
Test Error Generator
This file is used to demonstrate TheWatcher's error detection and fix suggestion capability.
It intentionally contains code that will generate errors.
"""

def divide_numbers(a, b):
    """Divide a by b."""
    print(f"Dividing {a} by {b}...")
    return a / b

def convert_to_int(value):
    """Convert a value to an integer."""
    print(f"Converting {value} to an integer...")
    return int(value)

def list_operation():
    """Perform operations on a list."""
    my_list = [1, 2, 3]
    print(f"Accessing index 5 of {my_list}...")
    return my_list[5]  # Index error

def dict_operation():
    """Perform operations on a dictionary."""
    my_dict = {"a": 1, "b": 2}
    print(f"Accessing key 'c' of {my_dict}...")
    return my_dict["c"]  # Key error

def type_error():
    """Generate a type error."""
    num = 42
    text = "The answer is: "
    print(f"Concatenating '{text}' with {num}...")
    return text + num  # TypeError: can only concatenate str (not "int") to str

def name_error():
    """Generate a name error."""
    print("Accessing undefined variable...")
    return undefined_variable  # NameError: name 'undefined_variable' is not defined

def demo_errors():
    """Demonstrate various errors."""
    print("Starting error demonstrations...")
    
    try:
        # Uncomment one of these to test different error types
        # divide_numbers(5, 0)  # ZeroDivisionError
        # convert_to_int("hello")  # ValueError
        # list_operation()  # IndexError
        # dict_operation()  # KeyError
        type_error()  # TypeError
        # name_error()  # NameError
    except Exception as e:
        print(f"Error caught: {e}")
        # Re-raise to demonstrate TheWatcher
        raise

if __name__ == "__main__":
    print("=== Error Test Program ===")
    print("This program intentionally generates errors to demonstrate TheWatcher.")
    demo_errors() 