import logging
from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app=app, key_func=get_remote_address)

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# The list of books
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen"},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 6, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 7, "title": "Moby Dick", "author": "Herman Melville"},
    {"id": 8, "title": "War and Peace", "author": "Leo Tolstoy"},
    {"id": 9, "title": "Jane Eyre", "author": "Charlotte Brontë"},
    {"id": 10, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky"},
    {"id": 11, "title": "Wuthering Heights", "author": "Emily Brontë"},
    {"id": 12, "title": "The Odyssey", "author": "Homer"},
    {"id": 13, "title": "Brave New World", "author": "Aldous Huxley"},
    {"id": 14, "title": "The Iliad", "author": "Homer"},
    {"id": 15, "title": "The Divine Comedy", "author": "Dante Alighieri"},
    {"id": 16, "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky"},
    {"id": 17, "title": "Anna Karenina", "author": "Leo Tolstoy"},
    {"id": 18, "title": "Great Expectations", "author": "Charles Dickens"},
    {"id": 19, "title": "Ulysses", "author": "James Joyce"},
    {"id": 20, "title": "The Grapes of Wrath", "author": "John Steinbeck"},
    {"id": 21, "title": "Les Misérables", "author": "Victor Hugo"},
    {"id": 22, "title": "Dracula", "author": "Bram Stoker"},
    {"id": 23, "title": "Heart of Darkness", "author": "Joseph Conrad"},
    {"id": 24, "title": "Frankenstein", "author": "Mary Shelley"},
    {"id": 25, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde"},
    {"id": 26, "title": "The Alchemist", "author": "Paulo Coelho"},
    {"id": 27, "title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll"},
    {"id": 28, "title": "Don Quixote", "author": "Miguel de Cervantes"},
    {"id": 29, "title": "The Old Man and the Sea", "author": "Ernest Hemingway"},
    {"id": 30, "title": "A Tale of Two Cities", "author": "Charles Dickens"},
    {"id": 31, "title": "The Count of Monte Cristo", "author": "Alexandre Dumas"},
    {"id": 32, "title": "The Sun Also Rises", "author": "Ernest Hemingway"},
    {"id": 33, "title": "Sense and Sensibility", "author": "Jane Austen"},
    {"id": 34, "title": "The Scarlet Letter", "author": "Nathaniel Hawthorne"},
    {"id": 35, "title": "The Little Prince", "author": "Antoine de Saint-Exupéry"},
    {"id": 36, "title": "Beloved", "author": "Toni Morrison"},
    {"id": 37, "title": "The Road", "author": "Cormac McCarthy"},
    {"id": 38, "title": "Slaughterhouse-Five", "author": "Kurt Vonnegut"},
    {"id": 39, "title": "Of Mice and Men", "author": "John Steinbeck"},
    {"id": 40, "title": "Gone with the Wind", "author": "Margaret Mitchell"},
    {"id": 41, "title": "Catch-22", "author": "Joseph Heller"},
    {"id": 42, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"id": 43, "title": "Rebecca", "author": "Daphne du Maurier"},
    {"id": 44, "title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez"},
    {"id": 45, "title": "Madame Bovary", "author": "Gustave Flaubert"},
    {"id": 46, "title": "In Search of Lost Time", "author": "Marcel Proust"},
    {"id": 47, "title": "The Secret Garden", "author": "Frances Hodgson Burnett"},
    {"id": 48, "title": "The Handmaid's Tale", "author": "Margaret Atwood"},
    {"id": 49, "title": "A Clockwork Orange", "author": "Anthony Burgess"},
    {"id": 50, "title": "Lolita", "author": "Vladimir Nabokov"},
    {"id": 51, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 52, "title": "The Wind in the Willows", "author": "Kenneth Grahame"},
    {"id": 53, "title": "The Color Purple", "author": "Alice Walker"},
    {"id": 54, "title": "Dune", "author": "Frank Herbert"},
    {"id": 55, "title": "The Kite Runner", "author": "Khaled Hosseini"},
    {"id": 56, "title": "Life of Pi", "author": "Yann Martel"},
    {"id": 57, "title": "The Shining", "author": "Stephen King"},
    {"id": 58, "title": "The Bell Jar", "author": "Sylvia Plath"},
    {"id": 59, "title": "Animal Farm", "author": "George Orwell"},
    {"id": 60, "title": "The Three Musketeers", "author": "Alexandre Dumas"},
    {"id": 61, "title": "Little Women", "author": "Louisa May Alcott"},
    {"id": 62, "title": "Gone Girl", "author": "Gillian Flynn"},
    {"id": 63, "title": "The Time Machine", "author": "H.G. Wells"},
    {"id": 64, "title": "The Road", "author": "Cormac McCarthy"},
    {"id": 65, "title": "The Stand", "author": "Stephen King"},
    {"id": 66, "title": "Emma", "author": "Jane Austen"},
    {"id": 67, "title": "The Call of the Wild", "author": "Jack London"},
    {"id": 68, "title": "The Name of the Rose", "author": "Umberto Eco"},
    {"id": 69, "title": "The Giver", "author": "Lois Lowry"},
    {"id": 70, "title": "Fahrenheit 451", "author": "Ray Bradbury"},
    {"id": 71, "title": "The Phantom of the Opera", "author": "Gaston Leroux"},
    {"id": 72, "title": "The Hunger Games", "author": "Suzanne Collins"},
    {"id": 73, "title": "The Da Vinci Code", "author": "Dan Brown"},
    {"id": 74, "title": "The Fault in Our Stars", "author": "John Green"},
    {"id": 75, "title": "The Perks of Being a Wallflower", "author": "Stephen Chbosky"},
    {"id": 76, "title": "The Book Thief", "author": "Markus Zusak"},
    {"id": 77, "title": "The Girl on the Train", "author": "Paula Hawkins"},
    {"id": 78, "title": "The Poisonwood Bible", "author": "Barbara Kingsolver"},
    {"id": 79, "title": "Memoirs of a Geisha", "author": "Arthur Golden"},
    {"id": 80, "title": "The Alchemist", "author": "Paulo Coelho"},
    {"id": 81, "title": "The Help", "author": "Kathryn Stockett"},
    {"id": 82, "title": "The Outsiders", "author": "S.E. Hinton"},
    {"id": 83, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
    {"id": 84, "title": "The Lovely Bones", "author": "Alice Sebold"},
    {"id": 85, "title": "Twilight", "author": "Stephenie Meyer"},
    {"id": 86, "title": "The Maze Runner", "author": "James Dashner"},
    {"id": 87, "title": "Divergent", "author": "Veronica Roth"},
    {"id": 88, "title": "Water for Elephants", "author": "Sara Gruen"},
    {"id": 89, "title": "The Secret Life of Bees", "author": "Sue Monk Kidd"},
    {"id": 90, "title": "Room", "author": "Emma Donoghue"},
    {"id": 91, "title": "The Road", "author": "Cormac McCarthy"},
    {"id": 92, "title": "Beautiful Disaster", "author": "Jamie McGuire"},
    {"id": 93, "title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson"},
    {"id": 94, "title": "The Lovely Bones", "author": "Alice Sebold"},
    {"id": 95, "title": "Gone Girl", "author": "Gillian Flynn"},
    {"id": 96, "title": "Ender's Game", "author": "Orson Scott Card"},
    {"id": 97, "title": "A Game of Thrones", "author": "George R.R. Martin"},
    {"id": 98, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling"},
    {"id": 99, "title": "Percy Jackson and the Olympians: The Lightning Thief", "author": "Rick Riordan"},
    {"id": 100, "title": "The Mortal Instruments: City of Bones", "author": "Cassandra Clare"}
]


def validate_book_data(data):
    if "title" not in data or "author" not in data:
        return False
    return True


@app.route('/api/books', methods=['GET', 'POST'])
@limiter.limit("5/minute")
def handle_books():
    if request.method == 'POST':
        app.logger.info("POST request received for adding a new book.")

        # Get the new book data from the client
        new_book = request.get_json()
        if not validate_book_data(new_book):
            return jsonify({"error": "Invalid book data"}), 400
        # Generate a new ID for the book
        new_id = max(book['id'] for book in books) + 1
        new_book['id'] = new_id
        # Add the new book to our list
        books.append(new_book)
        # Return the new book data to the client
        return jsonify(new_book), 201
    else:
        app.logger.info('GET request received for /api/books')  # Log a message

        # Handle the GET request
        author = request.args.get('author')
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))

        # Filter by author if an author is specified
        filtered_books = books
        if author:
            filtered_books = [book for book in books if book.get('author') == author]

        # Paginate the result
        start_index = (page - 1) * limit
        end_index = start_index + limit
        paginated_books = filtered_books[start_index:end_index]

        return jsonify(paginated_books)


def find_book_by_id(book_id):
    """ Find the book with the id `book_id`.
    If there is no book with this id, return None. """
    for book in books:
        if book["id"] == book_id:
            return book
    return None


@app.route('/api/books/<int:id>', methods=['PUT'])
def handle_book(id):
    # Find the book with the given ID
    book = find_book_by_id(id)
    # If the book wasn't found, return a 404 error
    if book is None:
        return '', 404
    # Update the book with the new data
    new_data = request.get_json()
    book.update(new_data)
    # Return the updated book
    return jsonify(book)


@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    # Find the book with the given ID
    book = find_book_by_id(id)
    # If the book wasn't found, return a 404 error
    if book is None:
        return '', 404
    books.remove(book)

    # Return the deleted book
    return jsonify(book)


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404


@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({"error": "Method Not Allowed"}), 405


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)