from app import greet_user

def test_greet_user_success():
    input_name = "John"
    expected_output = "Hello John! Welcome to the app."

    actual_output = greet_user(input_name)

    assert actual_output == expected_output

def test_greet_user_different_name():
    assert greet_user("DevOps-Bot") == "Hello DevOps-Bot! Welcome to the app."
