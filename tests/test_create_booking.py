import allure
import pytest

@allure.feature('Booking creation')
@allure.title('Test create booking')

def test_create_booking(api_client):
    with allure.step('Create booking'):
        booking_data = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        response = api_client.create_booking(booking_data)
    with allure.step('Assert status code'):
        assert isinstance(response, dict)
        assert "bookingid" in response
        assert "booking" in response

