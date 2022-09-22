import unittest

import main


class TestKingsMovement(unittest.TestCase):
    def test_horizontal(self):

        current_pos = "d4"
        valid_pos = ["c3", "d3", "e3", "c4", "e4", "c5", "d5", "e5"]

        for l in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            for n in range(1, 9):
                pos = l + str(n)
                self.assertEqual(pos in valid_pos and not main.canMove("king", current_pos, pos, output_board=False), False)

                self.assertEqual(pos not in valid_pos and main.canMove("king", current_pos, pos, output_board=False), False)
