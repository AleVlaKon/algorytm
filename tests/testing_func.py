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