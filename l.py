import re

str = "The rain in Spain"
x = re.search("ai", str)
print(x.span())
