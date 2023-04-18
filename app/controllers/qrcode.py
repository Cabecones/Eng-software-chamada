from io import BytesIO

import qrcode
from flask import send_file

from app import app
from app.models import Lesson


@app.route('/qr_code/<date>/<subject>')
def generate_qr_code(date, subject):
    lesson = Lesson(date, subject)
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(f"{date}|{subject}")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    lesson.qr_code = img_io.getvalue()

    return send_file(img_io, mimetype='image/png')
