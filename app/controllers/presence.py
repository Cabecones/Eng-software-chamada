from flask import request, render_template, redirect, url_for

from app import app
from app.models import Lesson, Student


@app.route('/presence/<date>/<subject>')
def presence(date, subject):
    lesson = Lesson(date, subject)

    return render_template('presence.html', lesson=lesson)


@app.route('/check_presence', methods=['POST'])
def check_presence():
    registration = request.form['registration']
    lesson_date, lesson_subject = request.form['lesson'].split('|')

    lesson = Lesson(lesson_date, lesson_subject)
    student = Student('Test', registration)

    lesson.add_attendance(student)

    return redirect(url_for('presence', date=lesson.date, subject=lesson.subject))
