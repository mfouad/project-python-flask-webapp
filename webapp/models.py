from webapp import db
    
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    done = db.Column(db.Boolean, default=0)

    def __init__(self, name, done):
        self.name = name
        self.done = done
    
    def __repr__(self):
        return "[{0}] {1}".format(self.done, self.name)
