from app import db
from app.models.student import Student
from app.models.service_hour import ServiceHour
from app.models.accolade import Accolade

MILESTONES = [10, 25, 50]

def request_confirmation(student_id: int, hours: int):
    """Student requests staff confirmation — creates unconfirmed ServiceHour."""
    sh = ServiceHour(student_id=student_id, hours=hours, confirmed=False)
    db.session.add(sh)
    db.session.commit()
    return sh

def view_accolades(student_id: int):
    student = Student.query.get(student_id)
    if not student:
        return None
    return student.accolades

