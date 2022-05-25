# https://leetcode.com/problems/logger-rate-limiter/
class Logger:

    def __init__(self):
        self.dic = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.dic:
            self.dic[message] = timestamp
            return True
        
        if self.dic[message] + 10 > timestamp:
            # when returning false, you don't want to update the timestamp of the message
            return False
        
        self.dic[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)