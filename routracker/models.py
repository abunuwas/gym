from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))

    def __repr__(self):
        return "<User(username='%s', email='%s', password='%s')>" % (
            self.username, self.email, self.password
        )

class ExerciseRoutine(db.Model):
    __tablename__ = 'exercise_routine'

    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column()
    routine = db.Column()

class Performance(db.Model):
    __tablename__ = 'performance'

    id = db.Column(db.Integer, primary_key=True)
    exercise_routine = db.Column()
    rating = db.Column(db.Integer)

class Exercise(db.Model):
    __exercise__ = 'exercises'

    id = db.Column(db.Intger, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text)
    schedule = db.Column()
    performance = db.Column()
    rating = db.Column()

class Routine(db.Model):
    __routine__ = 'routines'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    schedule = db.Column()
    exercises = db.Column()
    performance = db.Column()
    rating = db.Column()


