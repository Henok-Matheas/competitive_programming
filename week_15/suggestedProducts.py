class Solution:

    def suggestedProducts(self, products: List[str],
                          searchWord: str) -> List[List[str]]:
        vocabulary = {'END': False}
        products.sort(reverse=True)

        print(products)

        def add(word):
            current = vocabulary
            for letter in word:
                if letter not in current:
                    current[letter] = {'END': False}
                current = current[letter]
            current['END'] = True

        def prefix(word, vocab):
            current = vocab
            if letter not in current:
                return {}
            return current[letter]

        def allanswers(pat, workng):
            workings = [[pat, workng]]
            answer = []
            while workings:
                current = workings.pop()
                path = current[0]
                working = current[1]
                if "END" in working and working["END"]:
                    answer.append("".join(path))
                if len(answer) == 3:
                    return answer

                for after in working:
                    if after == "END":
                        continue
                    new = path + [after]
                    workings.append([new, working[after]])
            return answer

        for product in products:
            add(product)

        final = []
        path = []
        previous = vocabulary
        for letter in searchWord:
            path.append(letter)
            now = prefix(letter, previous)
            previous = now
            answers_list = allanswers(path, now) if now else []
            final.append(answers_list)

        return final