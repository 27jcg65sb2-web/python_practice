def load_users(filename):
    with open(filename,"r")as f:
        lines = f.readlines()
    users=[]
    for line in lines:
        
        sumples=line.strip().split(",")

        user={
            "name":sumples[0],
            "age":int(sumples[1])
        }
        users.append(user)
    return users
def print_adult_users(users):
    for user in users:
        if user["age"] >= 20:
            print(user["name"])
def is_adult(user):
    return user["age"] >= 20

users=load_users("users.txt")

print_adult_users(users)
        
for user in users:
    if is_adult(user):
        print(user["name"])
