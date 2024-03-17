import sys

case = int(sys.stdin.readline())

result = 0
for i in range(case):
    word=sys.stdin.readline()
    word_len=len(word)
    error =0
    for j in range(word_len-1):
        if word[j]!=word[j+1]:
            new_word=word[j+1:]
            if new_word.count(word[j])>=1:
                error +=1
    if error ==0:
        result +=1
        
print(result)            