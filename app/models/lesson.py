class Lesson:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject

    def get_qr_code_data(self):
        return f'{self.date} {self.subject}'

