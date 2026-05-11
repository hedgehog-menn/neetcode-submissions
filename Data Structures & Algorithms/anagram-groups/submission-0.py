class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        counter = 0

        for word in strs:
            char_count = Counter(word)
            key = next((k for k, v in hashmap.items() if v == char_count), None)
            if key is not None: # accept index-0
                res[key].append(word)
            else:
                hashmap[counter] = char_count
                counter += 1
                res.append([word])

        return res

