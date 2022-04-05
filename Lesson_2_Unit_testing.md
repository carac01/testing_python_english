### Unit Testing (Component or Module)

The component tests or Unit testing is the methodology in order to check that the function works as expected.<br>
Trying to get the boundaries for quality assure as a result.<br>
In addition, it gives the confidence, feel of safety and peace of mind when new characteristics are added because
it notifies about code stops working.<br>

Though from the first glance it feels like we are waisting the time, 
but in fact the testing optimises the code and makes the project rentable.<br> 
How is it possible?<br>
The test development opens the opportunity to find the new issues - it will reduce the quantity of issues in a future
and there are fewer hours spent to resolve the problem consequently.
Nevertheless, the productivity of the project is low at the beginning.
We could observe this fact on the next graphic:

![tdd.jpg](static/tdd.jpg)

#### Tutorial with Python

Let's create the simple object for managing the smartphone battery.
It will be able to:
* Get the battery percentage.
* Modify the percentage.
* Generate the text with visually nice explanation: "My percentage is 32%".
* It will be called battery.py and will contain the next code inside (source_code/battery.py):

```python
class Battery:
    PERCENTAGE = 0

    def get_percentage(self) -> int:
        return self.PERCENTAGE

    def is_full(self) -> bool:
        return self.PERCENTAGE == 100

    def set_percentage(self, new_percentage):
        my_percentage = new_percentage
        if new_percentage > 100:
            my_percentage = 100
        if new_percentage < 0:
            my_percentage = 0
        self.PERCENTAGE = my_percentage

    def show_battery_percentage(self): 
        return f"My percentage is {self.get_percentage()}"
```

The file with tests for battery.py function is located in source_code/battery_tests.py:

```python
from unittest import TestCase, main
from battery import Battery
from random import randint

class BatteryTest(TestCase):
    def setUp(self):
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
```

As you've already noticed the _setUp_ is used before test run to create the instance of Battery class 
with the functions that are going to be tested, and after the test is finished - _tearDown_ function performed,
usually it contains the instructions for test preconditions, 
returning the environment to previous state like it was before the test run.<br>

When the tests complete, the report is generated:
```log
======================================= test session starts =================================
collected 4 items                                                                                                                                                 

battery_tests.py::BatteryTest::test_battery_is_full PASSED                                   [ 25%]
battery_tests.py::BatteryTest::test_get_percentage PASSED                                    [ 50%]
battery_tests.py::BatteryTest::test_set_percentage PASSED                                    [ 75%]
battery_tests.py::BatteryTest::test_text_percentage_message PASSED                           [100%]

========================================= 4 passed in 0.15s ==================================

```

#### Data Providers

In case we want to check the list of results just call isFull function:

```csv
Function Percentage Expectation
isFull()     0      False
isFull()     1      False
isFull()     35     False
isFull()     50     False
isFull()     99     False
isFull()     100    True
```
It's time to test all of them. Probably, you think that there are more important things exist, and you are right. 