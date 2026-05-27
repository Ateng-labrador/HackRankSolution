E = int(input())
English_people = map(int, input().split())
English_people_set = set(English_people)

F = int(input())
Franch_people = map(int, input().split())
Franch_people_set = set(Franch_people)

x = English_people_set.difference(Franch_people_set)
print(len(x))