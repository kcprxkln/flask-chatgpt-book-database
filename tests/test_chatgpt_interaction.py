from chatgpt_interaction import ChatgptInteraction

category_length = [7, 16, 31, 29, 28, 32, 32, 19, 35, 30, 18]


interaction = ChatgptInteraction()

def test_chatgpt_api_cond():
    output = interaction.is_book_financial("placeholder")
    assert isinstance(output, str)

def test_is_book_financial():
    output = interaction.is_book_financial("Rich dad poor dad")
    assert output == "yes"


def test_book_description():
    output = interaction.book_description("Rich dad poor dad")
    assert isinstance(output, str) and len(output) > 10


def test_book_category():
    output = interaction.book_category("Rich dad poor dad")
    assert isinstance(output, str) and len(output) in category_length 
