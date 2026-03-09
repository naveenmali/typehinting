# Basic Types
name: str = "Alice"                        # Line 1
age: int = 25                              # Line 2
height: float = 5.6                        # Line 3
is_student: bool = True                    # Line 4

# Collections
scores: list[int] = [90, 85, 78]          # Line 5
info: dict[str, int] = {"age": 25}        # Line 6
coords: tuple[int, int] = (10, 20)        # Line 7

# Functions
def greet(name: str) -> str:              # Line 8
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:           # Line 9
    return a + b

def log(msg: str) -> None:               # Line 10
    print(msg)

# Optional (value can be None)
from typing import Optional               # Line 11
def find(name: str) -> Optional[str]:    # Line 12
    if name == "Alice":
        return "Found Alice!"
    return None                          

print(greet("Bob"))                       # Hello, Bob!
print(add(3, 4))                          # 7
print(find("Alice"))                      # Found Alice!
print(find("John"))                       # None