def f(uid):
    unique_id = []
    for id in uid:
        if id not in unique_id:
            unique_id.append(id)
        else:
            return False
    return True


print(f(["john5","ann123","JOHN5","xxx","abc333","a10"])) 
print(f(["abc123","ann","abc123","a10"]))
print(f(["bob2","bob2"]))
print(f(["bob2","BOB2"]) )