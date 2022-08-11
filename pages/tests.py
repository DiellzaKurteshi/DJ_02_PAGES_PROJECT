from django.test import TestCase, SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('')
        return self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        res = self.client.get('about/')
        return self.assertEqual(res.status_code, 200)

    def test_contact_pagr(self):
        resp = self.client.get('contact/')
        return self.assertEqual(resp.status_code, 200)

        