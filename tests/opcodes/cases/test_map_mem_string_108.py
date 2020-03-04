from unittest import TestCase

from tests import abspath

from pytezos.repl.interpreter import Interpreter
from pytezos.michelson.converter import michelson_to_micheline
from pytezos.repl.parser import parse_expression


class OpcodeTestmap_mem_string_108(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.i = Interpreter(debug=True)
        
    def test_opcode_map_mem_string_108(self):
        res = self.i.execute(f'INCLUDE "{abspath("opcodes/contracts/map_mem_string.tz")}"')
        self.assertTrue(res['success'])
        
        res = self.i.execute('RUN "bar" (Pair { Elt "bar" 4 ; Elt "foo" 11 } None)')
        self.assertTrue(res['success'])
        
        expected_expr = michelson_to_micheline('(Pair { Elt "bar" 4 ; Elt "foo" 11 } (Some True))')
        expected_val = parse_expression(expected_expr, res['result'][1].type_expr)
        self.assertEqual(expected_val, res['result'][1]._val)