#  💻 HVCC Club Catalogue

 A website created by the HVCC Computer Science club to catalogue the clubs on campus.

## Setting up the app

1. Within the main directory, create a Python virtual environment:<br>
    `python3 -m venv .venv` <br>
    (or potentially `python -m venv .venv` if you don't have Python3)

2. After activating the virtual environment (`. .venv/bin/activate` on Unix or `.venv\Scripts\activate` on Windows), install the required packages via pip:<br>
    `pip install -r requirements.txt`

3. In the main directory, create a .flaskenv file with the following contents:<br>
    `FLASK_APP=app.py`

4. To start the flask application:<br>
    In debug mode: `flask run --debug`

