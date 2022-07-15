import requests
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
result = {}

# Остановка, когда доходим до английских животных
english = False
print("The cycle is working, might need a few minutes...")
while not english:
    # Получаю животных со страницы
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html')
    names = soup.find_all('div', id='mw-pages')[0].find_all("li")
    for name in names:
        letter = name.text[0]
        if letter == "H":
            continue
        if letter == "A": # Проверка на английскую A
            english = True
            break
        if letter == "Ё": # Объединяю животных с Е и Ё в одну группу
            letter = "Е"
        if letter in result:
            result[letter].append(name.text)
        else:
            result[letter] = [name.text]
    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text == 'Следующая страница':
            # Перехожу на следующую страницу
            url = 'https://ru.wikipedia.org/' + a.get('href')
            page = requests.get(url).text

# Получаю словарь с количеством животных, начинающихся с буквы
lengths = {key:len(value) for key, value in result.items()}
# Вывожу количества животных, сортированные по алфавиту
for key, val in sorted(lengths.items()):
    print(f"{key}: {val}")