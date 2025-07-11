import os
def get_file_path(filename):
    """
    Returns the absolute path of the given filename.
    If the file does not exist, returns None.
    """
    file_path = os.path.abspath(filename)
    if os.path.exists(file_path):
        return file_path
    else:
        return None