from unittest import TestCase, main
from water import Water

class WaterTest(TestCase):
    def setUp(self) -> None:
        self.myWater = Water()

    def test_solid_state(self):
        for temperature in range(-273, 1):
            self.assertEqual("Solid", self.myWater.get_state(temperature),
                             f"The water state with {temperature} is not solid.")

    def test_liquid_state(self):
        for temperature in range(1, 100):
            self.assertEqual("Liquid", self.myWater.get_state(temperature),
                             f"The water state with {temperature} is not liquid.")

    def test_gaseous_state(self):
        for temperature in range(100, 500):
            self.assertEqual("Gas", self.myWater.get_state(temperature),
                             f"The water state with {temperature} is not gaseous.")


if __name__ == "__main__":
    main()
