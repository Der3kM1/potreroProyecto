from flask import Flask, render_template
from views.home import home
from views.courses import courses
from views.detail import detail

app = Flask(__name__)

@app.route('/')
def index():
    return home()

@app.route('/courses')
def course_list():
    return courses()

@app.route('/courses/<int:course_id>')
def course_detail(course_id):
    return detail(course_id)

if __name__ == '__main__':
    app.run(debug=True)