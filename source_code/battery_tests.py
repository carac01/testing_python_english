from unittest import TestCase, main
from battery import Battery
from random import randint

class BatteryTest(TestCase):
    def setUp(self) -> None:
        self.battery = Battery()

    def test_get_percentage(self):
        percentage = self.battery.get_percentage()
        self.assertTrue((0 <= percentage) and (percentage <= 100))

    def test_set_percentage(self):
        self.battery.set_percentage(-1)
        self.assertEqual(self.battery.get_percentage(), 0)

        self.battery.set_percentage(0)
        self.assertEqual(self.battery.get_percentage(), 0)

        self.battery.set_percentage(1)
        self.assertEqual(self.battery.get_percentage(), 1)

        self.battery.set_percentage(50)
        self.assertEqual(self.battery.get_percentage(), 50)

        self.battery.set_percentage(99)
        self.assertEqual(self.battery.get_percentage(), 99)

        self.battery.set_percentage(100)
        self.assertEqual(self.battery.get_percentage(), 100)

        self.battery.set_percentage(101)
        self.assertEqual(self.battery.get_percentage(), 100)

    def test_battery_is_full(self):
        self.battery.set_percentage(100)
        self.assertTrue(self.battery.is_full())

        self.battery.set_percentage(101)
        self.assertTrue(self.battery.is_full())

        self.battery.set_percentage(99)
        self.assertFalse(self.battery.is_full())

        self.battery.set_percentage(0)
        self.assertFalse(self.battery.is_full())

        self.battery.set_percentage(-100)
        self.assertFalse(self.battery.is_full())

    def test_text_percentage_message(self):
        self.battery.set_percentage(randint(0, 100))
        self.assertTrue(self.battery.show_battery_percentage(),
                        f"My percentage is {self.battery.get_percentage()}%")


if __name__ == "__main__":
    main()
