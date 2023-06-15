from behave import when, then,given
from utils.assertions import assert_equal
from apis.book_api import BookAPI

@given('I have a book search query "{query}"')
def step_given_book_search_query(context, query):
    context.query = query

@given('I have a category search query "{query}"')
def step_given_category_search_query(context, query):
    context.query = query

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