from flask import Flask, render_template, request, url_for
from firebase_admin import credentials, firestore, initialize_app, db
from algoliasearch import algoliasearch 
from chatgpt_interaction import ChatgptInteraction
import rating_scraping 

app = Flask(__name__)

chatgpt = ChatgptInteraction()

# Firebase initialization

# Algolia initialization 

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/book/<book_name>')
def book_page(book_name):
    #search for a book in db 
    # if exists, render the information 
    # else ask chat gpt if financial book
    if chatgpt.is_book_financial(book_name):
        category = chatgpt.book_category(book_name)
        description = chatgpt.book_description(book_name)
        rating = rating_scraping.scrape_rating(book_name)
    else:
        return render_template('notfinancialbook.html') #notfinancialbook.html might not be a good name xd 
        # yes - ask additional questions, scrape for rating
        # no - return that we couldn't find such financial related book
    return render_template('book_page.html', book=book_name, rating=rating, category=category, description=description)



if __name__=="__main__":
    app.run()
