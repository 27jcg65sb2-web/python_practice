with open("users.txt","r") as f:
    lines=f.readlines()
users=[]



for line in lines:
    parts = line.strip().split(",")
    user={
        "name":parts[0],
        "age":int(parts[1])
    }
    users.append(user)
print(users)
for i in users:
    if i["age"]>=20:
        print(i["name"])
total = 0

for user in users:
    total += user["age"]

print(total / len(users))