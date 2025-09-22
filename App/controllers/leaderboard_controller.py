from app.models.student import Student

def get_leaderboard(limit=10):
    return Student.query.order_by(Student.total_hours.desc()).limit(limit).all()
