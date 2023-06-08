from flask import Flask, render_template, request, url_for
# from firebase_admin import credentials, firestore, initialize_app, db
from algoliasearch.search_client import SearchClient
from chatgpt_interaction import ChatgptInteraction
import rating_scraping 
import os

app = Flask(__name__)

chatgpt = ChatgptInteraction()

# Firebase initialization

# Algolia initialization 
# client = SearchClient.create('my app id', os.getenv('algolia_apikey'))
# index = client.init_index('indexname')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bnf') #enpoint to testing how book not found web frontend look like
def bnf():
    return render_template('book_not_found.html')


@app.route('/book', methods=['GET'])
def book_page():
    book_title = request.args.get('book_name')
    show_book_title = book_title.title()
    #search for a book in db 
    # if exists, render the information 
    # else ask chat gpt if financial book
    try:
        if chatgpt.is_book_financial(book_title):
            category = chatgpt.book_category(book_title)
            description = chatgpt.book_description(book_title)
            rating = rating_scraping.scrape_rating(book_title)
        else:
            return render_template('book_not_found.html') #notfinancialbook.html might not be a good name xd     
    
    except:
            return render_template('integration_problem.html')
        # yes - ask additional questions, scrape for rating
        # no - return that we couldn't find such financial related book
    return render_template('book_page.html', book=show_book_title, rating=rating, category=category, description=description)



if __name__=="__main__":
    app.run()
