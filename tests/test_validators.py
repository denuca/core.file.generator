from core.validators import validate_text_input, validate_file_upload

def test_validate_text_input():
    valid, error = validate_text_input("This is a test")
    assert valid
    assert error is None

    valid, error = validate_text_input("")
    assert not valid
    assert error == "Text input cannot be empty."

# Similar tests for file upload validation can be added
