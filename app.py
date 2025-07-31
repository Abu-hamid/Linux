from flask import Flask, render_template, request, redirect, url_for, jsonify
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

# Route for To-Do page with form
@app.route('/todo', methods=['GET', 'POST'])
def todo():
    error_message = None
    success_message = None
    todo_items = []
    
    # Handle form submission
    if request.method == 'POST':
        item_name = request.form.get('itemName')
        item_description = request.form.get('itemDescription')
        
        try:
            if not item_name or not item_description:
                raise ValueError("Both Item Name and Item Description are required")

            # Store in MongoDB
            collection.insert_one({
                "itemName": item_name,
                "itemDescription": item_description
            })
            
            success_message = "To-Do item added successfully!"
            
        except (ValueError, PyMongoError) as e:
            error_message = str(e)
    
    # Get all todo items from database
    try:
        todo_items = list(collection.find({"itemName": {"$exists": True}}, {"_id": 0}))
    except PyMongoError as e:
        error_message = f"Error loading todo items: {str(e)}"
    
    return render_template('todo.html', 
                         error=error_message, 
                         success=success_message, 
                         todo_items=todo_items)

# Route for /api/todoitem that shows a form
@app.route('/api/todoitem', methods=['GET', 'POST'])
def todo_item_form():
    error_message = None
    success_message = None
    
    if request.method == 'POST':
        item_name = request.form.get('itemName')
        item_description = request.form.get('itemDescription')
        
        try:
            if not item_name or not item_description:
                raise ValueError("Both Item Name and Item Description are required")

            # Store in MongoDB
            collection.insert_one({
                "itemName": item_name,
                "itemDescription": item_description
            })
            
            success_message = "To-Do item added successfully!"
            
        except (ValueError, PyMongoError) as e:
            error_message = str(e)
    
    return render_template('todo.html', 
                         error=error_message, 
                         success=success_message, 
                         todo_items=[])

# API endpoint for JSON submissions
@app.route('/api/todoitem/json', methods=['POST'])
def api_submit_todo_item():
    try:
        data = request.get_json()
        item_name = data.get('itemName')
        item_description = data.get('itemDescription')

        if not item_name or not item_description:
            return jsonify({"success": False, "error": "Both itemName and itemDescription are required."}), 400

        collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_description
        })

        return jsonify({"success": True, "message": "To-Do item saved successfully."}), 201

    except (PyMongoError, Exception) as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ✅ New GET route to list all items
@app.route('/api/todoitems', methods=['GET'])
def get_all_todo_items():
    try:
        items = list(collection.find({}, {"_id": 0}))
        return jsonify({"success": True, "items": items}), 200
    except PyMongoError as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
