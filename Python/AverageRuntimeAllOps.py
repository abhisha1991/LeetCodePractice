'''
Given a file consisting of lines like this:
2023-02-01T10:00:00 Operation ABC Start
2023-02-01T10:01:00 Operation ABC End
2023-02-01T10:02:00 Operation DEF Start
2023-02-01T10:10:00 Operation XYZ End
2023-02-01T20:09:00 Operation WXY Start
2023-02-01T10:08:00 Operation XYZ Start
2023-02-01T20:12:00 Operation WXY End
Can you write a program to read these lines and output the average runtime of all operations?
'''
from collections import defaultdict

# operation definiton
class Operation():
    def __init__(self, ts, start, name):
        self.timestamp = ts
        assert start in [0,1]
        self.start = start
        self.name = name

class Solution():
    def __init__(self, text):
        self.text = text
        # dictionary for holding operations objects (start/end), keyed off by the operation name
        self.opDic = defaultdict(list)

    # general utility function for date time parse
    def get_datetime(self, dt_str):
        from datetime import datetime
        return datetime.strptime(dt_str, '%Y-%m-%dT%H:%M:%S')

    def parse_text_into_ops(self):
        arr = self.text.split('\n')
        for row in arr:
            elements = row.split(' ')
            ts = self.get_datetime(elements[0])
            opName = elements[2]
            opType = elements[3].lower()
            assert opType in ['start', 'end']

            if opType.lower() == 'start':
                start = 1
            else:
                start = 0

            self.opDic[opName].append(Operation(ts, start, opName))            

    def print_operations_start_end(self):
        for opName, ops in self.opDic.items():
            print(f'For operation: {opName}, there are {len(ops)} item(s)')
            for op in ops:
                assert opName == op.name
                print(f'Start: {op.start}')
                print(f'Timestamp: {op.timestamp}')

    # main function to be coded up
    def get_avg_runtime(self):
        self.parse_text_into_ops()
        # self.print_operations_start_end()

        totalTime = 0
        countOps = 0
        # iterate through opDic, skipping the operations that started but have not ended
        for opName, ops in self.opDic.items():
            if len(ops) == 1:
                print(f'Skipping operation: {opName}')
                continue

            countOps +=1
            diff = abs((ops[0].timestamp - ops[1].timestamp).total_seconds())
            totalTime += diff
        
        if countOps > 0:
            return totalTime / countOps
        return 0

s = Solution("""2023-02-01T10:00:00 Operation ABC Start
2023-02-01T10:01:00 Operation ABC End
2023-02-01T10:02:00 Operation DEF Start
2023-02-01T10:10:00 Operation XYZ End
2023-02-01T20:09:00 Operation WXY Start
2023-02-01T10:08:00 Operation XYZ Start
2023-02-01T20:12:00 Operation WXY End""")

# Explanation - There are 3 eligible operations - ABC, WXY and XYZ -- which run for 1, 3 and 2 mins respectively. 
# So average is (1+2+3)/3 = 2 min = 120 seconds

print(s.get_avg_runtime())
# print(s.get_datetime('2023-02-01T10:00:00'))