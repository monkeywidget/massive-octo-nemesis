Data Schema Notes
=================

- Each puzzle is a rectangular grid
- Each "state" of a button is represented by a unique color
- Each state has an implicit order relative to other states


API Models
==========

Event (in incoming API call request)
------------------------------------

- In: 
   - session id
   - Acting button coordinates

Board (in outgoing API response)
--------------------------------

- a 2D grid of the current colors


Application Models
==================

Board Session
-------------

- current state (Board)
   - edited frequently
- winning state (Board)
   - rarely edited
- associated with
   - a set of Rules
   - a State Set

Board
------

- max coordinates (x,y)
- current States in a single string (Varchar)

State Set
---------

- name
- description
- whether states wrap or end

State
-----

- (belongs to a State Set)
- name  (1 character)
- state index (defines an order)
- Color (rrggbb format, each field a 2-digit hexidecimal)


Rules
-----

See "Rule Schema" in RulesNotes.md

