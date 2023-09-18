#!/usr/bin/python3
"""
add database storage
"""

from os import getenv


storage_t = getenv("MICHEZO-STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
