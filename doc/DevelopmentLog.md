Development Log
===============
At https://github.com/monkeywidget/massive-octo-nemesis


Backlog (Implement Later)
=========================

- test data loader

- add State representation to StateSet view/serializer
- add Board representation to BoardSession detail view/serializer
- models for
   - StateSet
   - State under a StateSet
   - Board
   - BoardSession

- implement text client on game API
- implement dummy game API (non-REST)
   - http://django-rest-framework.org/tutorial/2-requests-and-responses.html
   - @api_view , APIView

- complete rules model (AND/OR on ACTEE)

- basic view / REST for State

Current To-Do (Implement Next)
==============================

- model for State (each belongs to StateSet)
- tests for State

- tests for StateSet (model)
   - https://factoryboy.readthedocs.org/en/latest/
- tests for StateSet (view)
   - TestClient: https://docs.djangoproject.com/en/dev/topics/testing/overview/

Committed (with commit numbers)
===============================

commit 
-----------------------------------------------

- hardware notes

commit 94145d3bde2d28ad5475767b2ea0fe832e9372cf
-----------------------------------------------

- get one unit test running
   - http://greaterdebater.com/blog/gabe/post/12
   - http://toastdriven.com/blog/2011/apr/10/guide-to-testing-in-django/

commit c8b49bc97a5a0d942f7e65900316e0725b56eecf 
-----------------------------------------------

- basic REST design
- refactor StateSet view to use class-based view
   - http://django-rest-framework.org/tutorial/3-class-based-views.html
- re-enable json with a new mixin
- new views.mixins package

commit 79f5508d9acc80544cefb31d85271044fb579f1c
-----------------------------------------------

- refactor to break out model (made "models" a package)

commit a020d83b60605aff5ccda0b7802f3fc76f1a8462
-----------------------------------------------

- refactor out JSONResponse
   - http://django-rest-framework.org/tutorial/2-requests-and-responses.html
- get one RESTful model running (StateSet)

Test:
- curl http://127.0.0.1:8000/statesets/2
- curl http://127.0.0.1:8000/statesets/
- curl -X POST http://127.0.0.1:8000/statesets/ -d title="The cat in the hat" -d description="a Dr Seuss thing" -d states_wrap="false"


commit 3a315f333fdde166e6bb4122678fa5d7a77d20a6
-----------------------------------------------

- working view for stateset: SHOW, LIST
- refactored views into separate files (views is a package now, not a module)
Reading:
- http://django-rest-framework.org/tutorial/2-requests-and-responses.html


commit e00923ec54ac86bcd84f0325bf0229570bdb9691
-----------------------------------------------

- StateSet serializer
   - initially, only own data
   - not using REST yet (running through tutorial)
- created StateSet model
   - python manage.py syncdb
- PostgreSQL
   - pip install psycopg2
   - set up DB:
      - createuser octonemesis
      - createdb -O octonemesis octonemesis
      - ALTER USER octonemesis WITH PASSWORD 'start123';
      - GRANT ALL PRIVILEGES ON DATABASE octonemesis TO octonemesis;

Reading:
- http://django-rest-framework.org/tutorial/1-serialization.html
- http://django-rest-framework.org/#tutorial

test:
>>> from octo_nemesis.models import StateSet
>>> from octo_nemesis.serializers import StateSetSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> stateset = StateSet(name="cool state set!", description="Twas brillig, and the slithy toves etc", states_wrap=False)
>>> stateset.save()
>>> stateset = StateSet(name="Beowulf Set", description="Hwast!!", states_wrap=True)
>>> serializer = StateSetSerializer(stateset)
>>> serializer.data
{u'id': 4, 'name': u'Beowulf Set', 'description': u'Hwast!!', 'states_wrap': True}
>>> content = JSONRenderer().render(serializer.data)
>>> content
'{"id": 4, "name": "Beowulf Set", "description": "Hwast!!", "states_wrap": true}'

>>> import StringIO
>>> stream = StringIO.StringIO(content)
>>> data = JSONParser().parse(stream)
>>> serializer = StateSetSerializer(data=data)
>>> serializer.is_valid()
True
>>> serializer.object
<StateSet: StateSet object>


>>> serializer = StateSetSerializer(StateSet.objects.all(), many=True)
>>> serializer.data
[{u'id': 2, 'name': u'Beowulf Set', 'description': u'Hwast!!', 'states_wrap': True}, {u'id': 4, 'name': u'Beowulf Set', 'description': u'Hwast!!', 'states_wrap': True}, {u'id': 1, 'name': u'cool state set!', 'description': u'Twas brillig, and the slithy toves etc', 'states_wrap': False}, {u'id': 3, 'name': u'cool state set!', 'description': u'Twas brillig, and the slithy toves etc', 'states_wrap': False}]



commit 694112293bd73f7fdf48a8f93868d7f0113976d0
-----------------------------------------------
- write business logic stories for models for rules
- design basic (non-rule) models for runtime
- write stories for hardware game
- basic API design
