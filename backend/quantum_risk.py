def quantum_risk(cipher, sensitivity):

    score = 0

    if cipher == "RSA":
        score += 40

    elif cipher == "ECDHE":
        score += 20

    if sensitivity == "HIGH":
        score += 50

    elif sensitivity == "MEDIUM":
        score += 25

    return min(score,100)
