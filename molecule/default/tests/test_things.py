import os
import pytest


class TestSuiteForThings(object):
    """A bunch of things to test!"""

    @pytest.mark.test_id('a1f75204-9bf8-11e8-877e-0025227c8120')
    @pytest.mark.jira('JIRA-123')
    def test_first_thing(self, host):
        """
        First test
        """

        assert "FAIL_FIRST_THING" not in os.environ

    @pytest.mark.test_id('a1f74ef8-9bf8-11e8-877e-0025227c8120')
    @pytest.mark.jira('JIRA-1234')
    def test_second_thing(self, host):
        """
        Second test
        """

        assert "FAIL_SECOND_THING" not in os.environ

    @pytest.mark.test_id('a1f74ba6-9bf8-11e8-877e-0025227c8120')
    @pytest.mark.jira('JIRA-12345')
    @pytest.mark.skip(reason='Nobody has time for three tests!')
    def test_third_thing(self, host):
        """
        Third test
        """

        assert "FAIL_THIRD_THING" not in os.environ
