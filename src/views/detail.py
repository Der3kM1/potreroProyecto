from flask import render_template
from flask import request
from firebase_admin import firestore
from firebase.firebase_config import db
db = firestore.client()

def detail(course_id):
    course_ref = db.collection('courses').document(course_id)
    course = course_ref.get()

    if course.exists:
        course_data = course.to_dict()
        return render_template('detail.html', course=course_data)
    else:
        return render_template('detail.html', course=None)