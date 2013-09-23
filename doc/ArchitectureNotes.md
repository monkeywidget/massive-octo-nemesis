Architecture Notes
==================

- API: JSON
- objects: RESTful django 
   - http://django-rest-framework.org
   - JSON transport 
- running against PostgreSQL


Clients
=======

Text Client
-----------

Web Client
----------

REST browser:
- rename / recolor REST browser theme:
   - http://django-rest-framework.org/topics/browsable-api.html 


Hardware/USB client
-------------------

Proposed:
- USB button pad is a monome-compatible
- USB driver etc is backed by Arduino
- Arduino connects to a Raspberry Pi, which is running the DB and app server


REST API
=========

See the SchemaNotes.md


StateSet
--------

State
-----

Under a StateSet

BoardSession
------------

Button
------

Under a BoardSession


Rule
----




API for App Client
==================

- new game
   - returns board session key
- fetch current board state for this session
   - returns board session key
   - returns grid of colors
- given this button press on this session, what is the new board state?
   - returns board session key
   - returns grid of colors
   - returns if the game has been won now


Utility Clients
===============

- Utility: Load puzzle from file
- curl !