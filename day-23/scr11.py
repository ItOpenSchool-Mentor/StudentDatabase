#######################################################################
# <<<<< Bonus SCRIPT >>>>>                                            # 
# Purpose: From a List of Strings, create a New String that selects   #
#          items that begin with letter `a` and extracts digits[0-9]  #
#          from it.                                                   #
#######################################################################
words = ["a1b2", "apple123", "b456", "a9x", "already", "A789"]

result = [
    ''.join(ch for ch in word if ch.isdigit())
    for word in words
    if word.lower().startswith('a') and any(ch.isdigit() for ch in word)
]

print(result)
