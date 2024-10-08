def get(path_to_version: str) -> str:
    """Get a version of an application.

    Returns:
        str: Version of an application.
    """
    with open(f"{path_to_version}/version.txt", "r", encoding="utf-8") as file:
        return file.read()