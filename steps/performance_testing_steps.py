import time
from behave import given, when, then
from apis.book_api import BookAPI

@given('I have a list of concurrent requests')
def step_given_concurrent_requests(context):
    context.concurrent_requests = []

    # Create a list of concurrent requests to be executed
    for i in range(context.concurrent_users):
        book_api = BookAPI(context.base_url)
        request = book_api.get_book_details(context.book_id)
        context.concurrent_requests.append(request)

@when('I execute the concurrent requests')
def step_when_execute_concurrent_requests(context):
    start_time = time.time()

    for request in context.concurrent_requests:
        response = request.execute()

    elapsed_time = time.time() - start_time
    context.execution_time = elapsed_time

@then('the requests should complete within a certain time limit')
def step_then_requests_complete_within_time_limit(context):
    max_execution_time = context.max_execution_time
    assert context.execution_time <= max_execution_time, f"Execution time exceeded the limit. Expected: <= {max_execution_time}, Actual: {context.execution_time}"
