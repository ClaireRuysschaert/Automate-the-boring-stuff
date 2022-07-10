# ? = matches 0 or 1 of the preceding group
# * = matches 0 or more of the preceding group
# + = matches 1 or more of the preceding group
# {n} = matches exactly n of the preceding group
# {n,} = matches n or more of the preceding group
# {,m} = matches 0 to m of the preceding group
# {n,m} = matches at least n and at most m of the preceding group
# {n,m}? = matches at least n and at most m of the preceding group, but it’s optional
# *? = matches 0 or more of the preceding group, but it’s optional
# +? = matches 1 or more of the preceding group, but it’s optional
# ^ŝpam = must begin with spam
# spam$ = must end with spam
# . = matches any character except newline

#\d , \w , and \s match a digit, word, or space character, respectively.
#\D , \W , and \S match anything except a digit, word, or space character, respectively.

# [abc] = matches any character between the brackets
# [^abc] = matches any character that isn’t between the brackets