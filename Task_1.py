import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)  # Створюємо мін-купу
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)
    
    return total_cost


# Приклад використання:
cables = [4, 3, 2, 6]
print("Мінімальні витрати:", min_cost_to_connect_cables(cables))
