# -*- coding:Utf-8 -*-

dir_path = "path_of_the_life"


with open(dir_path+'db.txt', 'r') as f:
    data = f.read()

data = [item for item in data.split('\n') if len(item)]
table = []

for element in data:
    element = element.split(' ')
    element = element[0], element[-1].split('&')[0].split('v=')[-1]
    table.append(element)


reste = len(table) % 7 #reste du tableau si pas multiple de 7
html = '<table><tr>'


i=1
for item in table[:len(table)-reste]:
    html += '<td style="background-color:#'+item[0]+'" id="'+item[0]+'__'+item[1]+'"></td>\n'

    if i%7 == 0:
        if i != len(table) - reste:
            html += '</tr>\n<tr>'
        else:
            html += '</tr>\n'
    i+=1

if reste:
    html += '<tr>'
    for item in table[len(table)-reste:]:
        print item
        html += '<td style="background-color:#'+item[0]+'" id="'+item[0]+'__'+item[1]+'"></td>\n'
    html += '</tr>\n'

html += '</table>'

with open(dir_path+'table.txt', 'a+') as f:
    f.write(html)

