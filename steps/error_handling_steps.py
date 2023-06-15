from behave import given, when, then
from utils.assertions import assert_equal
from apis.book_api import BookAPI
from apis.category_api import CategoryAPI

@given('I have an invalid book ID')
def step_given_invalid_book_id(context):
    context.book_id = "invalid_id"

@given('I have an invalid category ID')
def step_given_invalid_category_id(context):
    context.category_id = "invalid_id"

@when('I make a request with missing parameters')
def step_when_make_request_with_missing_parameters(context):
    book_api = BookAPI(context.base_url)
    context.response = book_api.get_book_details(context.book_id)  # Example of missing parameter

@when('I make a request with incorrect authentication')
def step_when_make_request_with_incorrect_authentication(context):
    book_api = BookAPI(context.base_url)
    context.response = book_api.get_book_details(context.book_id)  # Example of incorrect authentication

@then('the response status code should be {status_code:d}')
def step_then_response_status_code(context, status_code):
    assert_equal(context.response.status_code, status_code)

@then('the response should contain an appropriate error message')
def step_then_response_contains_error_message(context):
    response_data = context.response.json()
    assert 'error' in response_data
    assert 'message' in response_data['error']