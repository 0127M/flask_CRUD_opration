from myapp import db

class Student(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    email=db.Column(db.String(20))

    def __repr__(self):
        return {
            'first_name':self.first_name,
            'last_name':self.last_name,
            'email':self.email

        }

