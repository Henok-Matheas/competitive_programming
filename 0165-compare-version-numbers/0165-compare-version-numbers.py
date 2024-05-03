class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        
        """
        version1_list = version1.split(".")
        version2_list = version2.split(".")
        
        
        len1, len2 = len(version1_list), len(version2_list)
        
        range_ = max(len1, len2)
        
        for idx in range(range_):
            num1 = int(version1_list[idx]) if idx < len1 else 0
            num2 = int(version2_list[idx]) if idx < len2 else 0
            
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            
        return 0
            