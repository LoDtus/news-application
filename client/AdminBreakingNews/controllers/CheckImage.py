import requests

def CheckImage(url):
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
    if not url.lower().endswith(valid_extensions):
        return False

    try:
        response = requests.head(url, allow_redirects=True)
        content_type = response.headers.get('Content-Type')
        if content_type and content_type.startswith('image'):
            return True
    except requests.RequestException:
        return False

    return False