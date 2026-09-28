class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq={}

        for word in words:
            freq[word]=freq.get(word,0)+1
        
        sort=sorted(freq.items(),key=lambda x:[-x[1],x[0]])

        result=[]

        for word,count in (sort[:k]):
            result.append(word)
        
        return result
        