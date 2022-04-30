from datetime import datetime
from collections import Counter, defaultdict

start_time = datetime.now()
counted = Counter([i for i in range(1, 100001)])
end_time = datetime.now()
print('Duration with counter: {}'.format(end_time - start_time))

start_time = datetime.now()
countd = defaultdict(int)
for i in range(1, 100001):
    countd[i] += 1
end_time = datetime.now()
print('Duration with dictionary: {}'.format(end_time - start_time))