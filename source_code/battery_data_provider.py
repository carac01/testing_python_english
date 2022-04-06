from unittest import TestCase, main
from battery import Battery
from unittest_data_provider import data_provider


class BatteryTest(TestCase):
    charge_items = lambda: (
        (0, False),
        (1, False),
        (35, False),
        (50, False),
        (99, False),
        (100, True),
    )

    def setUp(self) -> None:
        self.battery = Battery()

    @data_provider(charge_items)
    def test_is_full_charged(self, percentage, expected):
        self.battery.set_percentage(percentage)
        self.assertTrue(self.battery.is_full() == expected)


if __name__ == "__main__":
    main()
