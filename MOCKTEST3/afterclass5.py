arr = [37,51,44,23,78,92,39,84,83,51]
limit = 70

def min_pts(limit,arr):
    func = lambda pts: pts>=limit
    result = list(filter(func,arr))
    return result

print(min_pts(limit,arr))

