# General Python Rules — Quick Reference

This document gives a concise overview of common Python concepts and best practices useful for beginners and as a quick reminder for experienced developers.

## Basics
- Python is dynamically typed and uses indentation to define blocks.
- Use meaningful variable names and keep code readable.

## Variables & Types
- Common built-in types: `int`, `float`, `str`, `bool`, `NoneType`.
- Assignments:

```python
x = 10
name = "Alice"
pi = 3.14
flag = True
```
- Use `is` for identity checks with singletons (e.g., `x is None`), `==` for equality.

## Collections
- List: ordered, mutable, allows duplicates.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
```

- Tuple: ordered, immutable.

```python
coords = (10, 20)
```

- Dict: key-value mapping, keys must be hashable.

```python
person = {"name": "Alice", "age": 30}
```

- Set: unordered, unique elements.

```python
uniq = {1, 2, 3}
```

## Control Flow
- `if` / `elif` / `else` for branching.
- `for` loops iterate over iterables; prefer `for item in iterable:`.
- `while` for loops with a condition; avoid infinite loops.
- Use comprehensions for concise mapping/filtering:

```python
squares = [x*x for x in range(10) if x % 2 == 0]
```

## Functions
- Define with `def`; prefer clear names and small responsibilities.
- Use default args, `*args`, `**kwargs` when appropriate.
- Document with docstrings (triple-quoted string under the def).

```python
def greet(name: str) -> str:
    """Return a greeting for name."""
    return f"Hello, {name}!"
```

## Classes & OOP
- Use classes for modeling state and behavior.
- `__init__` is the constructor; prefer composition over deep inheritance.
- Keep methods focused and use dunder methods sparingly.

```python
class Counter:
    def __init__(self, start=0):
        self.count = start
    def increment(self):
        self.count += 1
```

## Modules & Packages
- One module = one .py file. Group related modules into packages (folders with `__init__.py`).
- Avoid circular imports; import at function scope if necessary.

## Exceptions & Error Handling
- Use exceptions for error cases, not for flow control.
- Create specific exception types when needed.

```python
try:
    value = int(user_input)
except ValueError:
    print("Please enter a valid integer")
```

## File I/O
- Use context managers to guarantee resource cleanup.

```python
with open('data.txt', 'r', encoding='utf-8') as f:
    text = f.read()
```

## Virtual Environments & Dependencies
- Use `venv` or `virtualenv` to isolate dependencies.
- List dependencies in `requirements.txt` or `pyproject.toml`.

## Type Hints
- Use typing for clarity and better tooling support: `def fn(x: int) -> str:`
- Type hints are optional but recommended for larger codebases.

## Style & Best Practices
- Follow PEP 8: 4-space indentation, max ~79-99 chars per line, descriptive names.
- Write docstrings and small tests for important functions.
- Keep functions short and focused (single responsibility).

## Common Pitfalls
- Mutable default arguments: avoid `def f(items=[]):` — use `None` then set inside.
- Modifying a list while iterating over it can cause unexpected behavior.
- Relying on insertion order of dicts only when explicitly intended (modern Python preserves insertion order but don't depend on it for logic unless appropriate).

## Quick Examples
- Swap values: `a, b = b, a`
- Iterate with index: `for i, v in enumerate(items):`
- Join strings: `', '.join(list_of_strings)`

---

Keep this file as a short reference. For deeper learning, consult the official Python docs at https://docs.python.org/3/ and PEPs for style and language details.
