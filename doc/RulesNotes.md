Rules Notes
===========


Implementation Notes
====================

- on a click,
   - fetch only the rules that can apply given the Actor state
   - build button selector
      - evaluate against only buttons that may be effected


Rule
====

General Format
--------------

- ACTOR button A
   - any
   - in State X
- FOR_ACTEE buttons (selector has AND/OR)
   - all
   - only those in State Y
   - in a position relative to Actor A position
      - actor_self
      - next to (8 neighbors)
      - orthagonal to (4 neighbors)
      - kitty-corner to (4 neighbors)
      - same row
      - same column
      - at relative coordiates (x1,y1) 
- DO (can do multiple of:)
   - set to State S
   - advance State M steps
   - evaluate another Rule R1, R2, R3...Rn
   

Rules Stories
-------------

- Lights Out:
   - StateSet (states wrap)
      - State 0: #000000
      - State 1: #ffffff
   - ACTOR
      - any 
   - FOR_ACTEE 
      - actor_self
      - OR orthogonal to actor
   - DO
      - advance State 1 step


Rule Schema
-----------

Rule:
- id
- actor (-1 = ACTOR_ANY, other values are state_index)

Rule_Actee:
- TBD

Rule_Action:
- id
- rule_id (belongs to)
- rule_index (order to execute)
- do (SET_STATE, STATE_INCR, EVAL_RULE)
- do_param (int: state to set to, number or state steps to increment, or rule_id to run)

