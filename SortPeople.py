class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        sorted_people = sorted(zip(heights, names), reverse=True)
        return [name for _, name in sorted_people]