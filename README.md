# YaMDb

### About:
The YaMDb is a review-aggregation project for film, television, book, music. The YaMDb collect online reviews from users. The users upload their reviews to the movie(TV-show,book,music) page on the website.The YaMDb keeps track of all the reviews counted for each film. An average score on a 0 to 10 scale is also calculated.
### Developers:
- [Iskander Ryskulov](https://github.com/IskanderRRR)
- [Pavel Homov](https://github.com/PavelHomov)
- [Georgy Popov](https://github.com/Georrgeee)

### Applied technologies:
- Python
- Django
- Django Rest Framework
- Simple-JWT
- GIT
- SQLite

### User Roles
- Anonymous - can view descriptions of works, read reviews and comments.

- Authenticated user (user) - can read everything, like Anonymous, can additionally publish reviews and rate works (films / books / songs), can comment on other people's reviews and rate them; can edit and delete their reviews and comments.

- Moderator - the same rights as an Authenticated User plus the right to delete and edit any reviews and comments.

- Administrator (admin) - full rights to manage the project and all its contents. Can create and delete works, categories and genres. Can assign roles to users.

- Django Administrator - Same rights as the Administrator role.

### Cloning a repository and switching to it on the command line:
`https://github.com/IskanderRRR/api_yamdb.git`

`cd api_final_yatube`

### Create and activate virtual environment:
The virtual environment must use Python 3.7

`pyhton -m venv venv`

- Linux/MacOS

`source venv/bin/activate`

- Windows

`source venv/scripts/activate`

### Installing dependencies from the requirements.txt file:
`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

### To start the development server, while in the project directory, run the commands:
`python manage.py migrate`
`python manage.py createsuperuser`
`python manage.py runserver`

### Documentation is available at the address:
`http://127.0.0.1:8000/redoc/`