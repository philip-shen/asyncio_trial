from Server import Google, BASE_URL, BASE_URL_AU

def test_homepage():
    google = Google(base_url=BASE_URL)
    google.homepage()

def test_error():
    #google = Google(base_url="NON_EXISTENT_URL")
    #google.bad_page()
    google = Google(base_url=BASE_URL_AU)
    google.homepage()

test_homepage()
test_error()