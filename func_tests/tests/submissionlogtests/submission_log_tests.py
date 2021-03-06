# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
import unittest
from nose.plugins.attrib import attr
from framework.base_test import  setup_driver, teardown_driver
from framework.utils.data_fetcher import fetch_, from_
from pages.loginpage.login_page import LoginPage
from pages.smstesterpage.sms_tester_page import SMSTesterPage
from testdata.test_data import DATA_WINNER_SMS_TESTER_PAGE, DATA_WINNER_LOGIN_PAGE, DATA_WINNER_DASHBOARD_PAGE
from tests.logintests.login_data import VALID_CREDENTIALS
from tests.smstestertests.sms_tester_data import *
from tests.submissionlogtests.submission_log_data import *


class TestSubmissionLog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = setup_driver()
        cls.driver.go_to(DATA_WINNER_LOGIN_PAGE)
        login_page = LoginPage(cls.driver)
        cls.dashboard = login_page.do_successful_login_with(VALID_CREDENTIALS)

    def setUp(self):
        self.driver.go_to(DATA_WINNER_SMS_TESTER_PAGE)
        self.page = SMSTesterPage(self.driver)

    @classmethod
    def tearDownClass(cls):
        teardown_driver(cls.driver)

    def prerequisites_of_submission_log(self, sms_data):
        sms_tester_page = self.page
        sms_tester_page.send_sms_with(sms_data)
        self.assertEqual(sms_tester_page.get_response_message(), fetch_(MESSAGE, from_(sms_data)))
        self.driver.go_to(DATA_WINNER_DASHBOARD_PAGE)
        view_all_project_page = self.dashboard.navigate_to_view_all_project_page()
        project_overview_project = view_all_project_page.navigate_to_project_overview_page(PROJECT_NAME)
        data_page = project_overview_project.navigate_to_data_page()
        submission_log_page = data_page.navigate_to_all_data_record_page()
        return submission_log_page

    @attr('functional_test', 'smoke')
    def test_verify_successful_sms_submission_log(self):
        """
        Function to test the successful SMS submission
        """
        submission_log_page = self.prerequisites_of_submission_log(VALID_DATA2)
        self.assertRegexpMatches(submission_log_page.get_submission_message(SMS_DATA_LOG),
                                 fetch_(SMS_SUBMISSION, from_(SMS_DATA_LOG)))

    @attr('functional_test')
    def test_invalid_sms_submission_log(self):
        """
        Function to test the invalid SMS submission by exceeding value of the word field limit
        """
        submission_log_page = self.prerequisites_of_submission_log(EXCEED_NAME_LENGTH2)
        self.assertRegexpMatches(submission_log_page.get_submission_message(EXCEED_WORD_LIMIT_LOG),
                                 fetch_(SMS_SUBMISSION, from_(EXCEED_WORD_LIMIT_LOG)))
        self.assertEqual(submission_log_page.get_failure_message(EXCEED_WORD_LIMIT_LOG),
                         fetch_(FAILURE_MSG, from_(EXCEED_WORD_LIMIT_LOG)))

    @attr('functional_test')
    def test_submission_log_for_extra_plus_in_btw_sms(self):
        """
        Function to test the successful SMS submission while using extra plus in between of SMS
        """
        submission_log_page = self.prerequisites_of_submission_log(EXTRA_PLUS_IN_BTW)
        self.assertRegexpMatches(submission_log_page.get_submission_message(EXTRA_PLUS_IN_BTW_LOG),
                                 fetch_(SMS_SUBMISSION, from_(EXTRA_PLUS_IN_BTW_LOG)))

    @attr('functional_test')
    def test_submission_log_for_invalid_geo_code_format(self):
        """
        Function to test the invalid SMS submission for invalid geo code
        """
        submission_log_page = self.prerequisites_of_submission_log(WITH_INVALID_GEO_CODE_FORMAT)
        self.assertRegexpMatches(submission_log_page.get_submission_message(WITH_INVALID_GEO_CODE_FORMAT_LOG),
                                 fetch_(SMS_SUBMISSION, from_(WITH_INVALID_GEO_CODE_FORMAT_LOG)))
        self.assertEqual(submission_log_page.get_failure_message(WITH_INVALID_GEO_CODE_FORMAT_LOG),
                         fetch_(FAILURE_MSG, from_(WITH_INVALID_GEO_CODE_FORMAT_LOG)))
