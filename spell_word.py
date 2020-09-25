from collections import defaultdict;

class Solution1(object):
    def canSpell(self, magazine, word):
        letters = defaultdict(int);

        for c in magazine:
            letters[c] +=1
        
        for c in word:
            if letters[c] <= 0:
                return False
            letters[c] -= 1

        return True

        
print(Solution1().canSpell(['A','B','C','D','E','F'], 'BED'))
# True (9 loops)

print(Solution1().canSpell(['A','B','C','D','E','F'], 'CAT'))
# False (9 loops)
