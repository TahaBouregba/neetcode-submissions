class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for i in strs:
            result += str(len(i)) + "#" + i

        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find #
            while s[j] != '#':
                j += 1

            # Get the length
            size = int(s[i:j])

            # Move after #
            j += 1

            # Extract the word
            res.append(s[j:j + size])

            # Move to the next encoded word
            i = j + size

        return res
                            
        
        


    
