import unittest
import pyunit

class TestRockPaperScissors(unittest.TestCase):
    # Test 1: The user wins if the user has "rock" and the program has "scissors
    def test_user_wins_rock_vs_scissors(self):
        self.assertEqual(pyunit.calculate_winner("rock", "scissors"), "user")

    # Test 2: The program wins if the user has "rock" and the program has "paper"
    def test_program_wins_rock_vs_paper(self):
        self.assertEqual(pyunit.calculate_winner("rock", "paper"), "program")




if __name__ == "__main__":
    unittest.main()