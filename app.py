from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mytutors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Tutor model definition
class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    subject = db.Column(db.String(50), nullable=False)

# Function to import tutor data from CSV
def import_tutor_data():
    tutors_df = pd.read_csv("mockTutorList.csv")
    for index, row in tutors_df.iterrows():
        new_tutor = Tutor(
            name=row['NAME'],
            age=row['AGE'],
            email=row['EMAIL'],
            subject=row['SUBJECT']
        )
        db.session.add(new_tutor)
    db.session.commit()

# Homepage route
@app.route('/')
def home():
    return "Welcome to Be My Tutor!"

# Register tutor route
@app.route('/register_tutor', methods=['GET', 'POST'])
def register_tutor():
    if request.method == 'POST':
        new_tutor_data = {
            'name': request.form['name'],
            'age': request.form['age'],
            'email': request.form['email'],
            'subject': request.form['subject']
        }

        # Create a new Tutor instance
        new_tutor = Tutor(**new_tutor_data)

        # Add the new tutor to the database session and commit
        db.session.add(new_tutor)
        db.session.commit()

        return jsonify({"message": "Tutor registered successfully", "tutor_id": new_tutor.id})

    # If it's a GET request, render the registration form
    return render_template('register_tutor.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
