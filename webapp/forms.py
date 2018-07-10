from wtforms import TextField, Form
from wtforms.validators import Required

class TaskForm(Form):
    name = TextField("Task Name", [Required])



