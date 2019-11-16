'''
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,4,6].

'''


class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class NestedIterator(object):

    def __init__(self, nestedList):
        from collections import deque
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        Q = deque()
        self.datas = []
        for x in nestedList:
            Q.append(x)
        while Q:
            data = Q.popleft()
            if data.isInteger():
                self.datas.append(data.getInteger())
            else:
                temp = data.getList()
                for i in range(len(temp) - 1, -1, -1):
                    Q.appendleft(temp[i])
        self.index = -1

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.datas[self.index]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index < len(self.datas) - 1:
            return True
        else:
            return False
