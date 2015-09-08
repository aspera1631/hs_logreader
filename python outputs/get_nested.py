__author__ = 'bdeutsch'
# get the contents of the innermost hard brackets of a string
import re

str1 = "[power] this is [a test [of a function] that] might work, [or] it might not."
str2 = "This string has no nesting."

def get_nested(str1):
    m = re.findall(r"\[([^\[]+?)]", str1)
    if len(m)>1:
        strings = []
        for item in m[1:]:
            strings.append(item)
        return strings
    else:
        return None


test = get_nested(str2)

print test