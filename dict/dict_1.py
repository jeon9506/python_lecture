singer = {}

singer['이름'] = '트와이스'
singer['구성원 수'] = 9
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'SINGAL'

for k in singer.keys() :
    print(f'{k} --> {singer[k]}')

print(list(singer.keys()))
print(singer.values())