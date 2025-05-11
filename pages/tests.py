from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        # Make a GET request to the homepage URL
        # This line uses Django's test client to simulate a GET request to the '/' URL path,
        # which corresponds to our homepage as defined in pages/urls.py
        # The client.get() method returns a response object that contains all the data returned by the view
        response = self.client.get('/')
        
        # Assert that the response status code is 200 (OK)
        # This line checks if the HTTP status code of the response is 200, which means the page loaded successfully
        # assertEqual() is a testing method that verifies the first argument equals the second argument
        # If the status code is not 200, the test will fail, indicating a problem with the homepage
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    
    
     
