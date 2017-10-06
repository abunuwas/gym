from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))

    def __repr__(self):
        return "<User(username='%s', email='%s', password='%s')>" % (
            self.username, self.email, self.password
        )


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text)


class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    exercise = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    repetitions = db.Column(db.Integer)
    weight = db.Column(db.Float)
    # pound | kg
    weight_unit = db.Column(db.String)
    # good | medium | bad
    performance = db.Column(db.String(128))
