import unittest
from datetime import datetime
from car_factory import CarFactory
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 5)
        self.assertTrue(NubbinBattery(last_service_date, today).needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 3)
        self.assertFalse(NubbinBattery(last_service_date, today).needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 4)
        self.assertTrue(SpindlerBattery(last_service_date, today).needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 2)
        self.assertFalse(SpindlerBattery(last_service_date, today).needs_service())

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        self.assertTrue(CapuletEngine(last_service_mileage, current_mileage).needs_service())
    
    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        self.assertFalse(CapuletEngine(last_service_mileage, current_mileage).needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        self.assertTrue(WilloughbyEngine(last_service_mileage, current_mileage).needs_service())
    
    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        self.assertFalse(WilloughbyEngine(last_service_mileage, current_mileage).needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
         self.assertTrue(SternmanEngine(True).needs_service())
    
    def test_engine_should_not_be_serviced(self):
        self.assertFalse(SternmanEngine(False).needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_array = [0.8, 1, 0.4, 0.88]
        self.assertTrue(OctoprimeTires(tire_array).needs_service())
    
    def test_tires_should_not_be_serviced(self):
        tire_array = [0.3, 0.3, 0.8, 1]
        self.assertFalse(OctoprimeTires(tire_array).needs_service())

class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_array = [0, 1, 0.4, 0.88]
        self.assertTrue(CarriganTires(tire_array).needs_service())
    
    def test_tires_should_not_be_serviced(self):
        tire_array = [0.56, 0.7, 0.89, 0.88]
        self.assertFalse(CarriganTires(tire_array).needs_service())

class TestNubbinBatteryInCar(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 5)
        car = CarFactory.create_rorschach(today, last_service_date, 0, 0, [0,0,0,0])
        car2 = CarFactory.create_thovex(today, last_service_date, 0, 0, [0,0,0,0])

        self.assertTrue(car.needs_service())
        self.assertTrue(car2.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 3)
        car = CarFactory.create_rorschach(today, last_service_date, 0, 0, [0,0,0,0])
        car2 = CarFactory.create_thovex(today, last_service_date, 0, 0, [0,0,0,0])

        self.assertFalse(car.needs_service())
        self.assertFalse(car2.needs_service())

class TestSpindlerBatteryInCar(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 4)
        car = CarFactory.create_calliope(today, last_service_date, 0, 0, [0,0,0,0])
        car2 = CarFactory.create_glissade(today, last_service_date, 0, 0, [0,0,0,0])
        car3 = CarFactory.create_palindrome(today, last_service_date, False, [0,0,0,0])

        self.assertTrue(car.needs_service())
        self.assertTrue(car2.needs_service())
        self.assertTrue(car3.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year - 2)
        car = CarFactory.create_calliope(today, last_service_date, 0, 0, [0,0,0,0])
        car2 = CarFactory.create_glissade(today, last_service_date, 0, 0, [0,0,0,0])
        car3 = CarFactory.create_palindrome(today, last_service_date, False, [0,0,0,0])

        self.assertFalse(car.needs_service())
        self.assertFalse(car2.needs_service())
        self.assertFalse(car3.needs_service())      

class TestCapuletEngineInCar(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, today, current_mileage, last_service_mileage, [0,0,0,0])
        car2 = CarFactory.create_thovex(today, today, current_mileage, last_service_mileage, [0,0,0,0])

        self.assertTrue(car.needs_service())
        self.assertTrue(car2.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, today, current_mileage, last_service_mileage, [0,0,0,0])
        car2 = CarFactory.create_thovex(today, today, current_mileage, last_service_mileage, [0,0,0,0])

        self.assertFalse(car.needs_service())
        self.assertFalse(car2.needs_service())

class TestWilloughbyEngineInCar(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, today, current_mileage, last_service_mileage, [0,0,0,0])
        car2 = CarFactory.create_rorschach(today, today, current_mileage, last_service_mileage, [0,0,0,0])

        self.assertTrue(car.needs_service())
        self.assertTrue(car2.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, today, current_mileage, last_service_mileage, [0,0,0,0])
        car2 = CarFactory.create_rorschach(today, today, current_mileage, last_service_mileage, [0,0,0,0])

        self.assertFalse(car.needs_service())
        self.assertFalse(car2.needs_service())

class TestSternmanEngineInCar(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_palindrome(today, today, True, [0,0,0,0])

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_palindrome(today, today, False, [0,0,0,0])

        self.assertFalse(car.needs_service())

class TestOctoprimeTiresInCar(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_rorschach(today, today, 0, 0, [0.8, 1, 0.4, 0.88])
        car2 = CarFactory.create_thovex(today, today, 0, 0, [0.8, 1, 0.4, 0.88])

        self.assertTrue(car.needs_service())
        self.assertTrue(car2.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_rorschach(today, today, 0, 0, [0.3, 0.3, 0.8, 1])
        car2 = CarFactory.create_thovex(today, today, 0, 0, [0.3, 0.3, 0.8, 1])

        self.assertFalse(car.needs_service())
        self.assertFalse(car2.needs_service())    

class TestCarriganTiresInCar(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_calliope(today, today, 0, 0, [0, 1, 0.4, 0.88])
        car2 = CarFactory.create_glissade(today, today, 0, 0, [0, 1, 0.4, 0.88])
        car3 = CarFactory.create_palindrome(today, today, False, [0, 1, 0.4, 0.88])

        self.assertTrue(car.needs_service())
        self.assertTrue(car2.needs_service())
        self.assertTrue(car3.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        car = CarFactory.create_calliope(today, today, 0, 0, [0.56, 0.7, 0.89, 0.88])
        car2 = CarFactory.create_glissade(today, today, 0, 0, [0.56, 0.7, 0.89, 0.88])
        car3 = CarFactory.create_palindrome(today, today, False, [0.56, 0.7, 0.89, 0.88])

        self.assertFalse(car.needs_service())
        self.assertFalse(car2.needs_service())
        self.assertFalse(car3.needs_service()) 

if __name__ == '__main__':
    unittest.main()
