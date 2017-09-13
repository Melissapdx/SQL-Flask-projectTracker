"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first_name, last_name, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                           first_name=first_name,
                           last_name=last_name,
                           github=github)

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student"""
    return render_template("student_search.html")


@app.route("/student-add", methods=["GET"])
def display_student_form():
    """ Shows form to add student info """
    return render_template("student_add.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student"""
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')
    hackbright.make_new_student(first_name, last_name, github)

    html = render_template("student_added.html", first_name=first_name, last_name=last_name, github=github)

    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
