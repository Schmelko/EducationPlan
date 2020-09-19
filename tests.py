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

    def test_task4(self):
        teacher_name = 'Albatrosz Aladin'
        expected = 24
        result = self.education_plan.number_of_lessons_per_week_by_teacher(teacher_name)
        self.assertEqual(expected, result)

    def test_task5(self):        
        expected = {
            '12.b': 'Pulyka Pozsinka',
            '12.c': 'Vidra Viktor',
            '12.d': 'Puma Pongor'
        }
        results = {class_name:self.education_plan.head_teacher_by_class(class_name) for class_name in expected.keys()}
        self.assertDictEqual(expected, results)

if __name__ == '__main__':
    unittest.main()
