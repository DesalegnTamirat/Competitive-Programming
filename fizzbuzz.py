class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        t = list()
        for i in range(1, n + 1):
            if i % 15 == 0:
                t.append('FizzBuzz')
            elif i % 5 == 0:
                t.append('Buzz')
            elif i % 3 == 0:
                t.append('Fizz')
            else:
                t.append(str(i))
        return t