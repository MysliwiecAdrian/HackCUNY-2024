from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load tutor data from CSV and assign unique 'user_id'
tutors_df = pd.read_csv("mockTutorList.csv")
tutors = {}  # Initialize an empty dictionary to store tutor data with user_id
for index, row in tutors_df.iterrows():
    user_id = index + 1  # Assign a user_id starting from 1
    tutors[user_id] = {
        'name': row['NAME'],
        'age': row['AGE'],
        'email': row['EMAIL'],
        'subject': row['SUBJECT']
    }

@app.route('/')
def home():
    return "Welcome to Be My Tutor!"

@app.route('/register_tutor', methods=['GET', 'POST'])
def register_tutor():
    if request.method == 'POST':
        # Process form data
        new_tutor_data = {
            'name': request.form['name'],
            'age': request.form['age'],
            'email': request.form['email'],
            'subject': request.form['subject']
        }

        # Validate incoming data
        if not all(key in new_tutor_data for key in ('name', 'age', 'email', 'subject')):
            return jsonify({"error": "Missing data in request"}), 400

        # Generate a new tutor ID
        new_tutor_id = max(tutors.keys()) + 1 if tutors else 1
        tutors[new_tutor_id] = new_tutor_data

        print(tutors)  # For debugging purposes

        return jsonify({"message": "Tutor registered successfully", "tutor_id": new_tutor_id})

    # If it's a GET request, render the registration form
    return render_template('register_tutor.html')

if __name__ == '__main__':
    app.run(debug=True)
