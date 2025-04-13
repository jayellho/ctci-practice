'''
 1. Future stock prices

 Problem Statement:
 Given an unordered list of future stock prices, what is the maximum amount of profit that you could generate from a starting amount of $1,000.00.

 Rules: 
 - You can trade fractional shares (e.g. if there were shares for $400.00, you can buy/sell 2.5 of them for $1,000.00). 
 - All trades occur instantaneously and do not incur any transaction costs. 
 - Shares may only be bought/sold on a date that you have a known price. 
 - Short selling is NOT allowed. 
 - You do not need to have a position at all times i.e. if you cant find a profitable trade, you dont need to trade. 
 - Round your answer to the nearest dollar.
 - Do not assume the input tuple will be sorted in any manner. 
 - Future prices will be given in the following format [Stock, Date, Price].

 Example 1:
 Input:
 CSCO, 10/18/2024, 41.89
 AMZN, 10/10/2024, 113.67
 AMZN, 10/18/2024, 120.5
 CSCO, 10/10/2024, 43.12

 Solution:
 Buy 8.797 AMZN @ $113.67 on 10/10/2024 and sell @ 120.5 on 10/18/2024. Profit = $60.

 Expected Output:
 60


 Example 2:
 Input:
 IBM, 12/01/2023, 132.05 3
 IBM 12/03/2023, 135.19 4
 IBM 12/18/2023, 134.07 7
 AAPL 12/01/2023 187.19 1
 AAPL 12/04/2023 164.33 5
 AAPL 12/20/2023 180.94 9
 AAPL 12/21/2023 179.65 10
 GOOG 12/01/2023 116.41 2
 GOOG 12/07/2023 111.36 6
 GOOG 12/19/2023 112.19 8
 
 Solution:
 Buy 7.573 IBM @ $132.05 on 12/01/2023 and sell @ 135.19 on 12/3/2023. 
 Buy 6.230 AAPL on 12/4/2023 @ 164.33 and sell on 12/20/2023 @ $180.94. 
 Profit = $127.

 Expected Output:
 127
'''

'''
- sort input by date.
- create DAG with 2 kinds of edges:
    - connection between different stocks - 0-weighted.
    - connection between same stocks - weight by log(y) - log(x) where y is the later price, x is the earlier price.
- find the longest path.
    - DP:
        - L[i] = max(L[j] + edge[j, i] for all nodes with incoming edges j into i)
'''



    
import math

def getMaxProfit(price_list):
    # Sort the price list by date, then by company for a deterministic order.
    price_list.sort(key=lambda x: (x[1], x[0]))
    n = len(price_list)
    
    # dp[i]: maximum cumulative log multiplier achievable by the time we reach price_list[i].
    dp = [-float('inf')] * n
    dp[0] = 0  # Starting capital gives a log multiplier of 0.
    
    # This dictionary will track the last occurrence index for each company.
    last_occurrence = {}
    
    # Process nodes in sorted (topological) order.
    for i in range(n):
        company, date, price = price_list[i]
        
        # If there is a previous occurrence of this company, consider the trade edge.
        # The edge weight represents the trading gain: log(current_price) - log(previous_price)
        if company in last_occurrence:
            j = last_occurrence[company]
            trade_weight = math.log(price) - math.log(price_list[j][2])
            dp[i] = max(dp[i], dp[j] + trade_weight)
        
        # Propagate the best cumulative log gain to the next node (time edge with weight 0).
        if i + 1 < n:
            dp[i+1] = max(dp[i+1], dp[i])
        
        # Update the last occurrence of the current company.
        last_occurrence[company] = i
    print(f"dp = {dp}")
    # The best cumulative gain among all nodes.
    best = max(dp)
    
    # Final money = starting money * exp(best gain);
    # net profit is final money minus the starting money.
    final_money = 1000 * math.exp(best)
    profit = final_money - 1000
    return round(profit)

# Test with Example 1.
stock_data_example1 = [
    ["CSCO", "10/18/2024", 41.89],
    ["AMZN", "10/10/2024", 113.67],
    ["AMZN", "10/18/2024", 120.5],
    ["CSCO", "10/10/2024", 43.12]
]
print("Example 1 Profit:", getMaxProfit(stock_data_example1))  # Expected output: 60

# Test with Example 2.
stock_data_example2 = [
    ["IBM", "12/01/2023", 132.05],
    ["IBM", "12/03/2023", 135.19],
    ["IBM", "12/18/2023", 134.07],
    ["AAPL", "12/01/2023", 187.19],
    ["AAPL", "12/04/2023", 164.33],
    ["AAPL", "12/20/2023", 180.94],
    ["AAPL", "12/21/2023", 179.65],
    ["GOOG", "12/01/2023", 116.41],
    ["GOOG", "12/07/2023", 111.36],
    ["GOOG", "12/19/2023", 112.19],
]
print("Example 2 Profit:", getMaxProfit(stock_data_example2))  # Expected output: 127


# ABANDONED APPROACH
# import math
# import heapq
# import collections

# def getMaxProfit(price_list):

#     # sort list by date.
#     price_list.sort(key=lambda x: x[1])

#     # get sublists by company.
#     company_list = {}
#     for company, date, price in price_list:
#         if company not in company_list:
#             company_list[company] = [(date, price)]
#         else:
#             company_list[company].append((date, price))
    
#     print(company_list)
    

#     # create adjacency list.
#     # <source node: (co, date)> ==> <max heap of destination nodes: (edge_wt, co, date)
    
#     ## create edges by company.
#     adj_list = {}
#     for co, prices in company_list.items():
#         len_prices = len(prices)
#         if len_prices >= 2:
#             for i in range(len_prices-1):
#                 src_date, src_price = prices[i]
#                 dst_date, dst_price = prices[i+1]
#                 wt = math.log(dst_price) - math.log(src_price)

#                 if (co, src_date) not in adj_list:
#                     adj_list[(co, src_date)] = []
#                 heapq.heappush(adj_list[(co, src_date)], (-wt, co, dst_date))

    
#     ## create edges by topo sort.
#     for i in range(len(price_list)-1):
#         src_co, src_date, src_price = price_list[i]
#         dst_co, dst_date, dst_price = price_list[i+1]

#         if (src_co, src_date) not in adj_list:
#             adj_list[(src_co, src_date)] = []
#         heapq.heappush(adj_list[(src_co, src_date)], (0, dst_co, dst_date))

    
#     # iterate to get max.
#     max_profit = 0
#     q = collections.deque()
#     q.append(price_list[0][:2])
#     visited = set()
#     visited.add((price_list[0][0], price_list[0][1]))


#     while q:
#         co, date = q.popleft()

#         if (co, date) in adj_list and adj_list[(co, date)]:
#             wt, dst_co, dst_date = adj_list[(co,date)][0]
#             print(f"wt, dst_co, dst_date = {wt, dst_co, dst_date}")

#         max_profit -= wt
#         if (dst_co, dst_date) not in visited:
#             q.append((dst_co, dst_date))
#             visited.add((dst_co, dst_date))
#     print(1000 * math.exp(max_profit))
#     return max_profit




# # test.
# stock_data_eg1 = [
#     ["IBM", "12/01/2023", 132.05],
#     ["IBM", "12/03/2023", 135.19],
#     ["IBM", "12/18/2023", 134.07],
#     ["AAPL", "12/01/2023", 187.19],
#     ["AAPL", "12/04/2023", 164.33],
#     ["AAPL", "12/20/2023", 180.94],
#     ["AAPL", "12/21/2023", 179.65],
#     ["GOOG", "12/01/2023", 116.41],
#     ["GOOG", "12/07/2023", 111.36],
#     ["GOOG", "12/19/2023", 112.19],
# ]

# stock_data_eg2 = [
#     ["CSCO", "10/18/2024", 41.89],
#     ["AMZN", "10/10/2024", 113.67],
#     ["AMZN", "10/18/2024", 120.5],
#     ["CSCO", "10/10/2024", 43.12]
# ]


# getMaxProfit(stock_data_eg1)
# getMaxProfit(stock_data_eg2)