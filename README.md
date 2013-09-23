massive-octo-nemesis
====================

Interface, REST and Rules Engine for a Turing-complete "Lights Out"

The What Now?
-------------

"Lights Out" was a puzzle released by Tiger Electronics / Tiger Toys in 1995.

This is like that ... except much, much crazier.  

Also it runs on the Monome 40h interface, or more appropriately the Arduinome RGB (8x8).


Why is it named such a ridiculous thing?
----------------------------------------
  
Well, believe it or not, "massive-octo-nemesis" was the randomly-generated string 
suggested by GitHub.

Since one of my favorite movies is "I WORK FOR NEMESIS," I decided to keep it. 


What Is This Built With?
------------------------

What technology will you have to know to hack into this thing?

- back end
  - django (python)
  - JSON
  - PostgreSQL 
- web front end  
  - jQuery


Install (dev environment)
=========================



How To
======


Run the server
--------------
   
    python manage.py runserver

Run the tests
-------------

    python manage.py test octo_nemesis.tests

Example basic queries
=====================

StateSets
---------

List all:
    curl http://127.0.0.1:8000/stateset/

List one:
    curl http://127.0.0.1:8000/stateset/2/
    
Create new:
    curl -X POST http://127.0.0.1:8000/statesets/ -d title="The cat in the hat" -d description="a Dr Seuss thing" -d states_wrap="false"

browser: visit:
	http://127.0.0.1:8000/statesets/?format=json
	http://127.0.0.1:8000/statesets/
