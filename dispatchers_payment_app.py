def dispatchers_payment_system(collection_rate):
    result = 0
    if collection_rate < 0:
        raise ValueError("you have not done any work that can earn you a rating")
    if collection_rate <= 50:
        result = collection_rate * 160 + 5000

    elif 50 > collection_rate <= 59:
        result = collection_rate * 200 + 5000

    elif 60 > collection_rate <= 69:
        result = collection_rate * 250 + 5000

    elif collection_rate >= 70:
        result = collection_rate * 500 + 5000

    return result
