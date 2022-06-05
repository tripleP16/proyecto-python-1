from exceptions.invalid_extension_exception import InvalidFileExtensionError


def validate_file_extension(file_name):
    if file_name.split(".")[-1] == "txt":
        return True
    raise InvalidFileExtensionError()
