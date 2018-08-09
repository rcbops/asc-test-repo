import os
import pytest

"""A bunch of stuff to test!"""


@pytest.mark.test_id('a1f7110e-9bf8-11e8-877e-0025227c8120')
@pytest.mark.jira('JIRA-123')
def test_first_stuff(host):
    """
    First test
    """

    assert "FAIL_FIRST_STUFF" not in os.environ


@pytest.mark.test_id('a1f70dee-9bf8-11e8-877e-0025227c8120')
@pytest.mark.jira('JIRA-1234')
def test_second_stuff(host):
    """
    Second test
    """

    assert "FAIL_SECOND_STUFF" not in os.environ


@pytest.mark.test_id('a1f7034e-9bf8-11e8-877e-0025227c8120')
@pytest.mark.jira('JIRA-12345')
@pytest.mark.skip(reason='Nobody has time for three tests!')
def test_third_stuff(host):
    """
    Third test
    """

    assert "FAIL_THIRD_STUFF" not in os.environ
