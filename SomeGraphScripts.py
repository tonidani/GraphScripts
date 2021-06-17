#AGR05 ANTONIO RODRIGUEZ
import copy, sys


#potrzebne do robienia kopii co iteracje algorytmu "krawedzi ciecia" bądź "mostu"


def make_data(file):
# otwieranie i wrzucanie do listy
    data = []

    for i in file:
        data.append(i.split())

    return data


def make_successor_dict(data):

    vertex = len(data)
    inf = float('inf')
    help_list = []
    count = 0
    successor_dict = {}

#zamiana - na inf oraz float
    i = 1
    while count < vertex:
        j = 0
        while j < vertex:
            if data[count][j] == '-':
                data[count][j] = 0
            else:
                data[count][j] = int(data[count][j])
                help_list.append(j+1)
            j += 1
        successor_dict[i] = help_list
        i += 1
        help_list = []
        count += 1

    return successor_dict


def make_float_weight_data(data):
#tworzenie macierzy wag
    vertex = len(data)
    float_weight_data = {}
    i=0

    while i < vertex:
        float_weight_data[i+1] = data[i]
        i += 1

    return float_weight_data


def make_dict_with_positions_of_weight(float_weight_data):
# Słownik, z wagami poszczególnych wierszy i kolumn (2gi wiersz wyjscia)
    inf = float('inf')
    dict_with_positions_of_weight = {}
    dict_of_dict_with_positions_of_weight = {}
    i = 1
    j = 0

    while i <= len(float_weight_data):
        while j < len(float_weight_data):
            if float_weight_data[i][j] != inf and float_weight_data[i][j] != 0:
                dict_with_positions_of_weight[j+1] = int(float_weight_data[i][j])
            j += 1
        j = 0
        dict_of_dict_with_positions_of_weight[i] = dict_with_positions_of_weight
        i += 1
        dict_with_positions_of_weight = {}

    return dict_of_dict_with_positions_of_weight


def make_edges(dict_of_dict_with_positions_of_weight):
#tworzy liste setów (nieuporząkowane) jezeli sa 2 takie same tzn ze jest krawedz
    help_list_of_set = []
    edges = []
    edges_tup = []

    for j in dict_of_dict_with_positions_of_weight:
        for i in dict_of_dict_with_positions_of_weight[j]:
            help_list_of_set.append({j,i})

    for i in help_list_of_set:
        if i not in edges:
            edges.append(i)

#usuwa powtórzone elementy , czyli wstawia tylko krawedzie
    for i in edges:
        edges_tup.append(tuple(i))

    return edges_tup

def make_edges_list(edges_tup):
#tworzy liste z krawedzi i je sortuje
    edges_list = []

    for x in edges_tup:
        edges_list.append(list(x))

    for i in edges_list:
        i.sort()

    return edges_list

def make_edges_with_weight(dict_of_dict_with_positions_of_weight, edges_tup):
#szuka wag poszczególnych krawedzi w slowniku wag
    edges_with_weight = {}

    for x in edges_tup:
        edges_with_weight[x] = dict_of_dict_with_positions_of_weight[x[0]][x[1]]

    return edges_with_weight


def BFS(successor_dict, s):
#funkcja zaczerpnięta z geeksforgeeks BFS Python
    visited = [False] * (len(successor_dict) + 1) # 15 + 1 omija błąd index out of range
    queue = []
    queue.append(s)
    visited[s] = True
    vertices = []

    while queue:
        s = queue.pop(0)
        vertices.append(s)
        for i in successor_dict[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return vertices

def bridge_edge(successor_dict, edges_list):

    for x in edges_list:
        successor_dict_copy = copy.deepcopy(successor_dict)
        v1 = x[0]
        v2 = x[1]
        successor = successor_dict_copy[v1]

        for v in successor:
            if v is v2:
                successor.remove(v)

        successor = successor_dict_copy[v2]
        for v in successor:
            if v is v1:
                successor.remove(v)

        bfs_vertices = BFS(successor_dict_copy, v1)
        if v2 in bfs_vertices:
            print('(v',v1,') -> (v',v2,') : no')
        else:
            print('(v',v1,') -> (v',v2,') : yes')



def floydWarshall(data):
    INF = float('inf')
    count = 1
    vertex = len(data)
    dist = copy.deepcopy(data)
    antecors = []
    row = []

#tworzy macierz poprzednikow
    for i in dist:
        for x in i:
            if x != INF:
                row.append(count)
            else:
                row.append("none")
        antecors.append(row)
        row = []
        count += 1

#floydWarshall
    count = 0
    for k in range(vertex):
        for i in range(vertex):
            for j in range(vertex):
                shortcut = dist[i][k] + dist[k][j]
                if shortcut < dist[i][j]:
                    dist[i][j] = shortcut
                    antecors[i][j] = antecors[k][j]
        if dist[i][i] < 0:
            print(" CYKL UJEMNY ! KONIEC PROGRAMU")
            sys.exit()

        print("W(",count,") =")

        for z in dist:
            print(z)
        print("\n")


        print("P(", count, ") =")

        for z in antecors:
            print(z)
        print("\n")

        count += 1


    print("ostateczna macierz odległości: ")
    for i in dist:
        print(i)

    print("\nostateczna macierz poprzedników: ")
    for i in antecors:
        print(i)


    return dist, antecors

def make_dict(dist):
    dist_dict = {}
    vertex = len(data)
    i = 0
    while i < vertex:
        dist_dict[i+1] = dist[i]
        i+=1
    return dist_dict



def prim(data):

    inner_graph = copy.copy(data)
    vertex = len(data)
    inf = float('inf')
    pos = 0
    i = 0
    z = 0
    y = 0
    weights = 0
    x = 0
    help_list = []
    visited = [0]
    print("rozpatrywany wierzcholek: ", pos + 1)
    #inicjalizacja
    while x < vertex:
        if inner_graph[z][x] == inf:
            if x == 0:
                help_list.append(['NONE', x])
            else:
                help_list.append(['NONE', inf])
        else:
            help_list.append([z+1,inner_graph[z][x]])
        x += 1
    print(help_list)

    while y < vertex-1:

                        i = visited[-1]
                        v = min(inner_graph[i])
                        weights += v
                        pos = inner_graph[i].index(v)
                        inner_graph[i][pos] = 100
                        inner_graph[pos][i] = 100
                        l=0
                        #print(inner_graph)
                        while l < vertex:

                            inner_graph[l][visited[-1]] = 100
                            l+=1
                        l=0


                        #print(visited)


                        print("rozpatrywany wierzcholek: ", pos + 1)

                        while z < len(inner_graph):
                            if inner_graph[pos][z] < help_list[z][1] and z not in visited:
                                help_list[z] = [pos+1, inner_graph[pos][z]]
                            z += 1
                        z = 0
                        print(help_list)

                        visited.append(pos)
                        y += 1

    print("wagi: ",weights)
    print("krawędzie: " )
    j = 0
    while j < len(visited):
        if j+1 != len(visited):
            print('(',visited[j]+1,',',visited[j+1]+1,')')
        else:
            break
        j+=1
        

def bridges(data, v, last, visited):

    helpik = []

    if data[visited[last-1]][v] == 0:
        return False

    for count in visited:
        helpik.append(count+1)

    print(helpik)
    helpik  = list()

    for vertex in visited:
        if vertex == v:
            return False
    
   
    return True
    

def Cycles(data, visited, last):
#funkcja zaczerpnięta z geeksforgeeks hamilton Python 

    if last == V:
        if data[visited[last-1]][visited[0]] == 1:
            return True
        else:
            return False

    for v in range(0, V):

        if bridges(data, v, last, visited) == True:
            visited[last] = v
            if Cycles(data, visited, last+1) == True:
                return True

        visited[last] = -1

    return False

def Hamilton(data, V):

    visited = [-1] * V
    visited[0] = 0
    
    if Cycles(data, visited,1) == False:
        print ("Nie ma cyklu hamiltona\n")
        return False

    print("CYKL HAMILTONA ")

    for vertex in visited:
        print(vertex + 1, end=" ")

    print(visited[0] + 1)

    return False



file = open('graph09.txt')
#AGR01 - funkcje z programu nr 1
data = make_data(file)
successor_dict = make_successor_dict(data)
#float_weight_data = make_float_weight_data(data)
#dict_of_dict_with_positions_of_weight = make_dict_with_positions_of_weight(float_weight_data)
#edges_tup = make_edges(dict_of_dict_with_positions_of_weight)
#edges_list = make_edges_list(edges_tup)
#edges_with_weight = make_edges_with_weight(dict_of_dict_with_positions_of_weight, edges_tup)
#print(edges_with_weight)
#AGR02 - funkcje z programu nr 2
#print("------Edge------ : If Bridge")
#bridge_edge(successor_dict, edges_list)

#AGR03  - FW
#print('floyd')
#dist, antecors = floydWarshall(data)
#dist_dict = make_dict(dist)
#antecors_dict = make_dict(antecors)

#AGR04 - prim
#prim(data)

#AGR05 - Hamilton

V = len(data)
Hamilton(data, V)


