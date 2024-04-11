# Import the dependencies.
from flask import Flask, jsonify
import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlite3
import pandas as pd


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

# Start page with all routes listed

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/> The first link shows the unemployment rate, and number of unemployed individuals for the respective city based on the year and month. <br/><br/>"
        f"/api/v1.0/year_month_data<br/><br/>"
        f"Each link below shows the month, year, unemployment rate, and number of unemployed individuals for the respective city.<br/><br/>"
        f"/api/v1.0/raleigh_unep_data<br/><br/>"
        f"/api/v1.0/charlotte_unep_data<br/><br/>"
        f"/api/v1.0/greensboro_unep_data<br/><br/>"
        f"/api/v1.0/winstonsalem_unep_data"
    )



@app.route("/api/v1.0/year_month_data")
def year_month_sqlite_to_json():
    # SQLite database file path
    sqlite_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'year_month.sqlite')

    # Check if the file exists
    if not os.path.isfile(sqlite_file_path):
        return jsonify({"error": "SQLite file not found"}), 404
    
    # Connect to SQLite database
    conn = sqlite3.connect(sqlite_file_path)
    cursor = conn.cursor()

    # Fetch data from SQLite table
    cursor.execute("SELECT * FROM year_month")
    data = cursor.fetchall()

    # Close connection
    conn.close()

    # Convert SQLite data to JSON
    json_data = jsonify(data)

    return json_data



@app.route("/api/v1.0/raleigh_unep_data")
def ral_sqlite_to_json():
    # SQLite database file path
    sqlite_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'ral_dd.sqlite')

    # Check if the file exists
    if not os.path.isfile(sqlite_file_path):
        return jsonify({"error": "SQLite file not found"}), 404
    
    # Connect to SQLite database
    conn = sqlite3.connect(sqlite_file_path)
    cursor = conn.cursor()

    # Fetch data from SQLite table
    cursor.execute("SELECT * FROM raleigh")
    data = cursor.fetchall()

    # Close connection
    conn.close()

    # Convert SQLite data to JSON
    json_data = jsonify(data)

    return json_data


@app.route("/api/v1.0/charlotte_unep_data")
def char_sqlite_to_json():
    # Read SQLite file
    sqlite_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'char_dd.sqlite')

    # Check if the file exists
    if not os.path.isfile(sqlite_file_path):
        return jsonify({"error": "SQLite file not found"}), 404
    
    # Connect to SQLite database
    conn = sqlite3.connect(sqlite_file_path)
    cursor = conn.cursor()

    # Fetch data from SQLite table
    cursor.execute("SELECT * FROM charlotte")
    data = cursor.fetchall()

    # Close connection
    conn.close()

    # Convert SQLite data to JSON
    json_data = jsonify(data)

    return json_data



@app.route("/api/v1.0/greensboro_unep_data")
def green_sqlite_to_json():
    # Read SQLite file
    sqlite_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'green_dd.sqlite')

    # Check if the file exists
    if not os.path.isfile(sqlite_file_path):

        return jsonify({"error": "SQLite file not found"}), 404
    
      # Connect to SQLite database
    conn = sqlite3.connect(sqlite_file_path)
    cursor = conn.cursor()

    # Fetch data from SQLite table
    cursor.execute("SELECT * FROM greensboro")
    data = cursor.fetchall()

    # Close connection
    conn.close()

    # Convert SQLite data to JSON
    json_data = jsonify(data)

    return json_data



@app.route("/api/v1.0/winstonsalem_unep_data")
def win_sqlite_to_json():
    # Read SQLite file
    sqlite_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'win_dd.sqlite')

    # Check if the file exists
    if not os.path.isfile(sqlite_file_path):

        return jsonify({"error": "SQLite file not found"}), 404
    
    # Connect to SQLite database
    conn = sqlite3.connect(sqlite_file_path)
    cursor = conn.cursor()

    # Fetch data from SQLite table
    cursor.execute("SELECT * FROM winston")
    data = cursor.fetchall()

    # Close connection
    conn.close()

    # Convert SQLite data to JSON
    json_data = jsonify(data)

    return json_data


if __name__ == "__main__":
    app.run(debug=True)

