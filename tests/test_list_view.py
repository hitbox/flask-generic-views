from tests import ViewTestCase
from .extensions import db
from .models import User
from flask_generic_views import SortedListView


class TestListView(ViewTestCase):
    def setup_method(self, method):
        ViewTestCase.setup_method(self, method)
        self.app.add_url_rule('/users',
            view_func=SortedListView.as_view('index', model_class=User),
        )

        user = User(name=u'John Matrix')
        db.session.add(user)
        db.session.commit()

    def test_if_template_not_set_tries_to_use_default_template(self):
        response = self.client.get('/users')
        response.status_code == 200

    def test_supports_json(self):
        response = self.xhr_client.get('/users')
        assert response.status_code == 200
        assert response.json['data'][0]['name'] == u'John Matrix'