# - Projet 8 OC. (P_11 Améliorez un projet existant)

# - Description:
- Creation of an application to find a substitute for consumer products.

# - 1: Project online:
- Go to the following address: "https://indiana-p8-pur-beurre.herokuapp.com/"

# - 2: Initialization of the project locally:
- 1: To initialize the virtual environment: `pipenv install`.
- 2: To position yourself in pipenv : `pipenv shell`.

# - 3: Launch the project locally:
- : If you have already initialized the virtual environment.
- 1: Execute the command `python manage.py installdb` to create the database, then insert the data.
- 2: To run the app: `python manage.py runserver`.
- 3: Once launched, go to your browser and enter the following url: "http://127.0.0.1:8000/".

# -4: Unit test:
- : To launch the unit tests execute in the terminal the command `coverage run --source='.' manage.py test`.
- : To view the test report: `coverage report`.

# - Use:
- : Users have the option of creating an account, logged in, or searching for a product directly.
- : On the home page, find a product to replace and click on the button `Rechercher`.
- : After searching for a product, a choice of six substitutes is displayed, the user then has the option of saving a substitute.
- : The user has the possibility to see the saved favorites.
