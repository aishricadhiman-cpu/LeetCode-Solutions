class Solution(object):
    def get_num(self , n):
        total = 0
        while n > 0:
            n , digit = divmod(n , 10)
            total += digit**2
        return total
    def isHappy(self, n):
        slow = n
        fast = self.get_num(n)
        while fast != 1 and fast != slow:
            slow = self.get_num(slow)
            fast = self.get_num(self.get_num(fast))
        return fast==1

