Preprocessor Folder – Conventions & Rules

This folder (app/preprocessor/) contains all preprocessor functions for the project.
Functions in these files are automatically discovered and registered when the module is imported.

Rules for Writing Preprocessors

Each Python file in this folder should contain only preprocessor functions.

Example: normalize.py, timestamp.py, etc.

File names should be snake_case.

Function requirements:

Must be callable (i.e., a normal Python function).

Must take at least one argument (the data to process).

Do not define private/internal functions (_like_this) in these files — all functions in the file will be automatically registered.

Example Preprocessor File

normalize.py

def normalize_fields(data):
    # modify data fields
    return data

def add_timestamp(data):
    # add timestamp field to data
    return data