import pytest
from flask import url_for

from pypnusershub.tests.utils import set_logged_user_cookie

from gn_module_monitoring.tests.fixtures.generic import *


@pytest.mark.usefixtures("client_class", "temporary_transaction")
class TestModules:
    def test_get_modules_api(self, monitorings_users):
        set_logged_user_cookie(self.client, monitorings_users["admin_user"])
        r = self.client.get(url_for("monitorings.get_modules_api"))
        # TODO test structure
        assert r.status_code == 200
