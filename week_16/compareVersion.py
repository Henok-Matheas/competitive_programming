class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:
        verzion1 = version1.split(".")
        verzion2 = version2.split(".")

        for index in range(max(len(verzion1), len(verzion2))):
            rev1 = int(verzion1[index]) if index < len(verzion1) else 0
            rev2 = int(verzion2[index]) if index < len(verzion2) else 0

            if rev1 > rev2:
                return 1
            elif rev2 > rev1:
                return -1
        return 0
