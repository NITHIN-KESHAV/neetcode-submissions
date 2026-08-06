class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        st = {}


        for s in strs:
            key = "".join(sorted(s))

            if key not in st:
                st[key] = []
            st[key].append(s)
        
        return list(st.values())

