"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:

    def getImportance(self, employees: List['Employee'], id: int) -> int:

        emp_idx = 0
        for idx in range(len(employees)):
            if employees[idx].id == id:
                emp_idx = idx

        tot_imp = []

        def impFinder(idx):
            curr = employees[idx]
            tot_imp.append(curr.importance)

            for sub_id in curr.subordinates:
                for idx in range(len(employees)):
                    if employees[idx].id == sub_id:
                        impFinder(idx)

        impFinder(emp_idx)

        value = 0
        for imp in tot_imp:
            value += imp

        return value
