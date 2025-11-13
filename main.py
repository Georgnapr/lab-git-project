from utils import add_numbers
from config import NAME

def main():
    print(f"Привет, {NAME}!")
    a = 5
    b = 3
    result = add_numbers(a, b)
    print(f"{a} + {b} = {result}")

if __name__ == "__main__":
    main()