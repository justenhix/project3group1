# Import the dependencies.
from flask import Flask, jsonify
import csv
import os

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
        f"Available Routes:<br/> Each link shows the month, year, unemployment rate, and number of unemployeed individuals for the respective city.<br/><br/>"
        f"/api/v1.0/raleigh_unep_data<br/><br/>"
        f"/api/v1.0/charlotte_unep_data<br/><br/>"
        f"/api/v1.0/greensboro_unep_data<br/><br/>"
        f"/api/v1.0/winstonsalem_unep_data"
    )



@app.route("/api/v1.0/raleigh_unep_data")
def ral_csv_to_json():
    # Read CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'ral_dd.csv')

    # Check if the file exists
    if not os.path.isfile(csv_file_path):

        return jsonify({"error": "CSV file not found"}), 404
    data = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Convert CSV data to JSON
    json_data = jsonify(data)

    return json_data



@app.route("/api/v1.0/charlotte_unep_data")
def char_csv_to_json():
    # Read CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'char_dd.csv')

    # Check if the file exists
    if not os.path.isfile(csv_file_path):

        return jsonify({"error": "CSV file not found"}), 404
    data = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Convert CSV data to JSON
    json_data = jsonify(data)

    return json_data



@app.route("/api/v1.0/greensboro_unep_data")
def green_csv_to_json():
    # Read CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'green_dd.csv')

    # Check if the file exists
    if not os.path.isfile(csv_file_path):

        return jsonify({"error": "CSV file not found"}), 404
    data = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Convert CSV data to JSON
    json_data = jsonify(data)

    return json_data



@app.route("/api/v1.0/winstonsalem_unep_data")
def win_csv_to_json():
    # Read CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'win_dd.csv')

    # Check if the file exists
    if not os.path.isfile(csv_file_path):

        return jsonify({"error": "CSV file not found"}), 404
    data = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Convert CSV data to JSON
    json_data = jsonify(data)

    return json_data


if __name__ == "__main__":
    app.run(debug=True)

