def word_count(str):
    wrd_cnt = {}
    for word in str.lower().split():
        if word in wrd_cnt.keys():
            wrd_cnt[word] += 1
        else:
            wrd_cnt[word] = 1
    return wrd_cnt
    
print(word_count("I do not like it Sam I Am"))