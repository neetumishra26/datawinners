import unittest
import settings
from datawinners.submission.organization_finder import OrganizationFinder
from datawinners.tests.data import TRIAL_ACCOUNT_ORGANIZATION_ID, TRIAL_ACCOUNT_DATA_SENDER_MOBILE_NO, DEFAULT_TEST_ORG_TEL_NO, DEFAULT_TEST_ORG_ID

class TestOrganizationFinder(unittest.TestCase):
    def test_should_find_organization_for_trial_account(self):
        organization,error = OrganizationFinder().find(TRIAL_ACCOUNT_DATA_SENDER_MOBILE_NO, settings.TRIAL_ACCOUNT_PHONE_NUMBER)
        # this organization is created in test data
        self.assertEqual(TRIAL_ACCOUNT_ORGANIZATION_ID,organization.org_id)

    def test_should_return_error_when_datasender_is_not_registered_for_trial_account(self):
        organization,error = OrganizationFinder().find("123", settings.TRIAL_ACCOUNT_PHONE_NUMBER)
        # this organization is created in test data
        self.assertEqual(u"Sorry, this number 123 is not registered with us.",error)

    def test_should_return_error_when_organization_doesnot_exists(self):
        organization,error = OrganizationFinder().find("123", "678")
        # this organization is created in test data
        self.assertEqual(u'No organization found for telephone number 678',error)

    def test_should_return_organization(self):
        organization,error = OrganizationFinder().find("123", DEFAULT_TEST_ORG_TEL_NO)
        # this organization is created in test data
        self.assertEqual(DEFAULT_TEST_ORG_ID,organization.org_id)