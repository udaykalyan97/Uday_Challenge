import unittest
import requests

#AWS webserver address
SERVER_URL = 'http:localhost:8080'

class TestWebServer(unittest.TestCase):

    def test_connection(self):
        # Test if the server is up and running
        response = requests.get(SERVER_URL)
        self.assertEqual(response.status_code, 200)

    def test_static_content(self):
        # Test static file requests
        static_files = ['/index.html', '/css/style.css', '/images/logo.png']
        for file in static_files:
            response = requests.get(SERVER_URL + file)
            self.assertEqual(response.status_code, 200)
            self.assertIn('text/html', response.headers.get('Content-Type'))

    def test_dynamic_content(self):
        # Test dynamic URL requests
        dynamic_urls = ['/products/1', '/user/profile']
        for url in dynamic_urls:
            response = requests.get(SERVER_URL + url)
            self.assertEqual(response.status_code, 200)
            # Add additional assertions based on the expected response from the server

    def test_post_data_processing(self):
        # Test POST data processing
        payload = {'username': 'test_user', 'password': 'test_password'}
        response = requests.post(SERVER_URL + '/login', data=payload)
        self.assertEqual(response.status_code, 200)
        # Add additional assertions based on the expected response from the server

    def test_error_handling(self):
        # Test error handling
        invalid_url = SERVER_URL + '/non_existent_page'
        response = requests.get(invalid_url)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
