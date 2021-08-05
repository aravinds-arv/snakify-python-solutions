from collections import defaultdict

lateng = defaultdict(list)
for i in range(int(input())):
    eng_word, lat_trans = input().split(' - ')
    lat_translations = lat_trans.split(', ')
    for lat_word in lat_translations:
        lateng[lat_word].append(eng_word)
        
print(len(lateng))
for lat_word, eng_translations in sorted(lateng.items()):
    print(lat_word + ' - ' + ', '.join(eng_translations))