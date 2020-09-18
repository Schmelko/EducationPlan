from education_plan_entry import EducationPlanEntry

class EducationPlan:

    def __init__(self, lines):
        self.entries = []
        for index in range(0, len(lines), 4):
            self.entries.append(EducationPlanEntry(
                lines[index].strip('\n'),
                lines[index+1].strip('\n'),
                lines[index+2].strip('\n'),
                lines[index+3].strip('\n')))