#Реализация алгоритма поиска в ширину
from collections import deque #ипорт функции создания очереди

graph = {}
graph["you"] = ["alece", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque() #создаем очередь
    search_queue += graph[name] #все соседи добавляются в очередь поиска
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("claire")