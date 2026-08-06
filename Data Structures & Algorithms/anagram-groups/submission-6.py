class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        st = {}

        for s in strs:

            a = [0]* 26

            for c in s:
                index = ord(c) - ord('a')
                a[index] += 1
            
            key = tuple(a)

            if key not in st:

                st[key] = []

            st[key].append(s)
        
        return list(st.values())



        

