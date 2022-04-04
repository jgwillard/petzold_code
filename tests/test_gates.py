import unittest

from gates import And, Nand, Nor, Not, Or, Xor


class TestLogicGates(unittest.TestCase):
    def setUp(self):
        pass

    def test_not(self):
        test_inverter = Not("test_inverter")
        test_inverter.input.val = 1
        self.assertEqual(test_inverter.output.val, 0, "!1 = 0")
        test_inverter.input.val = 0
        self.assertEqual(test_inverter.output.val, 1, "!0 = 1")

    def test_and(self):
        test_and_gate = And("test_and_gate")
        test_and_gate.input_a.val = 1
        test_and_gate.input_b.val = 1
        self.assertEqual(test_and_gate.output.val, 1, "1 x 1 = 1")
        test_and_gate.input_a.val = 0
        self.assertEqual(test_and_gate.output.val, 0, "0 x 1 = 0")
        test_and_gate.input_b.val = 0
        self.assertEqual(test_and_gate.output.val, 0, "0 x 0 = 0")
        test_and_gate.input_a.val = 1
        self.assertEqual(test_and_gate.output.val, 0, "1 x 0 = 0")

    def test_or(self):
        test_or_gate = Or("test_or_gate")
        test_or_gate.input_a.val = 1
        test_or_gate.input_b.val = 1
        self.assertEqual(test_or_gate.output.val, 1, "1 + 1 = 1")
        test_or_gate.input_a.val = 0
        self.assertEqual(test_or_gate.output.val, 1, "0 + 1 = 1")
        test_or_gate.input_b.val = 0
        self.assertEqual(test_or_gate.output.val, 0, "0 + 0 = 0")
        test_or_gate.input_a.val = 1
        self.assertEqual(test_or_gate.output.val, 1, "1 + 0 = 1")

    def test_nand(self):
        test_nand_gate = Nand("test_nand_gate")
        test_nand_gate.input_a.val = 1
        test_nand_gate.input_b.val = 1
        self.assertEqual(test_nand_gate.output.val, 0, "!(1 x 1) = 0")
        test_nand_gate.input_a.val = 0
        self.assertEqual(test_nand_gate.output.val, 1, "!(0 x 1) = 1")
        test_nand_gate.input_b.val = 0
        self.assertEqual(test_nand_gate.output.val, 1, "!(0 x 0) = 1")
        test_nand_gate.input_a.val = 1
        self.assertEqual(test_nand_gate.output.val, 1, "!(1 x 0) = 1")

    def test_nor(self):
        test_nor_gate = Nor("test_nor_gate")
        test_nor_gate.input_a.val = 1
        test_nor_gate.input_b.val = 1
        self.assertEqual(test_nor_gate.output.val, 0, "!(1 + 1) = 0")
        test_nor_gate.input_a.val = 0
        self.assertEqual(test_nor_gate.output.val, 0, "!(0 + 1) = 0")
        test_nor_gate.input_b.val = 0
        self.assertEqual(test_nor_gate.output.val, 1, "!(0 + 0) = 1")
        test_nor_gate.input_a.val = 1
        self.assertEqual(test_nor_gate.output.val, 0, "!(1 + 0) = 0")

    def test_xor(self):
        test_xor_gate = Xor("test_xor_gate")
        self.assertEqual(test_xor_gate.output.val, 0, "(0 + 0) * (!0 + !0) = 0")
        test_xor_gate.input_a.val = 1
        self.assertEqual(test_xor_gate.output.val, 1, "(0 + 1) * (!0 + !1) = 1")
        test_xor_gate.input_b.val = 1
        self.assertEqual(test_xor_gate.output.val, 0, "(1 + 1) * (!1 + !1) = 0")
        test_xor_gate.input_a.val = 0
        self.assertEqual(test_xor_gate.output.val, 1, "(0 + 1) * (!0 + !1) = 1")
        test_xor_gate.input_b.val = 0
        self.assertEqual(test_xor_gate.output.val, 0, "(0 + 0) * (!0 + !0) = 0")
        test_xor_gate.input_a.val = 1
        self.assertEqual(test_xor_gate.output.val, 1, "(1 + 0) * (!1 + !0) = 1")