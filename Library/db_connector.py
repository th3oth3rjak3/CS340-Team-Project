"""
This module houses database credentials and separates them from the main app.

"""

def get_db_creds() -> dict:
    """Returns database credentials to the app."""

    keys = {
        "Host": "classmysql.engr.oregonstate.edu",
        "User": "cs340_USERNAME",
        "Password": "ONID",
        "Database": "cs340_USERNAME",
        "Cursor Class": "DictCursor",
        "Session Type": "filesystem",
        "Secret Key": "super secret key",
        "Templates Auto Reload": True
        }

    return keys
