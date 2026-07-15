def explain(score):

    reasons = []

    if score > 80:
        reasons.append("High transaction amount")

        reasons.append("Unknown device")

        reasons.append("Multiple failed logins")

    return reasons
