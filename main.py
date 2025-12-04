
attribute = {
    'HP' : 100,
    'SAN' : 100,
    'Inventory' : []
}

main_story = {
    'Chapter_1' : {
        'Chapter_1' : 'Chapter_1.txt',
        'Chioces' : {
            '1' : 'sec1',
            '2' : 'sec2'
        },
    },
}

answer = str(input())
for chioce in main_story['Chapter_1']['Chioces']:
    print(chioce[answer])