class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                list+=["FizzBuzz"]
            elif i%3==0:
                list+=["Fizz"]
            elif i%5==0:
                list+=["Buzz"]
            else:
                list+=[str(i)]
        return list
