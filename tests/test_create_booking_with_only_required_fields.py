import allure
import pytest
from requests.exceptions import HTTPError

@allure.feature('Booking creation')
@allure.title('Test create booking with only required fields')

def test_create_booking_without_required_fields(api_client):
    with allure.step('Create booking'):
        booking_data = {
            "additionalneeds": "blablabla"
        }
        with pytest.raises(HTTPError) as e:
            api_client.create_booking(booking_data)

        with allure.step('Assert code 500'):
            assert e.value.response.status_code == 500