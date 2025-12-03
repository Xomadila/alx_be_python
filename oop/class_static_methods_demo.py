# oop/class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: performs addition.
        Does not depend on class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: performs multiplication.
        Has access to class attributes via 'cls'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b