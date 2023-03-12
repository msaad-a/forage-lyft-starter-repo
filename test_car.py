import unittest
from datetime import datetime
from car_factory import CarFactory

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 5)
        car = CarFactory.create_rorschach(today, last_service_date, 0, 0)
        car2 = CarFactory.create_thovex(today, last_service_date, 0, 0)

        self.assertTrue(car.needs_service())
        self.assertTrue(car2.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 3)
        car = CarFactory.create_rorschach(today, last_service_date, 0, 0)
        car2 = CarFactory.create_thovex(today, last_service_date, 0, 0)

        self.assertFalse(car.needs_service())
        self.assertFalse(car2.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 3)
        car = CarFactory.create_calliope(today, last_service_date, 0, 0)
        car2 = CarFactory.create_glissade(today, last_service_date, 0, 0)
        car3 = CarFactory.create_palindrome(today, last_service_date, False)

        self.assertTrue(car.needs_service())
        self.assertTrue(car2.needs_service())
        self.assertTrue(car3.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 1)
        car = CarFactory.create_calliope(today, last_service_date, 0, 0)
        car2 = CarFactory.create_glissade(today, last_service_date, 0, 0)
        car3 = CarFactory.create_palindrome(today, last_service_date, False)

        self.assertFalse(car.needs_service())
        self.assertFalse(car2.needs_service())
        self.assertFalse(car3.needs_service())      

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, today, current_mileage, last_service_mileage)
        car2 = CarFactory.create_thovex(today, today, current_mileage, last_service_mileage)

        self.assertTrue(car.needs_service())
        self.assertTrue(car2.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, today, current_mileage, last_service_mileage)
        car2 = CarFactory.create_thovex(today, today, current_mileage, last_service_mileage)

        self.assertFalse(car.needs_service())
        self.assertFalse(car2.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, today, current_mileage, last_service_mileage)
        car2 = CarFactory.create_rorschach(today, today, current_mileage, last_service_mileage)

        self.assertTrue(car.needs_service())
        self.assertTrue(car2.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, today, current_mileage, last_service_mileage)
        car2 = CarFactory.create_rorschach(today, today, current_mileage, last_service_mileage)

        self.assertFalse(car.needs_service())
        self.assertFalse(car2.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_palindrome(today, today, True)

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_palindrome(today, today, False)

        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
