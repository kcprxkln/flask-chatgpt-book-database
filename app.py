from flask import Flask, render_template, request, url_for
import firebase_admin
from firebase_admin import credentials, firestore    
from algoliasearch.search_client import SearchClient
from chatgpt_interaction import ChatgptInteraction
from book import generate_book_title, generate_book_key
import rating_scraping 
import os

app = Flask(__name__)

chatgpt = ChatgptInteraction()

# Firebase initialization
cred_obj = firebase_admin.credentials.Certificate('') #actual path to the firebase key
firebase_admin.initialize_app(cred_obj)

db = firestore.client()

# Algolia initialization 
# client = SearchClient.create('my app id', os.getenv('algolia_apikey'))
# index = client.init_index('indexname')

@app.route('/')
def home():
    return render_template('home.html')

#enpoint to testing how book not found web frontend look like
@app.route('/bnf') 
def bnf():
    return render_template('book_not_found.html')

@app.route('/book', methods=['GET'])
def book_page():
    book_title = request.args.get('book_name')
    #search for a book in db '
    key = generate_book_key(book_title)

    # if exists, render the information 
    query = db.collection('financial-books').where("key", '==', key)
    results = query.get()

    if results:
        for doc in results:
            data = doc.to_dict()
            rating = data['rating']
            description = data['description']
            category = data['category']
            title = data['title']

    else: # else ask chat gpt if financial book
        try:
            if chatgpt.is_book_financial(book_title):
                category = chatgpt.book_category(book_title)
                description = chatgpt.book_description(book_title)
                rating = rating_scraping.scrape_rating(book_title)
                title = generate_book_title(book_title)
                book_object = {
                    "key" : key, 
                    "title" : title,
                    "description" : description,
                    "rating" : rating, 
                    "category" : category
                }
                db.collection('financial-books').add(book_object)    # add new book to the db 
            else:
                return render_template('book_not_found.html')  
        
        except:
                return render_template('integration_problem.html')

    return render_template('book_page.html', book=title, rating=rating, category=category, description=description)



if __name__=="__main__":
    app.run()
