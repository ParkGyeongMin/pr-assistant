def get_language_from_filename(filename):
    EXTENSION_MAP = {
        'py' : 'python',
        'js' : 'javascript',
        'java' : 'java',
        'kt' : 'kotlin'
    }

    extension = filename.split('.')[-1] if '.' in filename else ''
    return EXTENSION_MAP.get(extension.lower(), 'python')