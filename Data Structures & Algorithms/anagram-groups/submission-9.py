class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for i in strs:
            base_list = [0] * 26
            for j in i:
                index = ord(j) - ord('a')
                base_list[index] += 1

            base_tuple = tuple(base_list)
            anagram_dict[base_tuple] = anagram_dict.get(base_tuple, [])
            anagram_dict[base_tuple].append(i)
        
        return list(anagram_dict.values())
        