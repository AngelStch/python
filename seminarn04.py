# zad 1: 
def find_day_winner(matches):
    win_count = {}
    for winner in matches:
        win_count[winner] = win_count.get(winner, 0) + 1

    max_wins = max(win_count.values(), default=0)
    winners = [team for team, count in win_count.items() if count == max_wins]

    return winners[0] if len(winners) == 1 else "Tie"

matches1 = ["Team1", "Team2", "Team1", "Team2", "Team1"]
print(find_day_winner(matches1))

matches2 = ["Team1", "Team2", "Team1", "Team2"]
print(find_day_winner(matches2))

# zad 2:
def is_perfect_number(num):
    if num < 1:
        return False
    return sum(i for i in range(1, num // 2 + 1) if num % i == 0) == num

def find_perfect_numbers(numbers):
    return [num for num in numbers if is_perfect_number(num)]

numbers_list = [6, 28, 12, 496, 8128, 10]
perfect_numbers = find_perfect_numbers(numbers_list)
print("Перфектни числа в списъка:", perfect_numbers)

# zad 3:
def cyclic_product_sum(list1, list2):
    max_len = max(len(list1), len(list2))
    extended_list1 = [list1[i % len(list1)] for i in range(max_len)]
    extended_list2 = [list2[i % len(list2)] for i in range(max_len)]

    return sum(a * b for a, b in zip(extended_list1, extended_list2))

list1 = [1, 2, 3]
list2 = [4, 5]
print("Резултат:", cyclic_product_sum(list1, list2))

# zad 4:
def extract_characters(text, *indices):
    return "".join(text[i] for i in indices if 0 <= i < len(text))

text_input = "Примерен текст"
print("Резултатен текст:", extract_characters(text_input, 0, 2, 4, 10))

# zad 5:
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

num1, num2 = 12, 18
print(f"НОК на {num1} и {num2} е: {lcm(num1, num2)}")

# zad 6: 
def is_prime(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def can_be_sum_of_two_primes(num):
    return any(is_prime(i) and is_prime(num - i) for i in range(2, num))

number = 10
if can_be_sum_of_two_primes(number):
    print(f"{number} може да бъде представено като сума от две прости числа.")
else:
    print(f"{number} не може да бъде представено като сума от две прости числа.")

# zad 7
import random

def create_matrix(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))

def sum_columns(matrix):
    if not matrix:
        print("Матрицата е празна.")
        return
    sums = [sum(row[j] for row in matrix) for j in range(len(matrix[0]))]
    
    print("Сумите по колони:")
    for j, column_sum in enumerate(sums, 1):
        print(f"Колона {j}: {column_sum}")

rows, cols = 3, 4
matrix = create_matrix(rows, cols)

print("Създадената матрица:")
print_matrix(matrix)
sum_columns(matrix)
