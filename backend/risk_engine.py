def calculate_risk(user):

    score = 0

    if user["new_device"]:
        score += 20

    if user["new_location"]:
        score += 15

    if user["large_transaction"]:
        score += 25

    if user["failed_logins"] > 3:
        score += 20

    if user["malware_detected"]:
        score += 20

    return min(score,100)
