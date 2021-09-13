"""
Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:
class Error1(Error2, Error3 ... ErrorK):
    pass


Антон написал код, который выглядит следующим образом.
try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...
Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого положения и напишите программу, которая будет определять обработку каких исключений можно удалить из кода.
Важное примечание:
В отличие от предыдущей задачи, типы исключений не созданы.
Создавать классы исключений также не требуется
Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее где-то поймали их предка.


Формат входных данных
В первой строке входных данных содержится целое число n - число классов исключений.
В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.
Формат выходных данных
Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.
Пример теста 1
Рассмотрим код
try:
   foo()
except ZeroDivision :
   print("ZeroDivision")
except OSError:
   print("OSError")
except ArithmeticError:
   print("ArithmeticError")
except FileNotFoundError:
   print("FileNotFoundError")


...


По условию этого теста, Костя посмотрел на этот код, и сказал Антону, что исключение FileNotFoundError можно не ловить, ведь мы уже ловим OSError -- предок FileNotFoundError
Sample Input:
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError
Sample Output:
FileNotFoundError
"""

#Создал класс для построения графа

class Graph: # Создаю класс графа
    def __init__(self):
        self. grapf = {}

    def add_node(self, node_name, parents):
        if node_name in self. grapf.keys():
        # если узел уже в графе, добавляем узлу родителей
            self. grapf [node_name].extend(parents)
        else:
          # иначе добавляем узел в граф и указываем его родителей
            self. grapf [node_name] = parents
        for p in parents:
           # проверяем есть ли узлы родителей в графе и если нет, добавляем узел без указания их родителей
            if p not in self. grapf.keys(): self.add_node(p, [])

    def is_parent(self, parent, node_name, ans='No'):
       # функция проверки является ли parent родителем node_name
        if parent == node_name or parent in self. grapf [node_name]:
          # проверка есть ли parent в родителях node_name на 1 и 2 уровнях
            return "Yes"
        else:
            for n in self. grapf [node_name]:
          # проверка есть ли parent в родителях node_name на 3 уровне
                if parent in self. grapf [n]:
                    return "Yes"
                else:
                 # проверка есть ли parent в родителях node_name рекурсией на более глубоких уровнях
                    ans = self.is_parent(parent, n)
                    if ans == 'Yes': return ans
        return ans

    def get_nodes(self):
        return self. grapf.keys()

    def read_data(self, data):
       # добавление узла и родителей через строку ввода
        node = [d.strip() for d in data.split(':')]
        parents = [p.strip() for p in node[1].split()] if len(node) > 1 else []
        self.add_node(node[0], parents)

grapf = Graph()
for i in range(int(input())):grapf.read_data(input())
exeptions = [input() for i in range(int(input()))]

nodes = grapf.get_nodes()
answer = {node: [] for node in nodes}
for parent in nodes:
    for child in nodes:
        result = grapf.is_parent(parent, child)
        if result == 'Yes':
            answer[parent].append(child)

for exeption in exeptions:
    if exeption in answer.keys():
        for child in answer[exeption]:
            if child != exeption and child in answer.keys(): del answer[child]
        del answer[exeption]
    else:
        print(exeption)
