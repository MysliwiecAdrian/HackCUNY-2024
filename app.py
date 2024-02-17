import csv
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

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
            existing_tutor = Tutor.query.filter_by(email=row['EMAIL']).first()
            if existing_tutor is None:
                new_tutor = Tutor(
                    name=row['NAME'],
                    age=int(row['AGE']),
                    email=row['EMAIL'],
                    subject=row['SUBJECT']
                )
                db.session.add(new_tutor)
        db.session.commit()

@app.before_first_request
def create_tables_and_import():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_tutor = Tutor(
            name=request.form['name'],  
            age=int(request.form['age']),
            email=request.form['email'],
            subject=request.form['subject']
        )
        db.session.add(new_tutor)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
