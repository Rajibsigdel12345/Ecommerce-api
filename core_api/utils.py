from django.core.exceptions import ValidationError


def get_extension() -> list:
    return ['.jpeg', '.png', '.jpg', '.gif', '.webp']


def image_validation(value):
    import os
    valid_extensions = get_extension()
    ext = os.path.splitext(value.name)[1]
    print(ext)
    if ext.lower() not in valid_extensions:
        raise ValidationError("Not a valid file type")
