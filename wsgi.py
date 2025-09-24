# wsgi.py

from App import create_app, db
from App.models.student import Student
from App.models.staff import Staff
from App.models.service_hour import ServiceHour
from App.models.accolade import Accolade

from App.seed import student_db, staff_db


from app.controllers import student_controller, staff_controller, leaderboard_controller
import click

app = create_app()

@app.cli.command("initdb")
def initdb():
    """Create database tables."""
    db.create_all()
    click.echo("Initialized the database.")

@app.cli.command("seed")
def seed():
    """Seed DB with sample students & staff."""
    db.create_all()
    if not Student.query.first():
        s1 = Student(name="Alice")
        s2 = Student(name="Bob")
        staff = Staff(name="Mr. Smith")
        db.session.add_all([s1, s2, staff])
        db.session.commit()
        click.echo("Seeded sample data: students (Alice, Bob) and staff (Mr. Smith).")
    else:
        click.echo("Already seeded.")

@app.cli.command("log-hours")
@click.option("--staff-id", required=True, type=int)
@click.option("--student-id", required=True, type=int)
@click.option("--hours", required=True, type=int)
def cli_log_hours(staff_id, student_id, hours):
    sh = staff_controller.log_hours(staff_id, student_id, hours)
    click.echo(f"Logged {hours} hours for student {student_id}. Entry id: {sh.id}")

@app.cli.command("request-confirmation")
@click.option("--student-id", required=True, type=int)
@click.option("--hours", required=True, type=int)
def cli_request_confirmation(student_id, hours):
    sh = student_controller.request_confirmation(student_id, hours)
    click.echo(f"Requested confirmation for {hours} hours. Request id: {sh.id}")

@app.cli.command("confirm-hours")
@click.option("--service-hour-id", required=True, type=int)
@click.option("--staff-id", required=True, type=int)
def cli_confirm_hours(service_hour_id, staff_id):
    sh = staff_controller.confirm_hours(service_hour_id, staff_id)
    if sh:
        click.echo(f"Confirmed service hours id {service_hour_id} (student {sh.student_id}).")
    else:
        click.echo("ServiceHour not found.")

@app.cli.command("view-leaderboard")
def cli_view_leaderboard():
    rows = leaderboard_controller.get_leaderboard()
    for i, s in enumerate(rows, start=1):
        click.echo(f"{i}. {s.name} - {s.total_hours} hours")

@app.cli.command("view-accolades")
@click.option("--student-id", required=True, type=int)
def cli_view_accolades(student_id):
    s = Student.query.get(student_id)
    if not s:
        click.echo("Student not found.")
        return
    if not s.accolades:
        click.echo("No accolades yet.")
        return
    for a in s.accolades:
        click.echo(f"Milestone {a.milestone} awarded on {a.date_awarded}")

