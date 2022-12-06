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
        self.pg = IntelligentOffice()

    @patch.object(GPIO, 'input')
    def test_check_quadrant_occupancy_pin_one_false(self, mock_input):
        mock_input.return_value = 0
        occ = self.pg.check_quadrant_occupancy(self.pg.INFRARED_PIN_1)
        self.assertFalse(occ)

    @patch.object(GPIO, 'input')
    def test_check_quadrant_occupancy_pin_one_true(self, mock_input):
        mock_input.return_value = 50
        occ = self.pg.check_quadrant_occupancy(self.pg.INFRARED_PIN_1)
        self.assertTrue(occ)

    def test_check_quadrant_occupancy_wrong_pin(self):
        self.assertRaises(IntelligentOfficeError, self.pg.check_quadrant_occupancy, 10)

