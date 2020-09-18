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
        result = len(self.education_plan.entries)
        self.assertEqual(expectedLength, result)


if __name__ == '__main__':
    unittest.main()
