import collections
string=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]

long_string= "".join(string)
collections.Counter(long_string)


print(collections.Counter(long_string))