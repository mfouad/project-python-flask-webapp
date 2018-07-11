import wtforms
from wtforms import TextField, Form, DateField
from wtforms.validators import Required

class TaskForm(Form):
    name = TextField("Task Name", [Required])
    deadline = TextField("Deadline")




