"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    tups = hackbright.get_grades_by_github(github)
    print(tups)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github, tups=tups)
    return html


@app.route("/student-add", methods=['GET'])
def student_add():
    """Add a student."""

    return render_template('student_add.html')


@app.route("/add-confirmation", methods=['POST'])
def confirmation():
    """Confirm and Add Student"""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    html = render_template('add_confirmation.html', 
                           first_name=first_name, 
                           last_name=last_name, github=github)
    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
