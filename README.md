# Mathematical Vectors Library

A Python library implementing a fully-featured mathematical vector class using Python's dunder (magic) methods. This library is designed for intuitive and Pythonic manipulation of vectors, supporting comparison, arithmetic, type conversion, and more.

## Features

- Vector creation from lists of numbers
- Magnitude and direction (unit vector) calculation
- Dimension property
- Equality and comparison operations (`==`, `<`, `>`, etc.)
- Arithmetic operations (`+`, `-`, `*`, unary `-`, unary `+`)
- Dot product (`**`) and cross product (`@`)
- In-place arithmetic (`+=`, `-=`, `*=`)
- Type conversions (`int`, `float`, `complex`, `str`, `repr`)
- Truthiness checks
- Formatted string output
- Container methods (`len`, iteration, indexing, assignment)
- Error handling for unsupported operations

## Example Usage

Example usage and feature demonstrations are included in the test suite (`testing/vector_tests.py`).  
To see all features in action, run the tests with:

```bash
pytest testing/vector_tests.py
```

## Running the Example

The `main.py` file is currently a placeholder for future CLI and state management tools.

## Future Plans

- Provide a CLI interface for vector operations via command line
- Explore more class functionality to make this a proper class ie. custom exceptions.
print(f"<0, 0> is truthy: {bool(Vector([0, 0]))}")  # False
print(f"Vector 1 as string: {str(v1)}")       # <1.0, 2.0, 3.0>
print(f"Vector 2 as repr: {repr(v2)}")        # Vector(4.0, 5.0, 6.0)
print(f"Vector 1 format 2f: {v1:.2f}")        # <1.00, 2.00, 3.00>
print(f"v1 + v2: {v1 + v2}")                  # <5.0, 7.0, 9.0>
print(f"v1 - v2: {v1 - v2}")                  # <-3.0, -3.0, -3.0>
print(f"v1 * 2: {v1 * 2}")                    # <2.0, 4.0, 6.0>
print(f"v1 ** v2 (dot product): {v1 ** v2}")  # 32.0
print(f"v1 @ v2 (cross product): {v1 @ v2}")  # <-3.0, 6.0, -3.0>
print(f"-v1: {-v1}")                          # <-1.0, -2.0, -3.0>
print(f"+v1: {+v1}")                          # <1.0, 2.0, 3.0>
```

## Running the Example

Run the included `main.py` to see the vector class in action and test all features:

```bash
python main.py
```

## Future Plans

- Provide a CLI interface for vector operations via command line
- Explore more class functionality to make this a proper class ie. custom exceptions.
