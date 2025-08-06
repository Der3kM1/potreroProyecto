from flask import Blueprint, render_template
import requests

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses')
def courses():
    api_url = 'https://potrero-digital-api.vercel.app/courses'
    response = requests.get(api_url)
    courses_data = response.json() if response.status_code == 200 else []

    return render_template('courses.html', courses=courses_data)