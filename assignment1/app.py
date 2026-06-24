import os
import sys

def greet_user(name: str) -> str:
    return f"Hello {name}! Welcome to the app."

def main():
    user_name = os.environ.get("APP_USER")

    if not user_name:
        print("Error: Required environment variable 'APP_USER' is not set.", file=sys.stderr)
        sys.exit(1)

    greeting = greet_user(user_name)
    print(greeting)

    sys.exit(0)

if __name__ == "__main__":
    main()
