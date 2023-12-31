
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BREAK CASE CATCH CHAR_CONSTANT COMMENT COMPARISON CONTINUE DEFAULT DIVIDE DO_WHILE ELSE ELSE_IF FLOAT FOR IDENTIFIER IF INTEGER KWORD LPAREN LSQUAREBRACKET MINUS MULTIPLY PLUS RETURN RPAREN RSQUAREBRACKET SEMICOLON SWITCH THROW TRY VOID WHILEexpression : KWORD expression KWORD expressionexpression : IDENTIFIERexpression : FLOATexpression : INTEGERexpression : expression MULTIPLY expression\n                    | expression DIVIDE  expression\n                    | expression PLUS expression\n                    | expression PLUS PLUS\n                    | expression MINUS expressionexpression  : expression COMPARISON  expressionexpression : IDENTIFIER ASSIGN expressionexpression : LPAREN expression RPARENexpression : CHAR_CONSTANTexpression : expression SEMICOLON expression'
    
_lr_action_items = {'KWORD':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,],[2,2,-2,-3,-4,2,-13,2,2,2,2,2,2,24,2,-5,-6,-7,-8,-9,-10,-14,2,-11,-12,-1,]),'IDENTIFIER':([0,2,6,8,9,10,11,12,13,15,24,],[3,3,3,3,3,3,3,3,3,3,3,]),'FLOAT':([0,2,6,8,9,10,11,12,13,15,24,],[4,4,4,4,4,4,4,4,4,4,4,]),'INTEGER':([0,2,6,8,9,10,11,12,13,15,24,],[5,5,5,5,5,5,5,5,5,5,5,]),'LPAREN':([0,2,6,8,9,10,11,12,13,15,24,],[6,6,6,6,6,6,6,6,6,6,6,]),'CHAR_CONSTANT':([0,2,6,8,9,10,11,12,13,15,24,],[7,7,7,7,7,7,7,7,7,7,7,]),'$end':([1,3,4,5,7,17,18,19,20,21,22,23,25,26,27,],[0,-2,-3,-4,-13,-5,-6,-7,-8,-9,-10,-14,-11,-12,-1,]),'MULTIPLY':([1,3,4,5,7,14,16,17,18,19,20,21,22,23,25,26,27,],[8,-2,-3,-4,-13,8,8,8,8,8,-8,8,8,8,8,-12,8,]),'DIVIDE':([1,3,4,5,7,14,16,17,18,19,20,21,22,23,25,26,27,],[9,-2,-3,-4,-13,9,9,9,9,9,-8,9,9,9,9,-12,9,]),'PLUS':([1,3,4,5,7,10,14,16,17,18,19,20,21,22,23,25,26,27,],[10,-2,-3,-4,-13,20,10,10,10,10,10,-8,10,10,10,10,-12,10,]),'MINUS':([1,3,4,5,7,14,16,17,18,19,20,21,22,23,25,26,27,],[11,-2,-3,-4,-13,11,11,11,11,11,-8,11,11,11,11,-12,11,]),'COMPARISON':([1,3,4,5,7,14,16,17,18,19,20,21,22,23,25,26,27,],[12,-2,-3,-4,-13,12,12,12,12,12,-8,12,12,12,12,-12,12,]),'SEMICOLON':([1,3,4,5,7,14,16,17,18,19,20,21,22,23,25,26,27,],[13,-2,-3,-4,-13,13,13,13,13,13,-8,13,13,13,13,-12,13,]),'RPAREN':([3,4,5,7,16,17,18,19,20,21,22,23,25,26,27,],[-2,-3,-4,-13,26,-5,-6,-7,-8,-9,-10,-14,-11,-12,-1,]),'ASSIGN':([3,],[15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,6,8,9,10,11,12,13,15,24,],[1,14,16,17,18,19,21,22,23,25,27,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> KWORD expression KWORD expression','expression',4,'p_expression_kword','analizator.py',104),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','analizator.py',108),
  ('expression -> FLOAT','expression',1,'p_expression_float','analizator.py',112),
  ('expression -> INTEGER','expression',1,'p_expression_integer','analizator.py',116),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_binary_operation','analizator.py',124),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binary_operation','analizator.py',125),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binary_operation','analizator.py',126),
  ('expression -> expression PLUS PLUS','expression',3,'p_expression_binary_operation','analizator.py',127),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binary_operation','analizator.py',128),
  ('expression -> expression COMPARISON expression','expression',3,'p_expression_comparison','analizator.py',137),
  ('expression -> IDENTIFIER ASSIGN expression','expression',3,'p_assignment','analizator.py',141),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_parentheses','analizator.py',145),
  ('expression -> CHAR_CONSTANT','expression',1,'p_char_constant','analizator.py',149),
  ('expression -> expression SEMICOLON expression','expression',3,'p_expression_semicolon','analizator.py',156),
]
