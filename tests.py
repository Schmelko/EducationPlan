import unittest
from education_plan_entry import EducationPlanEntry
from education_plan import EducationPlan

class TestsForEducationPlan(unittest.TestCase):

    def setUp(self):
        with open('beosztas.txt') as stream:
            lines = stream.readlines()
        
        self.education_plan = EducationPlan(lines)

    def test_task1(self):
        expectedLength = 329
        result = len(self.education_plan._entries)
        self.assertEqual(expectedLength, result)

    def test_task2(self):
        expectedLength = 329
        result = self.education_plan.number_of_entries()
        self.assertEqual(expectedLength, result)

    def test_task3(self):
        expected = 1016
        result = self.education_plan.number_of_lessons_per_week()
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
