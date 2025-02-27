# from collections import defaultdict
# d = defaultdict(list)
# # print(d)
# # defaultdict(<class 'list'>, {})
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)
# # ('python', ['awesome', 'language'])
# # ('something-else', ['not relevant'])

# n and m int
# n words which might repeat, in word group A
# m words belonging to word group B


####

from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    d[input()].append(str(i + 1))
for j in range(m):
    print(' '.join(d[input()]) or -1)