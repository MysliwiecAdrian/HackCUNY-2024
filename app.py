from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    # Add more fields as needed

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Extract form data
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        # Create a new Tutor object
        new_tutor = Tutor(name=name, email=email, subject=subject)
        # Add more fields as necessary

        # Add to the database session and commit
        db.session.add(new_tutor)
        db.session.commit()

        # Redirect to a confirmation page or the home page
        return redirect(url_for('home'))
    return render_template('register.html')