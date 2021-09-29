# thirstie_challenge
## install project
prerequisites: Python 3.8
* create virtual environment
* inside environment run "pip install -r requirements.txt"
* run "python manage.py migrate"
* run "python manage.py runserver"
## endpoints
First,I use a swagger for the 4 crud 
*    "libraries": "http://localhost:8000/libraries/",
*    "books": "http://localhost:8000/books/",
*    "user_library": "http://localhost:8000/user_library/",
*    "library_books": "http://localhost:8000/library_books/"  

I used a new user table to make it easier but on a secure context I would have used  the auth_user table that comes with django 
"library_books": "http://localhost:8000/library_books/"  have 2 query parameters user_id 
for example: http://localhost:8000/library_books/?library_id=2
