from rest_framework.views import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestTemperatureStats(APITestCase):

    def setUp(self) -> None:
        self.city = "New York"
        self.url = reverse('city-temperatures', kwargs={"city": self.city})
        self.days = dict({'days': 7})

    def test_successful_fetch_data_from_weather_api(self) -> None:
        response = self.client.get(self.url, self.days)
        data = response.data
        self.assertIn('minimum', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unsuccessful_fetch_data_if_days_more_than_10(self) -> None:
        self.days["days"] = 1000
        response = self.client.get(self.url, self.days)
        data = response.data
        self.assertNotIn('minimum', data)
        self.assertEqual(data['days'][0].title(),
                         '1000 Must Be Between 1 And 10')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unsuccessful_fetch_data_if_days_not_provided(self) -> None:
        self.days["days"] = ""
        response = self.client.get(self.url, self.days)
        data = response.data
        self.assertNotIn('minimum', data)
        self.assertEqual(data['days'][0].title(),
                         'This Field May Not Be Blank.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unsuccessful_fetch_data_if_days_is_a_string(self) -> None:
        self.days["days"] = "Two"
        response = self.client.get(self.url, self.days)
        data = response.data
        self.assertNotIn('minimum', data)
        self.assertEqual(data['days'][0].title(),
                         'Two Must Be An Integer')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unsuccessful_fetch_data_if_city_name_contains_special_characters(self) -> None:
        self.url = reverse('city-temperatures', kwargs={"city": "Nairobi@"})
        response = self.client.get(self.url, self.days)
        data = response.data
        self.assertNotIn('minimum', data)
        self.assertEqual(data['city'][0].title(),
                         'Nairobi@ Cannot Contain Special Characters')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unsuccessful_fetch_data_if_city_name_is_not_valid(self) -> None:
        self.url = reverse('city-temperatures', kwargs={"city": "Nairobiwer"})
        response = self.client.get(self.url, self.days)
        data = response.data
        self.assertNotIn('minimum', data)
        self.assertEqual(data['error'].title(),
                         'No Matching Location Found.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
