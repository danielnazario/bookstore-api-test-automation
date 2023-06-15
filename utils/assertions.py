
def assert_equal(actual, expected):
    assert actual == expected, f"Expected: {expected}, but got: {actual}"


def assert_in(item, container):
    assert item in container, f"Item: {item} not found in container"

def key_in_response(key, response_data):

    assert key in response_data, f"Key '{key}' not found in response data."

def is_list(data):

    assert isinstance(data, list), f"Expected list, got {type(data).__name__}."

def list_not_empty(data):

    assert len(data) > 0, "List is empty."