import re

text = "The rain in Spain falls mainly in the plain."

# 1. Match a pattern at the beginning of the string
match_result = re.match(r"The", text)
print("Match result:", match_result.group() if match_result else "No match")

# 2. Search for the first occurrence of "ain" in the string
search_result = re.search(r"ain", text)
print("Search result:", search_result.group() if search_result else "No match")

# 3. Find all occurrences of "ain"
findall_result = re.findall(r"ain", text)
print("Find all result:", findall_result)

# 4. Replace "rain" with "snow"
sub_result = re.sub(r"rain", "snow", text)
print("Sub result:", sub_result)

# 5. Split text at every space
split_result = re.split(r"\s", text)
print("Split result:", split_result)