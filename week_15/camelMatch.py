class Solution:

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        pattern_dict = {"END": False}
        workng = pattern_dict
        for letter in pattern:
            workng[letter] = {"END": False}
            workng = workng[letter]
            workng['END'] = True

        def search(word):
            # print("word is",word)
            # takes in capital letters
            index = 0
            for char in pattern:
                # print("char for pattern is",char)
                while index < len(word) and (65 > ord(word[index])
                                             or ord(word[index]) > 90
                                             and word[index] != char):
                    # print("index is moving up",index + 1,"for char",char,"word at that index is",word[index])
                    index += 1

                # print(f"the final index is {index} with character {word[index] if index < len(word) else None} for char {char}")
                if index >= len(word) or word[index] != char:
                    return False
                index += 1

            while index < len(word):
                if 65 <= ord(word[index]) <= 90:
                    return False
                index += 1

            return True

        answer = []
        for query in queries:
            answer.append(search(query))
        return answer
