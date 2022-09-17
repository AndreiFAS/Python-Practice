# .html

def start():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    telephone = input('Введите номер телефона: ')
    decription = input('Добавьте описание: ')
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Имя: {} </p>\n'\
        .format(style, name)
    html += '    <p {}>Фамилия: {} </p>\n'\
        .format(style, surname)
    html += '    <p {}>Телефон: {} </p>\n'\
        .format(style, telephone)
    html += '    <p {}>Описание: {} </p>\n'\
        .format(style, decription)
    html += '  </body>\n</html>'
    
    with open('/Old/HomeWork007/BD.html', 'a+') as page:
        page.write(html)
