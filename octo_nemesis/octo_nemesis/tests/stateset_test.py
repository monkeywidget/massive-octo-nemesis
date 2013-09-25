from django.test import TestCase
from octo_nemesis.models.stateset_model import StateSet

from django.test import Client  # for view tests

class StateSetTest(TestCase):
    
    # test 
    RGB_SET_DESCRIPTION = "the three primary colors"

    def setUp(self):
        # Every view test needs a client.
        self.client = Client()


    # model lifecycle

    def test_creates_with_parameters(self):
        
        StateSet.objects.create(name="RGB", 
                                description=StateSetTest.RGB_SET_DESCRIPTION, 
                                states_wrap=True)

        rgb_states = StateSet.objects.get(name="RGB")
        self.assertEqual(rgb_states.description, StateSetTest.RGB_SET_DESCRIPTION)
        self.assertTrue(rgb_states.states_wrap)

        
    def test_create_defaults_to_a_missing_param_name (self):
        StateSet.objects.create(description=StateSetTest.RGB_SET_DESCRIPTION)
        rgb_states = StateSet.objects.get(description=StateSetTest.RGB_SET_DESCRIPTION)
        self.assertEqual(rgb_states.name, "DefaultStateSet")

    def test_create_defaults_to_a_missing_param_states_wrap (self):
        StateSet.objects.create(description=StateSetTest.RGB_SET_DESCRIPTION)
        rgb_states = StateSet.objects.get(description=StateSetTest.RGB_SET_DESCRIPTION)
        self.assertFalse(rgb_states.states_wrap)

    # view and routing tests
    
    def test_stateset_renders_as_json (self):

        # clear the table 
        StateSet.objects.all().delete()
        # create single object
        StateSet.objects.create(description=StateSetTest.RGB_SET_DESCRIPTION)        

        response = self.client.get('/statesets/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


        # verify the content for the single object (fails)
        # TODO: parse the JSON and verify the fields (except for ID)
        self.assertEqual(response.content,
                         '[{"id": 1, "name": "DefaultStateSet", ' \
                         '"description": "the three primary colors", ' \
                         '"states_wrap": false}]'
                         )
        
if __name__ == '__main__':
    unittest.main()    