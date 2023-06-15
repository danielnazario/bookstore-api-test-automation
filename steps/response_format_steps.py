from behave import given, when, then
from utils.assertions import assert_equal
from apis.book_api import BookAPI
from apis.category_api import CategoryAPI


@given('I have a book search query "{query}"')
def step_given_book_search_query(context, query):
    context.query = query

@when('I search for books')
def step_when_search_for_books(context):
    book_api = BookAPI(context.base_url)
    context.response = book_api.search_books(context.query)

@when('I request the category details')
def step_when_request_category_details(context):
    category_api = CategoryAPI(context.base_url)
    context.response = category_api.get_category_details(context.category_id)

@then('the response should have the correct format for book search')
def step_then_response_has_correct_book_search_format(context):
    response_data = context.response.json()
    assert_equal(response_data['status'], 'success')
    assert_equal(response_data['total_results'], 10)
    assert 'books' in response_data
    assert isinstance(response_data['books'], list)
    assert all(isinstance(book, dict) for book in response_data['books'])

@then('the response should have the correct format for category details')
def step_then_response_has_correct_category_format(context):
    response_data = context.response.json()
    assert_equal(response_data['status'], 'success')
    assert 'category' in response_data
    assert isinstance(response_data['category'], dict)
    assert 'name' in response_data['category']
    assert 'id' in response_data['category']