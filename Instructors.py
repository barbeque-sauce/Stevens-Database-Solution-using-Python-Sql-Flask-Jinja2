"""
Author : Rohan Chandra 

Python script to create a web server to dispay all instructors information on a webpage using Flask and Jinja2. 

"""
from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
DB_FILE = 'Stevens.db'  #database file location

@app.route('/instructor_courses')
def instuctors():
    query = """select  i.cwid, i.name, i.dept, g.course, count(*) as students
               from instructors i join grades g on i.cwid = g.Instructor_CWID
               group by g.course order by i.cwid"""

    db = sqlite3.connect(DB_FILE)   #connect to the database file
    results = db.execute(query)     #execute the query and return the results

    #convert the query results into a list of dictionaries to pass as a parameter to render_template
    data = [{'cwid': cwid, 'name': name, 'dept': dept, 'course': course, 'students': students}
    for cwid, name, dept, course, students in results]

    db.close()  #close the connection to the database

    return render_template('instructors.html',
                           title='Stevens Repository',
                           table_title='Number of students by course and instructor',
                           instructors=data)

app.run(debug=True)
