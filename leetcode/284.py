

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.tnext = iterator.next()
        self.thasNext = iterator.hasNext()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.tnext

    def next(self):
        """
        :rtype: int
        """
        ret = self.tnext
        self.thasNext = self.iterator.hasNext()
        self.tnext = self.iterator.next() if self.thasNext else 0
        return ret

    
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.thasNext
        