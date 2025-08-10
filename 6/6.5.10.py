def find_silver_score(scores):
    gold_medal = float('-inf')
    silver_medal = float('-inf')
    for ball in scores:
        if ball > gold_medal:
            silver_medal = gold_medal
            gold_medal = ball
        elif ball > silver_medal and ball != gold_medal:
            silver_medal = ball
    return silver_medal


print(find_silver_score([40, 20, 30, 10, 20]))
print(find_silver_score([5, 2, 5, 3, 3, 1]))
print(find_silver_score([10, 10, 5, 5])) 
print(find_silver_score([1, 1, 3, 2, 2]))         # 3 – золото, 2 – серебро, 1 - бронза
print(find_silver_score([1, 2, 3]))      
print(find_silver_score([1, 2]))


