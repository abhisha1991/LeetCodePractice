'''
A company registers for an IPO. 
All shares are available on the website for bidding during a time frame called the bidding window. 
At the end of the bidding window an auction logic is used to decide how many available shares go to which bidder until all shares have been allocated, 
or all the bidders have received the shares they bid for, whichever comes first.

The bids arrive from users in the form of [userid, # shares, bidding price, timestamp] until the bidding window is closed.

The auction logic assigns shares as follows:
The bidder with the highest price gets the # of shares they bid for.
If multiple bidders have bid at the same price, the bidders are assigned shares in the order in which they places their bids (earliest bids first).
List the userids of all the users who didn't get even 1 share after all shares have been allocated.

INPUTS:
-- bids: list of lists of ints representing [userid, # shares, $bid, timestamp]
-- totalShares: total # of shares to be distributed.

PROBLEM STATEMENT:
Distribute shares amongst bidders and return userids of bidders that got 0 shares.
'''
# cols to sort on
USERID = 0
SHARES = 1
BID = 2
TIME = 3

def getLoserBids(bids, totalShares):
    # sort the bids by first in negative asc order of bid price (such that "negative highest bid" is smallest and comes first) 
    # and then we sort by time asc in case we have a tie on the bid price
    bids = sorted(bids, key=lambda x: (-x[BID], x[TIME]))
    loserIdx = 0
    for i in range(len(bids)):
        bid = bids[i]
        # subtract the number of shares being put forward by that bid
        totalShares -= bid[SHARES]
        # if we are not left with any more shares to give out, break
        if totalShares <= 0:
            # all members after this point, won't be able to get shares
            loserIdx = i
            break

    # select user ids from loser index onward to the end of the bids array
    # return sorted bids by userid         
    return sorted([bid for bid in bids[loserIdx:]], key=lambda x: x[0])

bids = [[5, 30, 10, 120], [1, 20, 80, 123], [2, 30, 76, 124], [1, 10, 81, 126], [3, 5, 10, 126], [4, 5, 100, 127], [3, 30, 100, 130]]
print(getLoserBids(bids, 100))
