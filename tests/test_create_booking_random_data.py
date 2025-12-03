import allure
from pydantic import ValidationError
from core.models.booking import BookingResponse

@allure.feature('Booking creation')
@allure.title('Test create booking with random data')

def test_create_booking_random_data(api_client, generate_random_booking_data):
    with allure.step("Create booking with random data"):
        booking_data = generate_random_booking_data
        response = api_client.create_booking(booking_data)
        try:
            BookingResponse(**response)
        except ValidationError as e:
            raise ValidationError(f"Response validation failed: {e}")

        actual = response["booking"]

        assert actual.items() >= booking_data.items()
        assert actual["bookingdates"].items() >= booking_data["bookingdates"].items()
        print("")
