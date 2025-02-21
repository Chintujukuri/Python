import re

text="the quick brown fox"
pattern=r"quick"
match=re.search(pattern,text)

# re.match(pattern, text) → Matches only at the beginning of text.
# re.search(pattern, text) → Searches anywhere in text and returns the first occurrence.

if match:
    print("match found: ",match.group())
else:
    print("no match")