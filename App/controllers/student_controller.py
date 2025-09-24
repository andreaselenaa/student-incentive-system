from App import db
from App.models.student import Student
from App.models.service_hour import ServiceHour
from App.models.accolade import Accolade

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

