import flask
from webapp import app
import os
from webapp.models import Task
import unittest
import tempfile
from webapp.views import is_due, is_assigned
from datetime import *

class TaskTestCase(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_request(self):
        with app.test_request_context('/?name=Peter'):
            assert flask.request.path == '/'
            assert flask.request.args['name'] == 'Peter'

    @unittest.skip
    def test_web_view(self):
        with app.test_client() as c:
            resp = c.get('/tasks')
            data = flask.json.loads(resp.data)
            assertEquals(data['contains'], "Ahmed")

    @unittest.skip
    def test_post(self):
        with app.test_client() as c:
            rv = c.post('/api/auth', json={
                'username': 'flask', 'password': 'secret'
            })
            json_data = rv.get_json()
            assert(json_data)

    def test_due_today(self):
        task = Task("test task", False, date.today())
        assert(is_due(task) == True)

    def test_due_tomorrow(self):
        task = Task("test task", False, date.today() + timedelta(days=1))
        assert(is_due(task) == False)

    def test_due_yesterday(self):
        task = Task("test task", False, date.today() + timedelta(days=-2))
        assert(is_due(task) == True)


    def test_datetime(self):
        assert((datetime.now() - timedelta(seconds=5)) < datetime.now())

    def test_assignee(self):
        task = Task("fouad", False, date.today())
        assert(is_assigned(task, "fouad"))

    def test_assignee_case_insensiteve(self):
        task = Task("fouad", False, date.today())
        assert(is_assigned(task, "Fouad"))

        task = Task("FouaD", False, date.today())
        assert(is_assigned(task, "Fouad"))
    
if __name__ == '__main__':
    unittest.main()