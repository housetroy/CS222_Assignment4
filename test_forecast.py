import unittest 
from forecast import get_forecast_data, get_forecast_url

class TestForecast(unittest.TestCase):

    def test_forecast_url_ocntains_gridpoints(self):
        url = get_forecast_url()
        self.assertIn("https://api.weather.gov/gridpoints", url)

    def test_forecast_has_14_periods(self):
        url = get_forecast_url()
        periods = get_forecast_data(url)
        self.assertEqual(len(periods), 14)

unittest.main()