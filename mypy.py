pip install mypy

# CORRECT code
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"

# INTENTIONAL ERRORS for mypy to catch
result = add("hello", 2)        # ❌ passing str instead of int
greeting = greet(123)           # ❌ passing int instead of str

age: int = "twenty five"        # ❌ assigning str to int variable


mypy type_check.py
```

---

**Output you'll see:**
```
type_check.py:9: error: Argument 1 to "add" has incompatible type "str"; expected "int"  [arg-type]
type_check.py:10: error: Argument 1 to "greet" has incompatible type "int"; expected "str"  [arg-type]
type_check.py:12: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
Found 3 errors in 1 file (checked 1 source file)

# FIXED code
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"

result = add(3, 2)              # ✅ correct
greeting = greet("Alice")       # ✅ correct

age: int = 25                   # ✅ correct

mypy type_check.py
# Output: Success: no issues found in 1 source file