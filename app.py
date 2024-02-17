import csv
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app import db, Tutor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    
def import_tutors_from_csv(csv_path='mockTutorList.csv'):
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Check if tutor already exists to avoid duplicates
            existing_tutor = Tutor.query.filter_by(email=row['EMAIL']).first()
            if existing_tutor is None:  # Add new tutor if not already in database
                new_tutor = Tutor(
                    name=row['NAME'],
                    age=int(row['AGE']),
                    email=row['EMAIL'],
                    subject=row['SUBJECT'],
                    x=int(row['X']),
                    y=int(row['Y'])
                )
                db.session.add(new_tutor)
        db.session.commit()
        
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Extract form data
        NAME = request.form['NAME']
        AGE = request.form['AGE']
        EMAIL = request.form['EMAIL']
        SUBJECT = request.form['SUBJECT']
        # Create a new Tutor object
        new_tutor = Tutor(NAME=NAME,AGE = AGE, EMAIL=EMAIL, SUBJECT=SUBJECT)

        # Add to the database session and commit
        db.session.add(new_tutor)
        db.session.commit()

        # Redirect to a confirmation page or the home page
        return redirect(url_for('home'))
    return render_template('register.html')
