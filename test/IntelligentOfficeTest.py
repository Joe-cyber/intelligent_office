import unittest
from unittest.mock import patch
import mock.GPIO as GPIO
from mock.RTC import RTC
from IntelligentOffice import IntelligentOffice
from IntelligentOfficeError import IntelligentOfficeError


class IntelligentOfficeTest(unittest.TestCase):
    """
    Define your test cases here
    """

    def setUp(self) -> None:
        self.io = IntelligentOffice()

    @patch.object(GPIO, 'input')
    def test_check_quadrant_occupancy_pin_one_false(self, mock_input):
        mock_input.return_value = 0
        occ = self.io.check_quadrant_occupancy(self.io.INFRARED_PIN_1)
        self.assertFalse(occ)

    @patch.object(GPIO, 'input')
    def test_check_quadrant_occupancy_pin_one_true(self, mock_input):
        mock_input.return_value = 50
        occ = self.io.check_quadrant_occupancy(self.io.INFRARED_PIN_1)
        self.assertTrue(occ)

    def test_check_quadrant_occupancy_wrong_pin(self):
        self.assertRaises(IntelligentOfficeError, self.io.check_quadrant_occupancy, 10)

    @patch.object(RTC, 'get_current_time_string')
    @patch.object(RTC, 'get_current_day')
    def test_manage_blinds_based_on_time_true(self, mock_rtc1, mock_rtc2):
        mock_rtc1.return_value = "MONDAY"
        mock_rtc2.return_value = "08:00:59"
        self.io.manage_blinds_based_on_time()
        self.assertTrue(self.io.is_blinds_open())

    @patch.object(RTC, 'get_current_time_string')
    @patch.object(RTC, 'get_current_day')
    def test_manage_blinds_based_on_time_false_week_end(self, mock_rtc1, mock_rtc2):
        mock_rtc1.return_value = "SUNDAY"
        mock_rtc2.return_value = "08:00:59"
        self.io.manage_blinds_based_on_time()
        self.assertFalse(self.io.is_blinds_open())

    @patch.object(RTC, 'get_current_time_string')
    @patch.object(RTC, 'get_current_day')
    def test_manage_blinds_based_on_time_false(self, mock_rtc1, mock_rtc2):
        mock_rtc1.return_value = "MONDAY"
        mock_rtc2.return_value = "20:00:59"
        self.io.manage_blinds_based_on_time()
        self.assertFalse(self.io.is_blinds_open())
