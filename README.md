Book API - README
This project is a RESTful API for managing a collection of books, built using Flask and Flask-Limiter to control request rates. The API supports retrieving books with pagination and filtering, and adding new books with data validation.

Features
GET /api/books: Retrieves a list of books, with optional pagination and author filtering.
POST /api/books: Adds a new book to the collection, with input validation to ensure both title and author fields are present.
Rate Limiting: Limits requests to 5 per minute to avoid overloading the server.
Technologies Used
Flask: Framework for creating the API.
Flask-Limiter: Middleware for rate limiting to enhance security and prevent abuse.
Logging: Configured to log events such as book additions and request handling.
Setup
Install required dependencies:

bash
Code kopieren
pip install Flask Flask-Limiter
Run the application:

bash
Code kopieren
python app.py
The API will be available at http://127.0.0.1:5000.

Endpoints
GET /api/books
Description: Retrieves a list of books with optional filters and pagination.

Parameters:

author (optional): Filter books by author.
page (optional): Page number for pagination (default is 1).
limit (optional): Number of results per page (default is 10).
Rate Limit: 5 requests per minute.

Example: GET /api/books?page=1&limit=5&author=George%20Orwell

Response:

200 OK: List of books in JSON format.
POST /api/books
Description: Adds a new book to the collection.

Body:

title: The title of the book (required).
author: The author of the book (required).
Rate Limit: 5 requests per minute.

Example:

json
Code kopieren
{
  "title": "New Book Title",
  "author": "Author Name"
}
Response:

201 Created: Newly added book details in JSON format.
400 Bad Request: Invalid data if title or author is missing.
Logging
The application logs requests and important actions, such as:

Incoming requests (GET or POST).
Errors if data validation fails.
Successful addition of new books.
Logs are displayed in the console with timestamps, levels, and messages.
