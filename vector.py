"""A full implementation of a Vector class with operations."""
from typing import Self

class Vector:
    def __init__(
            self,
            val_list : list[float | int] = [0]
    ):
        self.vector = [float(v) for v in val_list]

    # Vector instance properties
    @property
    def magnitude(self) -> float:
        """Calculate the magnitude of the vector."""
        return sum(x ** 2 for x in self.vector) ** 0.5
    
    @property
    def direction(self) -> Self:
        """Return the direction of the vector as a unit vector."""
        mag = self.magnitude
        if mag == 0:
            return Vector([0] * self.size)
        return Vector([x / mag for x in self.vector])
    
    @property
    def dimension(self) -> int:
        """Return the dimension of the vector. Also accessible as len(v)."""
        return len(self.vector)
    
    # Comparison operations + adjacent methods
    def __eq__(self, other: object) -> bool:
        """Check if two vectors are equal."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.vector == other.vector
    
    def __ne__(self, other: object) -> bool:
        """Check if two vectors are not equal."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.vector != other.vector
    
    __hash__ = None  # Vectors are mutable, so they are not hashable.

    def __lt__(self, other: object) -> bool:
        """Check if this vector's magnitude is less than another vector."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude < other.magnitude
    
    def __le__(self, other: object) -> bool:
        """Check if this vector's magnitude is less than or equal to another vector."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude <= other.magnitude
    
    def __gt__(self, other: object) -> bool:
        """Check if this vector's magnitude is greater than another vector."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude > other.magnitude
    
    def __ge__(self, other: object) -> bool:
        """Check if this vector's magnitude is greater than or equal to another vector."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude >= other.magnitude
    
    # Type conversion methods
    def __repr__(self) -> str:
        """Return a string representation of the vector."""
        return f"Vector({", ".join(str(x) for x in self.vector)})"
    
    def __str__(self) -> str:
        """Return a string representation of the vector for printing."""
        return f"<{', '.join(str(x) for x in self.vector)}>"
    
    def __bool__(self) -> bool:
        """Return True if the vector is non-zero, False otherwise."""
        return any(x != 0 for x in self.vector)
    
    def __int__(self) -> int:
        """Return the integer representation of the vector's magnitude."""
        return int(self.magnitude)
    
    def __float__(self) -> float:
        """Return the float representation of the vector's magnitude."""
        return self.magnitude
    
    __bytes__ = None  # Vectors do not have a byte representation.

    def __complex__(self) -> complex:
        """Return the complex representation of the vector if 2d."""
        if self.dimension != 2:
            raise ValueError("Complex representation is only valid for 2D vectors.")
        return complex(self.vector[0], self.vector[1])
    
    def __format__(self, format_spec: str) -> str:
        """Return a formatted string representation of the vector."""
        return f"<{', '.join(f'{x:{format_spec}}' for x in self.vector)}>"