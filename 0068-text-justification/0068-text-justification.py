class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answers= [[]]
        length = 0

        for word in words:
            curr_length = len(word) + length + (1 if length else 0)
            if curr_length > maxWidth:
                length = 0
                answers.append([])
            answers[-1].append(word)
            length += 1 if length else 0
            length += len(word)

        final = []

        for line_idx,line in enumerate(answers):
            printable_line = []
            remaining = maxWidth
            for word in line:
                remaining -= len(word)

            

            if len(line) == 1:
                final.append(line[0] + (" " * remaining))
                continue

            if line_idx == len(answers) - 1:
                to_append = " ".join(line)
                final.append(to_append + " " * (maxWidth - len(to_append)))
                continue
            
            int_remain = remaining // (len(line) - 1)
            extra =  remaining % (len(line) - 1)

            for idx in range(len(line) - 1):
                spaces  = int_remain + (1 if extra else 0)
                printable_line.append(line[idx] + (" " * spaces))

                if extra:
                    extra -= 1

            printable_line.append(line[-1])
            
            final.append("".join(printable_line))

        return final