class Solution(object):
    def lengthOfLastWord(self, s):
        solution = s.strip().split()

        if solution:
            return len(solution[-1])
        
        return 0
       