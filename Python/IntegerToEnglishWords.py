# https://leetcode.com/problems/integer-to-english-words
class Solution:
    def numberToWords(self, num: int) -> str:
        '''
        pray to god you don't get this in an interview
        
        the way to solve this is to group numbers into sets of 3 and try to convert those to english
        why sets of 3? because we write 1 million as 1,000,000 in the english system partitioned at 3 digits
        
        for example, 1234567890 ==> 1  234  567  890 
        
        1 billion 234 million 567 thousand 890
                   |           |            |
                   |           |            |
                   |           |            |
                   |           |            |
                   |           |            |
                  two hundred thirty four   |
                               |            |
                               |            |
                    five hundred and sixty seven
                                            |
                                            |
                                      eight hundred and ninety
                                      
        the 3 digit can be split into 2 sub problems further, ie, 234 = 2 hundred 34
        
        34 can be split further into "thirty 4", 
        but we need to be aware of special cases like 19 (or in general 1x)-- which is the "teens" 
        '''      
        
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)

        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)
        
        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)
        
        # handle 2 digits, like say 34 ==> thirty four
        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                # the teens case!
                return two_less_20(num)
            else:
                tenner = num // 10
                rest = num - tenner * 10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)
        
        # handle 3 digits, like say 134 ==> one hundred thirty four
        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            # a number like 134 - which has a hundred part and a 2 digit part
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest) 
            # a number which is actually 2 digit, like 78
            elif not hundred and rest: 
                return two(rest)
            # a number like 300, which doesn't have a 'rest' part
            elif hundred and not rest:
                return one(hundred) + ' Hundred'
        
        # see if the number has any billion part
        billion = num // 1000000000
        
        # see if number has any million part
        million = (num - billion * 1000000000) // 1000000
        
        # see if number has any thousand part
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
        if not num:
            return 'Zero'
        
        result = ''
        if billion:        
            # result can have up to 3 digits on the billion side, like 378 billion, so we need to resolve 378
            result = three(billion) + ' Billion'
        if million:
            # add space between the billion and million
            result += ' ' if result else ''    
            # append to result - a 3 digit parse of the million part, like 378 billion 261 million
            # so we need to resolve 261 using the three function
            result += three(million) + ' Million'
        if thousand:
            # add space between the result so far (billion and million) and make way for the thousand part
            result += ' ' if result else ''
            # do a similar exercise to parse the thousand part in groups of 3
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result