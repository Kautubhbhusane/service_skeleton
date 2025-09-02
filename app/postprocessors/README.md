Postprocessor Folder – Conventions & Rules

This folder (app/postprocessor/) contains all postprocessor functions for the project.
Functions in these files are automatically discovered and registered when the module is imported.

Rules for Writing Postprocessor

Each Python file in this folder should contain only postprocessor functions.

Example: postprocessor_new.py, meta_postprocessor.py, etc.

File names should be snake_case.

Function requirements:

Must be callable (i.e., a normal Python function).

Must take at least one argument (the data to process).

Do not define private/internal functions (_like_this) in these files — all functions in the file will be automatically registered.

Example Preprocessor File

postprocessor.py

def postprocessor_new(data):
    # modify data fields
    return data

def meta_postprocessor(data):
    # modify data fields
    return data