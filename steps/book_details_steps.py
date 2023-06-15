from behave import given, when, then
from utils.assertions import assert_equal
from models.book import Book
from apis.book_api import BookAPI


@given('I have a book ID "{book_id}"')
def step_given_book_id(context, book_id):
    context.book_id = book_id


@when('I request the book details')
def step_when_request_book_details(context):
    book_api = BookAPI(context.base_url)
    context.response = book_api.get_book_details(context.book_id)


@then('the response status code should be 200')
def step_then_response_status_code(context):
    assert_equal(context.response.status_code, 200)


@then('the response should contain the following book details:')
def step_then_response_contains_book_details(context):
    book_data = context.response.json()
    expected_book = Book(title=context.table[0]['title'], author=context.table[0]['author'],
                         category=context.table[0]['category'], price=context.table[0]['price'])
    actual_book = BookAPI.extract_book_details(book_data)
    assert_equal(actual_book, expected_book)

