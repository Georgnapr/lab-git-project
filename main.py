from utils import add_numbers
from config import NAME
from initial_data import A, B
def main():
    print(f"Привет, {NAME}!")
    a = A
    b = B
    result = add_numbers(a, b)
    print(f"{a} + {b} = {result}")

if __name__ == "__main__":
    main()