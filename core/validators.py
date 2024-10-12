def validate_text_input(text):
    """
    Validate text input for the file generator.
    :param text: String of text provided by the user.
    :return: Tuple (is_valid, error_message) where is_valid is a boolean.
    """
    if not text:
        return False, "Text input cannot be empty."
    # Additional validation logic as needed
    return True, None

def validate_file_upload(file):
    """
    Validate file upload (e.g., ensure correct format, size limits).
    :param file: File object uploaded by the user.
    :return: Tuple (is_valid, error_message) where is_valid is a boolean.
    """
    if not file:
        return False, "No file was uploaded."
    # Additional file validation logic
    return True, None
