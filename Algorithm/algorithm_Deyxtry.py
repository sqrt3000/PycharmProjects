graph = {} #создаем новую хеш-таблицу

#эта таблица содержит другие хеш-таблицы
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

#включаем в граф остальные узлы и их соседей
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

#Создаем таблицу стоимостей (или весов)
infinity = float("inf") #это бесконечность в Python
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#Создаем хеш-таблицы родителей
parents = {}
parents["a"] = "start"
parents["b"] = " start"
parents["in"] = None

#Создаем массив для отслеживания всех обработанных узлов
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) #найти узел с наименшей стоимость среди необработанных
while  node  is  not  None: #если обработаны все узлы - цикл завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): #перебираем всех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: #Если к соседу можно быстрее добраться - обновляем стоимость соседнего узла
            costs[n] = new_cost
            parents[n] = node #Этот узел становится новым родителем для соседа
    processed.append(node) #узел помечается как обработанный
    node = find_lowest_cost_node(costs) # найти следующий узел для обработки и повторить цикл



# print  (graph["start"].keys())


