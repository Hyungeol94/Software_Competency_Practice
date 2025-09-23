#https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2025-09-23
#165. Compare Version Numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1str = version1.split(".")
        ver2str = version2.split(".")
        
        is_reverse = False
        if len(ver1str) < len(ver2str):
            ver1str, ver2str = ver2str, ver1str
            is_reverse = True
        
        for a, b in zip(ver1str, ver2str):
            if int(a) > int(b):
                return 1 if not is_reverse else -1
            if int(a) < int(b):
                return -1 if not is_reverse else 1
        
        if len(ver1str) > len(ver2str):
            i = len(ver2str)
            while i < len(ver1str):
                curr = ver1str[i]
                if int(curr) > 0:
                    return 1 if not is_reverse else -1
                i += 1 
        
        return 0