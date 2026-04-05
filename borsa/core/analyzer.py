def analyze(news_list):
    score = 0

    for news in news_list:
        if "POZİTİF" in news["sentiment"]:
            score += 2
        elif "NEGATİF" in news["sentiment"]:
            score -= 2

    if score > 2:
        return "AL 📈"
    elif score < -2:
        return "SAT 📉"
    else:
        return "BEKLE ⏳"