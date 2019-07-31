#Пример создания хеш-таблицы и хеш-функции
book = dict()#создаем новую хеш-таблицу, можно просто book = {}

book["apple"] = 0.77
book["orange"] = 1.32
book["avocado"] = 1.79
book["grapple"] = 0.11

print(book["avocado"])

#Example with phone_book
phone_book = {}

phone_book["Andrey"] = 674138256
phone_book["Vasiliy"] = 961191727
phone_book["Jenny"] = 976147218

print(phone_book["Vasiliy"])

#Исключение дубликатов
voted = {}#создаем новую хеш-таблицу для уже проголосовавших

def check_voter(name):
    if voted.get(name):
        print ("Kick them out!")
    else:
        voted[name] = True
        print("Let them vote!")

check_voter("Tom") #тестируем на дубликаты
check_voter("Igor") #тестируем на дубликаты
check_voter("Tom") #тестируем на дубликаты

#Использование хеш-таблиц как кеша для запрашиваемых веб-страниц
cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
       # data = get_data_from_server(url)
        data = "url_from_server"
        cache[url] = data
        return data
