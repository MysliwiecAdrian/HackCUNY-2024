from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

tutors_df = pd.read_csv("mockTutorList.csv")
tutors = tutors_df.to_dict('index')

@app.route('/')
def home():
    return "Welcome to Be My Tutor!"

@app.route('/register_tutor', methods=['POST'])
def register_tutor():
    new_tutor_data = request.json
    new_tutor_id = max(tutors.keys()) + 1 if tutors else 1  # Generate a new tutor ID
    tutors[new_tutor_id] = new_tutor_data
    # For demonstration, to see the updated tutors dictionary
    print(tutors)
    return jsonify({"message": "Tutor registered successfully", "tutor_id": new_tutor_id})

if __name__ == '__main__':
    app.run(debug=True)
