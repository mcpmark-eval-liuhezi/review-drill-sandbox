"""A tiny calculator used for the onboarding review drill."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return b - a


def main():
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))


if __name__ == "__main__":
    main
