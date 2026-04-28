# Detect Blocked Words : spam, scam, fake
blocked_words = {"spam", "scam", "fake"}
message = "this is a spam message"
words = set(message.split())
print(f"Blocked Words = {blocked_words}")
print(f"Words = {words}")

if words & blocked_words:
    print("Warning: Blocked Content Detected")

