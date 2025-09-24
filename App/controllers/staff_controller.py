from App import db
from App.models.service_hour import ServiceHour
from App.models.student import Student
from App.models.accolade import Accolade

MILESTONES = [10, 25, 50]

def log_hours(staff_id: int, student_id: int, hours: int):
    """
    Staff logs hours directly as confirmed (teacher/staff enters and confirms).
    """
    sh = ServiceHour(student_id=student_id, staff_id=staff_id, hours=hours, confirmed=True)
    db.session.add(sh)

    student = Student.query.get(student_id)
    if student:
        student.total_hours += hours
        _award_accolades_if_any(student)
    db.session.commit()
    return sh

def confirm_hours(service_hour_id: int, staff_id: int):
    """Staff confirms a previously requested (unconfirmed) ServiceHour."""
    sh = ServiceHour.query.get(service_hour_id)
    if not sh:
        return None
    if sh.confirmed:
        return sh 
    sh.confirmed = True
    sh.staff_id = staff_id

    student = Student.query.get(sh.student_id)
    if student:
        student.total_hours += sh.hours
        _award_accolades_if_any(student)

    db.session.commit()
    return sh

def _award_accolades_if_any(student):
    """Internal: add Accolade rows if student passed milestones."""
    from App.models.accolade import Accolade
    existing = {a.milestone for a in student.accolades}
    for m in MILESTONES:
        if student.total_hours >= m and m not in existing:
            acc = Accolade(student_id=student.id, milestone=m)
            db.session.add(acc)

