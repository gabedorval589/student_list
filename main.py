from flask import Flask, jsonify, render_template


app = Flask(__name__)
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
    return render_template("list_students.html")

@app.route("/students", methods=['POST'])
def add_students():
    students.append(s_dict)
    return students

if __name__ == '__main__':
    app.run(debug=True)