'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''


class Solution:
    def longestSubstring_brute(self, s: str, k: int) -> int:
        result = [0]
        for start in range(len(s)):
            temp = {}
            for end, string in enumerate(s[start:]):
                temp[string] = temp.get(string, 0) + 1
                if min(temp.values()) >= k:
                    if end + 1 == len(s):
                        return len(s)
                    else:
                        result.append(end + 1)
        return max(result)

    def longestSubstring(self, s: str, k: int) -> int:
        if not s or k > len(s):
            return 0
        if k < 2:
            return len(s)
        s2pos = {}
        s2count = {}
        for idx, string in enumerate(s):
            s2pos[string] = s2pos.get(string, []) + [idx]
            s2count[string] = s2count.get(string, 0) + 1
        keys = [key for key, v in s2count.items() if v < k]
        if not keys:
            return len(s)
        split_id = [-1, len(s)]
        for key in keys:
            split_id.extend(s2pos[key])
        split_id = list(sorted(split_id))
        segs = []
        for idx, id in enumerate(split_id):
            if idx < len(split_id) - 1:
                segs.append((id + 1, split_id[idx + 1], split_id[idx + 1] - id))
        segs = list(sorted(segs, key=lambda x: x[-1], reverse=True))
        result = 0
        for id, (start, end, length) in enumerate(segs):
            if length <= result:
                return result
            temp = self.longestSubstring(s[start: end], k)
            if id == 0 and temp == length:
                return temp
            result = max(result, temp)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring("ababbc", 2))
