# To-Do Application

This is a Flask-based To-Do application with a modern frontend and MongoDB backend.

## Features

### Frontend (master_1 branch)
- Beautiful, responsive To-Do page with modern UI
- Form with Item Name and Item Description fields
- Real-time display of existing To-Do items
- Client-side validation and error handling

### Backend (master_2 branch)
- `/submittodoitem` POST endpoint for submitting new To-Do items
- MongoDB integration for data persistence
- `/api/todoitems` GET endpoint for retrieving all To-Do items
- Error handling and validation

## Routes

- `/` - Main form page
- `/todo` - To-Do application page
- `/success` - Success page
- `/submittodoitem` - POST endpoint for submitting To-Do items
- `/api/todoitems` - GET endpoint for retrieving all To-Do items

## Setup

1. Install dependencies:
```bash
pip install flask pymongo python-dotenv
```

2. Set up environment variables:
Create a `.env` file with:
```
MONGO_URI=your_mongodb_connection_string
```

3. Run the application:
```bash
python app.py
```

4. Access the To-Do application at: `http://localhost:5000/todo`

## Branch Structure

- **master_1**: Frontend implementation with To-Do page
- **master_2**: Backend implementation with `/submittodoitem` route
- **main**: Merged version with both frontend and backend

## API Endpoints

### POST /submittodoitem
Submit a new To-Do item.

**Request Body:**
```json
{
    "itemName": "Task name",
    "itemDescription": "Task description"
}
```

**Response:**
```json
{
    "success": true,
    "message": "To-Do item saved successfully."
}
```

### GET /api/todoitems
Retrieve all To-Do items.

**Response:**
```json
{
    "success": true,
    "items": [
        {
            "itemName": "Task 1",
            "itemDescription": "Description 1"
        },
        {
            "itemName": "Task 2", 
            "itemDescription": "Description 2"
        }
    ]
}
``` 