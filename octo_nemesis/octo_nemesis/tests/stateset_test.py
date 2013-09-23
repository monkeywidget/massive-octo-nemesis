from django.test import TestCase

class StateSetTest(TestCase):

    def test_creates_with_parameters(self):
        self.assertTrue(False)
    
    def test_create_complains_on_missing_param_name (self):
        self.assertTrue(False)

    def test_create_complains_on_missing_param_description (self):
        self.assertTrue(False)

    def test_create_complains_on_missing_param_stateswrap (self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()    