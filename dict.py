import sys
import re
import os

DIAL_CODES = [
    (86, 'China'),
    (91, 'india'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
]

country_code = {code:country for code, country in DIAL_CODES}

print(country_code)

# print({code: country.upper for country, code in country_code.items() if code < 66})
print(country_code.get(80, 'Colombia'))

WORD_RE = re.compile(r'\w+')

index = {}


with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences


for word in sorted(index, key=str.upper):
    print(word, index[word])

fp = open('cafe.txt', 'w', encoding='utf_8')
print(fp)
print(fp.write('café'))
fp.close()
print(os.stat('cafe.txt').st_size)
print(os.getcwd())
print(os.name)
fp2 = open('cafe.txt')
print(fp2)
print(fp2.encoding)

