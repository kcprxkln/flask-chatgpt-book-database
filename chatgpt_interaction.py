import openai 
import os 

categories = [
    "Personal Finance",
    "Investing and Wealth Management",
    "Business and Entrepreneurship",
    "Economics and Finance Theory",
    "Financial Education and Literacy",
    "Personal Development and Success",
    "Retirement Planning",
    "Real Estate and Property Investment",
    "Financial Technology (Fintech)",
    "Behavioral Finance"
]

openai.api_key = os.getenv("openai_apikey")

class ChatgptInteraction():
    def __init__(self):
        self.model = "gpt-3.5-turbo"

    def is_book_financial(self, title):
        prompt = openai.ChatCompletion.create(
            model=self.model, 
            messages=[{"role": "user", "content": f"Is the {title} financial book? If yes response yes, if it's not response no"}]
        )
        answer = prompt.choices[0].message.content

        if answer.lower() == "no":
            return False
        else:
            return True
        
    def book_description(self, title):
        prompt = openai.ChatCompletion.create(
            model=self.model, 
            messages=[{"role": "user", "content": f"provide me essence of book {title} in 10 sentences. Format it just normal description, not a list of points."}]
        )
        description = prompt.choices[0].message.content 

        return description
    
    def book_category(self, title):
        prompt = openai.ChatCompletion.create(
            model=self.model, 
            messages=[{"role": "user", "content": f"In which category would you place the \"{title}\" book?Personal Finance, Investing and Wealth Management, Business and Entrepreneurship, Economics and Finance Theory, Financial Education and Literacy, Personal Development and Success, Retirement Planning, Real Estate and Property Investment, Financial Technology (Fintech), Behavioral Finance. Answer only with name of category"}]
        )
        category =  prompt.choices[0].message.content
        print(category)

        for c in categories:
            if c.lower() in category.lower():
                return category
        
        else:
            return "unknown"