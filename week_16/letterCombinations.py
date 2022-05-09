class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        parents = [""]

        final = []
        dicti = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        children = []
        for index, digit in enumerate(digits):
            concats = dicti[digit]
            # do sth
            for concat in concats:
                for parent in parents:
                    children.append(parent + concat)
            # ends
            parents = children
            children = []
        return parents if parents[0] != "" else []