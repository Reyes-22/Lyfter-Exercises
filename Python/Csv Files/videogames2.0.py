import csv
data = [{'Name': 'GTA V', 'Type': 'Action', 'Developer': 'Rockstar', 'Classification': 'A'},
        {'Name': 'God of War', 'Type': 'Action',
            'Developer': 'Santa Monica Studio', 'Classification': 'M'},
        {'Name': 'FIFA', 'Type': 'Sports', 'Developer': 'EA', 'Classification': 'E'},
        {'Name': 'Call of Duty:Warzone', 'Type': 'Action',
            'Developer': 'Vince Zampella', 'Classification': 'M'}
        ]
headers = ('Name', 'Type', 'Developer', 'Classification')

with open('videogames.tsv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, delimiter='\t', fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
