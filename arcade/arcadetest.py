from timeit import default_timer as timer
start = timer()
for x in range(1, 4444):
    print(x)
end = timer()
print('start = {} and end = {}'.format(start, end))