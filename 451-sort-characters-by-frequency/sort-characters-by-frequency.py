class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq={}

        for ch in s:
            freq[ch]=freq.get(ch,0)+1

        sort=sorted(freq.items(),key=lambda x: (-x[1],x[0]))

        res=""

        for ch,count in sort:
            res+=ch*count
        return res


        