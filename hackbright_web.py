"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    rows = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github, 
                           rows=rows)
    
    return html

@app.route("/student-search")
def get_student_form():

    return render_template("student_search.html")

@app.route("/new_student")
def new_student():

    return render_template("new_student.html")

@app.route("/form_results", methods=['POST'])
def form_results():

    first = request.form.get("firstname")
    last = request.form.get("lastname")
    github = request.form.get("github")

    hackbright.make_new_student(first, last, github)

    return render_template("form_results.html", 
                            first=first, last=last, github=github)


@app.route("/project")
def project():

    title = request.args.get('title')

    title, description, max_grade = hackbright.get_project_by_title(title)

    return render_template("get_project.html", 
                           title=title, 
                           description=description,
                           max_grade=max_grade)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
