import allure
from pydantic import ValidationError
from core.models.booking import BookingResponse

@allure.feature('Booking creation')
@allure.title('Test create booking without required fields')

def test_create_booking_with_only_required_fields(api_client):
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
        }
        response = api_client.create_booking(booking_data)
        try:
            BookingResponse(**response)
        except ValidationError as e:
            raise ValidationError(f"Response validation failed: {e}")

        expected = booking_data
        actual = response["booking"]

        assert actual.items() >= expected.items()
        assert actual["bookingdates"].items() >= expected["bookingdates"].items()
