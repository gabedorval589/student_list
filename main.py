from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)


# Configure SQLite database
# NB : As of Flask-SQLAlchemy 3.0, any SQLite database defined with a relative path (e.g., sqlite:///project.db) is automatically placed in the instance/ folder to ensure it isn't accidentally created in the application's root directory.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mystudents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

# Create SQLAlchemy instance
db = SQLAlchemy(app)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"

s_list = ['student1', 'student2']
s_dict = {'name': 'Brendan',
          'age': '15',
          'grade': '9th'}

s_list.append(s_dict)

students = [
    {'name': 'Brendan', 'age': '15', 'grade': '9th'},
    {'name': 'Eli', 'age': '15', 'grade': '9th'}
]

@app.route("/")
def hello_world():
    return render_template("hello.html")

@app.route("/students", methods=['GET'])
def get_students():
    return render_template("list_students.html", students = students)

@app.route("/students", methods=['POST'])
def add_students():
    students.append(s_dict)
    return students

if __name__ == '__main__':
    with app.app_context():  # Needed for DB operations
        db.create_all()      # Creates the database and tables
    app.run(debug=True)
