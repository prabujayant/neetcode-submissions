class Solution:    
    def encode(self, strs: List[str]) -> str:
        # Encode each string as "length#string"
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            # Find the separator "#"
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])   # extract length
            i = j + 1            # skip '#'
            
            # Extract the substring of given size
            res.append(s[i:i+size])
            i += size
        return res

        #o(m) o(m+n)