from tests import ViewTestCase
from .models import User
from .mocks import MockForm
from flask_generic_views import CreateFormView, ShowView


class TestCreateFormView(ViewTestCase):
    def setup_method(self, method):
        ViewTestCase.setup_method(self, method)

        self.app.add_url_rule('/users/new',
            view_func=CreateFormView.as_view('edit',
            model_class=User,
            form_class=MockForm),
        )
        self.app.add_url_rule('/users',
            view_func=ShowView.as_view('user.show', model_class=User)
        )

    def test_renders_template_on_get_request(self):
        response = self.client.get('/users/new')

        assert response.status_code == 200

    def test_redirects_on_succesful_post_request(self):
        response = self.client.post('/users/new',
            data={'name': u'Jack Daniels'}
        )

        assert response.status_code == 302

    def test_updates_database_on_succesful_post_request(self):
        self.client.post('/users/new',
            data={'name': u'Jack Daniels'}
        )
        assert User.query.first().name == u'Jack Daniels'
