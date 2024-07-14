from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.test.client import RequestFactory


class BaseSuperuserAuthenticatedClient(TestCase):
    """Common Authentication"""

    fixtures = ["auth_user"]
    username = "admin"

    def setUp(self):
        """To create admin user"""
        self.client = Client()

        self.user = User.objects.get(username=self.username)
        self.client.force_login(self.user)

        self.factory = RequestFactory()


class BaseUserAuthenticatedClient(BaseSuperuserAuthenticatedClient):
    username = "user_1"


def assertContainsAny(
    self,
    response,
    texts,
    status_code=200,
    msg_prefix="",
    html=False,
):
    total_count = 0
    for text in texts:
        args = self._assert_contains(response, text, status_code, msg_prefix, html)
        real_count = args[1]
        msg_prefix = args[2]
        total_count += real_count

    self.assertTrue(total_count != 0, f"None of the {texts} were found in the response: {response}")
