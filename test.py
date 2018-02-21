from fuzzywuzzy import fuzz
print("ok imported")
i = fuzz.ratio("this is a test", "this is a test!")
print("ok we have ratio")
print(i)
print("----")
