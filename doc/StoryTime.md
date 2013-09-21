Story Time!!!
=============

Hardware stories
----------------

- The game can run on a device while not connected to a PC
   - possible solution: add a Raspberry Pi to the device to run the DB and server
- Response time for a button press is instantaneous
- The device sends button presses and requests new state from the server API

Software Architecture
---------------------

- The basic rules for "Lights Out" can be played in puzzles that appeared on the original
- A puzzle, can be loaded from a file with:
   - states definitions
   - state transition order
   - button rules (what happens when you click which buttons)
   - initial state of the puzzle to be solved
- A client can load the initial positions from an API
- A client can send a button press event and receive the new board state
- A client gets a notification when the puzzle has been solved

Development Experience
----------------------

- Developer can easily run the unit tests
- Developer can easily get code coverage figures

- Developer can easily erase and reload the database
- Developer can easily see the state of objects through a REST interface


Unaddressed Stories
-------------------

- CA: abstract Rule engine to enable Conway's "Life"
   - requires a "number of neighbors in state X" operator
- Turing: rule CRUD
 