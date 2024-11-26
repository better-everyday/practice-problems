class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for s in strs:
            sorted_strs.append(''.join(sorted(s)))

        sorted_dict = {}
        for ss in list(set(sorted_strs)):
            sorted_dict[ss] = []

        for sstr in range(len(sorted_strs)):
            sorted_dict[sorted_strs[sstr]].append(strs[sstr])

        return list(sorted_dict.values())