from book import generate_book_key, generate_book_title


def test_generate_book_title():
    output = generate_book_title('here is  the   test title')
    assert output == "Here Is The Test Title"


def test_generate_book_key():
    output = generate_book_key('here is   the test title')
    assert output == "hereisthetesttitle"