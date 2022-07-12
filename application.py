import os
import csv
import pandas as pd
import random
from re import sub
from decimal import Decimal
import sqlite3

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session


from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from model.cheeseModel import *

from helpers import apology

# Configure application
app = Flask(__name__)
api = Api(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///cheesedir.db")

# define de connection to the database
# conn = sqlite3.connect("cheesedir.db")
# cur = conn.cursor()

@app.route('/', methods=["GET", "POST"])
def index():

    # generate a random number between 1 and 1364
    # to show 20 random rows each time the index page is open
    totalRows = 1374
    numRows = 5
    currentRow = random.randint(1, totalRows - numRows)

    #DOMAIN = request.base_url
    rowsOfCheese = Cheese.getRowsOfCheese(currentRow, numRows)
    return render_template("index.html", rowsOfCheese=rowsOfCheese)

@app.route('/search/<int:rowfrom>', methods=['GET', 'POST'])
def search(rowfrom):

    # Rows to show per page
    nomRowsToRetrieve = 20
    totalQueryNumOfRows = Cheese.getSqlCount()

    currentRow = rowfrom



    if (currentRow + nomRowsToRetrieve - 1) > totalQueryNumOfRows:
        rowsTo = totalQueryNumOfRows
        nextRow = rowfrom + 1
        previousRow = rowfrom - 20
        nomRowsToRetrieve = totalQueryNumOfRows - currentRow
    else:
        nomRowsToRetrieve = 20
        rowsTo = currentRow + nomRowsToRetrieve - 1
        nextRow = rowsTo + 1
        if (currentRow < 20):
            previousRow = currentRow
        else:
            previousRow = (currentRow - 20)

    #DOMAIN = request.base_url
    rowsOfCheese = Cheese.getRowsOfCheese(currentRow, nomRowsToRetrieve)

    return render_template("search.html",rowsOfCheese=rowsOfCheese,totalQueryNumOfRows=totalQueryNumOfRows,currentRow=currentRow,rowsTo=rowsTo,nextRow=nextRow,previousRow=previousRow)

@app.route('/loadtable', methods=['GET', 'POST'])
def loadtable():

    # a new file is going to be uploaded
    if request.method == 'POST':
        # Create variable for uploaded file
        cheesefile = request.files['fileupload']
        if cheesefile.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], cheesefile.filename)

            # set the file path
            cheesefile.save(file_path)

            parseCSV(file_path)
            return render_template("index.html")

    return render_template("loadtable.html")







