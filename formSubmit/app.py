from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    raise Exception("MONGO_URI Issue.")

client = MongoClient(mongo_uri)
db = client['mydatabase']
collection = db['formdata']

@app.route('/', methods=['GET', 'POST'])
def form():
    error_message = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        try:
            if not name or not email:
                raise ValueError("Name and Email are required")

            collection.insert_one({
                "name": name,
                "email": email
            })
            return redirect(url_for('success'))

        except (ValueError, PyMongoError) as e:
            error_message = str(e)

    return render_template('form.html', error=error_message)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
