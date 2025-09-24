from App import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    total_hours = db.Column(db.Integer, default=0, nullable=False)

    service_hours = db.relationship("ServiceHour", backref="student", lazy=True)
    accolades = db.relationship("Accolade", backref="student", lazy=True)

    def __repr__(self):
        return f"<Student {self.id} {self.name} ({self.total_hours}h)>"
