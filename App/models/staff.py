from App import db

class Staff(db.Model):
    __tablename__ = "staff"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    service_hours = db.relationship("ServiceHour", backref="staff", lazy=True)

    def __repr__(self):
        return f"<Staff {self.id} {self.name}>"
