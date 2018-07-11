import flask
from webapp import app
import os
from webapp.models import Task
import unittest
import tempfile

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

    def test_due_date(self):
        assert(1==1)

if __name__ == '__main__':
    unittest.main()