responses = [
    "The product quality is excellent and delivery was fast",
    "Terrible experience, very slow shipping and poor packaging",
    "Great value for money, I am very happy with my purchase",
    "The item arrived damaged, completely unacceptable service",
    "Fast delivery and excellent customer support, highly recommend",
    "Poor quality product, broke after one week, very disappointed",
    "Amazing product, exceeded all my expectations",
    "Shipping was slow but the product quality is good",
    "Excellent quality and great packaging, will buy again",
    "Very unhappy with the service, product was missing parts"
]

positive_keywords = ["excellent", "great", "fast", "happy", "amazing", "good", "recommend"]
negative_keywords = ["terrible", "poor", "slow", "damaged", "unacceptable", "disappointed", "unhappy"]

positive_counts = {word: 0 for word in positive_keywords}
negative_counts = {word: 0 for word in negative_keywords}

n_positive_responses = 0
n_negative_responses = 0
n_neutral_responses = 0

for response in responses:
    words = response.lower().replace(",", "").split()

    response_pos = 0
    response_neg = 0

    for word in words:
        if word in positive_keywords:
            positive_counts[word] += 1
            response_pos += 1
        if word in negative_keywords:
            negative_counts[word] += 1
            response_neg += 1

    if response_pos > response_neg:
        n_positive_responses += 1
    elif response_neg > response_pos:
        n_negative_responses += 1
    else:
        n_neutral_responses += 1

total = len(responses)
positive_rate = (n_positive_responses / total) * 100

most_common_positive = max(positive_counts, key=positive_counts.get)
most_common_negative = max(negative_counts, key=negative_counts.get)

print("Survey Analysis Report")
print("-----------------------")
print(f"Total Responses : {total}")
print(f"Positive : {n_positive_responses}")
print(f"Negative : {n_negative_responses}")
print(f"Neutral : {n_neutral_responses}")
print(f"Positive Response Rate: {positive_rate:.1f}%")
print()
print("Keywords Found:")
print(f"Most Common Positive: {most_common_positive} ({positive_counts[most_common_positive]})")
print(f"Most Common Negative: {most_common_negative} ({negative_counts[most_common_negative]})")