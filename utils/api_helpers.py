from urllib.parse import urljoin


def build_url(base_url, endpoint, params=None):
    url = urljoin(base_url, endpoint)
    if params:
        query_params = "&".join(f"{key}={value}" for key, value in params.items())
        url = f"{url}?{query_params}"
    return url
