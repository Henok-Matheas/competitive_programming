class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        answer = []
        for foldr in folder:
            if answer and foldr.startswith(answer[-1] + "/"):
                continue
            answer.append(foldr)
        return answer

        # TRIE IMPLEMENTATION


#         def removeSubfolders(self, folder: List[str]) -> List[str]:
#             folder.sort(key = lambda word : len(word))
#             folders = []

#             for file in folder:
#                 fil = file.split("/")
#                 folders.append(fil[1:])
#             directory = {"END":False}

#             answer = []
#             for folder in folders:
#                 working = directory
#                 works = True
#                 path = ""
#                 for sub in folder:
#                     if working["END"]:
#                         works = False
#                         break
#                     working["/" + sub] = {"END":False} if "/" + sub not in working else working["/" + sub]
#                     path += "/" + sub
#                     working = working["/" + sub]
#                 if works:
#                     answer.append(path)
#                 working["END"] = True
#             return answer