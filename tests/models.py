from .extensions import db


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Unicode(255))
    age = db.Column(db.Unicode)

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }