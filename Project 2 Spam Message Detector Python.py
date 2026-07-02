# Project : Spam Message Detector
# Tool : Python
# Benefit : Foundation for email filtering, fraud detection, and sentiment analysis

spam_words = ["win","prize","free","click","offer","money"]

message = input("Enter a  message: ").lower()

if any(word in message for word in spam_words):
    print("spam message")

else:
    print("Not Spam")