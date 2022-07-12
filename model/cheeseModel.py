import sqlite3
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from flask_restful import Api, Resource
import json

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///cheesedir.db")

# define de connection to the database used in LOad from CSV
conn = sqlite3.connect("cheesedir.db", check_same_thread=False)
cur = conn.cursor()

class Cheese():

    totalRows = 0

    def getRowsOfCheese(rowFrom, numRows):
        sqlStr = getSqlStrSearch(rowFrom, numRows)
        return db.execute(sqlStr)

    def getSqlCount():
        cur.execute(getSqlStrCount())
        totalRows = cur.fetchone()[0]

        return totalRows

def getSqlStrSearch(rowFrom, numRows):

    rowTo = rowFrom + numRows - 1
    valString = " {} AND {} ".format(rowFrom, rowTo)

    sqlStr = "with cheese AS (SELECT ROW_NUMBER () OVER"
    sqlStr = sqlStr + "( ORDER BY CheeseId )  row_num, "
    sqlStr = sqlStr + "CheeseId, CheeseNameEn, CheeseNameFr, ManufacturerNameEn, "
    sqlStr = sqlStr + "ManufacturerNameFr, ManufacturerProvCode, ManufacturingTypeEn, ManufacturingTypeFr, "
    sqlStr = sqlStr + "WebSiteEn, WebSiteFr, FatContentPercent, MoisturePercent, ParticularitiesEn, "
    sqlStr = sqlStr + "ParticularitiesFr, FlavourEn, FlavourFr, CharacteristicsEn, CharacteristicsFr, "
    sqlStr = sqlStr + "RipeningEn, RipeningFr, Organic, CategoryTypeEn, CategoryTypeFr, "
    sqlStr = sqlStr + "MilkTypeEn, MilkTypeFr, MilkTreatmentTypeEn, MilkTreatmentTypeFr, "
    sqlStr = sqlStr + "RindTypeEn, RindTypeFr, LastUpdateDate "
    sqlStr = sqlStr + "FROM cheesedataset)  "
    sqlStr = sqlStr + "SELECT "
    sqlStr = sqlStr + "row_num, "
    sqlStr = sqlStr + "CheeseId, ManufacturerProvCode as province,"
    sqlStr = sqlStr + "CASE WHEN length(CheeseNameEn) > 1 THEN CheeseNameEn ELSE CheeseNameFr END AS CheeseName, "
    sqlStr = sqlStr + "CASE WHEN length(ManufacturerNameEn) > 1 THEN ManufacturerNameEn ELSE ManufacturerNameFr END AS Manufacturer, "
    sqlStr = sqlStr + "CASE WHEN length(MilkTypeEn) > 1 THEN MilkTypeEn ELSE MilkTypeFr END AS MilkType, "
    sqlStr = sqlStr + "CASE WHEN length(ManufacturingTypeEn) > 1 THEN ManufacturingTypeEn ELSE ManufacturingTypeFr END AS ManufacturingType, "
    sqlStr = sqlStr + "CASE WHEN length(WebSiteEn) > 1 THEN WebSiteEn ELSE WebSiteFr END AS WebSite, "
    sqlStr = sqlStr + "MoisturePercent, "
    sqlStr = sqlStr + "CASE WHEN length(ParticularitiesEn) > 1 THEN ParticularitiesEn ELSE ParticularitiesFr END AS Particularities, "
    sqlStr = sqlStr + "CASE WHEN length(FlavourEn) > 1 THEN FlavourEn ELSE FlavourFr END AS Flavour, "
    sqlStr = sqlStr + "CASE WHEN length(CharacteristicsEn) > 1 THEN CharacteristicsEn ELSE CharacteristicsFr END AS Characteristics, "
    sqlStr = sqlStr + "CASE WHEN length(RipeningEn) > 1 THEN RipeningEn ELSE RipeningFr END AS Ripening, "
    sqlStr = sqlStr + "CASE WHEN Organic = 0 THEN 'Not' ELSE 'Organic' END AS Organic, "
    sqlStr = sqlStr + "CASE WHEN length(CategoryTypeEn) > 1 THEN CategoryTypeEn ELSE CategoryTypeFr END AS CategoryType, "
    sqlStr = sqlStr + "CASE WHEN length(MilkTreatmentTypeEn) > 1 THEN MilkTreatmentTypeEn ELSE MilkTreatmentTypeFr END AS MilkTreatment, "
    sqlStr = sqlStr + "CASE WHEN length(RindTypeEn) > 1 THEN RindTypeEn ELSE RindTypeFr END AS RindType, "
    sqlStr = sqlStr + "LastUpdateDate, "
    sqlStr = sqlStr + "FatContentPercent "


    sqlStr = sqlStr + "FROM cheese  "
    sqlStr = sqlStr + "WHERE row_num between "
    sqlStr = sqlStr + valString

    return sqlStr

def getSqlStrCount():
    sqlStr = "with cheese AS (SELECT ROW_NUMBER () OVER"
    sqlStr = sqlStr + "( ORDER BY CheeseId )  row_num, "
    sqlStr = sqlStr + "CheeseId, CheeseNameEn, CheeseNameFr, ManufacturerNameEn, "
    sqlStr = sqlStr + "ManufacturerNameFr, ManufacturerProvCode, ManufacturingTypeEn, ManufacturingTypeFr, "
    sqlStr = sqlStr + "WebSiteEn, WebSiteFr, FatContentPercent, MoisturePercent, ParticularitiesEn, "
    sqlStr = sqlStr + "ParticularitiesFr, FlavourEn, FlavourFr, CharacteristicsEn, CharacteristicsFr, "
    sqlStr = sqlStr + "RipeningEn, RipeningFr, Organic, CategoryTypeEn, CategoryTypeFr, "
    sqlStr = sqlStr + "MilkTypeEn, MilkTypeFr, MilkTreatmentTypeEn, MilkTreatmentTypeFr, "
    sqlStr = sqlStr + "RindTypeEn, RindTypeFr, LastUpdateDate "
    sqlStr = sqlStr + "FROM cheesedataset)  "
    sqlStr = sqlStr + "SELECT "
    sqlStr = sqlStr + "count(*) "
    sqlStr = sqlStr + "FROM cheese  "

    return sqlStr

def parseCSV(filePath):


    # Use Pandas to parse the CSV file
    csvData = pd.read_csv(filePath, header=0, keep_default_na=False, na_values=[' '])

    # Write records stored in the DataFrame csvData to the SQL database 'cheesedir'.
    # always delete the table before insert
    csvData.to_sql('cheesedataset', conn, if_exists='replace', index=False)