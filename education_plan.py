from education_plan_entry import EducationPlanEntry

class EducationPlan:

    def __init__(self, lines):
        self._entries = []
        for index in range(0, len(lines), 4):
            self._entries.append(EducationPlanEntry(
                lines[index].strip('\n'),
                lines[index+1].strip('\n'),
                lines[index+2].strip('\n'),
                lines[index+3].strip('\n')))
    
    def number_of_entries(self):
        return len(self._entries)
    
    def number_of_lessons_per_week(self):
        return sum(entry.hours_per_week for entry in self._entries)

    def number_of_lessons_per_week_by_teacher(self, teacher_name):
        return sum(entry.hours_per_week for entry in self._entries if entry.teacher_name == teacher_name)

    def head_teacher_by_class(self, class_name):
        for entry in self._entries:
            if entry.class_name == class_name and entry.subject == 'osztalyfonoki':
                return entry.teacher_name

    def is_subject_learnt_in_groups(self, class_name, subject):
        return len(tuple(entry for entry in self._entries if entry.class_name == class_name and entry.subject == subject)) > 1
