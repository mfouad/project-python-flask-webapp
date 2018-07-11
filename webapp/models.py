from webapp import db
    
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    done = db.Column(db.Boolean, default=0)
    deadline = db.Column(db.Date())

    def __init__(self, name, done, deadline):
        self.name = name
        self.done = done
        self.deadline = deadline
    
    def __repr__(self):
        return "[{0}] {1}".format(self.done, self.name)
