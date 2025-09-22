from app import db
from datetime import datetime

class Accolade(db.Model):
    __tablename__ = "accolades"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    milestone = db.Column(db.Integer, nullable=False) 
    date_awarded = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Accolade {self.milestone}h for student {self.student_id}>"

