from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        self.assertFalse(solution([212, 147, 103, 50, 46, 42]))
