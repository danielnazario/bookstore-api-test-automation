from behave import given, when, then
from utils import assertions
from apis.book_api import BookAPI
from apis.category_api import CategoryAPI

@given('I have a book search query "{query}"')
def step_given_book_search_query(context, query):
    context.query = query

@when('I search for books')
def step_when_search_for_books(context):
    book_api = BookAPI(context.base_url)
    context.response = book_api.search_books(context.query)

@when('I search for categories')
def step_when_search_for_categories(context):
    category_api = CategoryAPI(context.base_url)
    context.response = category_api.search_categories(context.query)

@then('the response should contain search results for books')
def step_then_response_contains_book_search_results(context):
    response_data = context.response.json()
    assertions.key_in_response('books', response_data)
    assertions.is_list(response_data['books'])
    assertions.list_not_empty(response_data['books'])

@then('the response should contain search results for categories')
def step_then_response_contains_category_search_results(context):
    response_data = context.response.json()
    assertions.key_in_response('categories', response_data)
    assertions.is_list(response_data['categories'])
    assertions.list_not_empty(response_data['categories'])
