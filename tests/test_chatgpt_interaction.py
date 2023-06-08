from chatgpt_interaction import ChatgptInteraction, categories
import openai
import os

openai.api_key = os.getenv("openai_apikey")

category_length = [len(category) for category in categories]


interaction = ChatgptInteraction()


def test_is_book_financial():
    output = interaction.is_book_financial("Rich dad poor dad")
    assert output == "yes"


def test_book_description():
    output = interaction.book_description("Rich dad poor dad")
    assert isinstance(output, str) and len(output) > 10


def test_book_category():
    output = interaction.book_category("Rich dad poor dad")
    output_no_dot = output.strip(".") #chatgpt returns the sentence with "." at the end
    assert isinstance(output, str) and len(output_no_dot) in category_length 
