'''
Given a file consisting of lines like this:
2017 - 02 - 01 T10: 00 Operation ABC Start
2017 - 02 - 01 T10: 01 Operation ABC End
2017 - 02 - 01 T10: 02 Operation DEF Start
2017 - 02 - 01 T10: 08 Operation XYZ Start
2017 - 02 - 01 T20: 09 Operation WXY Start
2017 - 02 - 01 T20: 10 Operation XYZ End
2017 - 02 - 01 T20: 12 Operation WXY End
Can you write a program to read these lines and output the average runtime of all operations?
'''
class Solution(object):
    def __init__(self, text):
        self.text = text
        self.ops = []
        # self.dic = {}
        self.start = {}
        self.end = {}


    def parseTime(self):
        temp = self.text.split('\n')
        for i in temp:
            temp2 = i.split(' ')
            timestamp = temp2[0]
            if temp2[3] == 'Start':
                self.start[temp2[2]] = timestamp
            elif temp2[3] == 'End':
                self.end[temp2[2]] = timestamp

        setop = set(list(self.start.keys()).extend(self.end.keys()))
        tsum = 0
        for i in setop:
            if i in self.start.keys() and i in self.end.keys():
                tsum += self.end[i] - self.start[i]
        return tsum / len(setop)

s = Solution("2017 - 02 - 01 T10: 00 Operation ABC Start"
             "2017 - 02 - 01 T10: 01 Operation ABC End"
             "2017 - 02 - 01 T10: 02 Operation DEF Start"
             "2017 - 02 - 01 T10: 08 Operation XYZ Start"
             "2017 - 02 - 01 T20: 09 Operation WXY Start"
             "2017 - 02 - 01 T20: 10 Operation XYZ End"
             "2017 - 02 - 01 T20: 12 Operation WXY End")
