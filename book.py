def generate_book_title(title: str):
    x = title.split()
    final_title = ' '.join(x).title()
    return final_title


def generate_book_key(title: str):
    x = title.split()
    key = ''.join(x).lower()
    return key