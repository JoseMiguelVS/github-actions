import os

username = os.getenv("USERNAME")
print(f"El nombre de usuario es: {username}")

for i in [1, 2, 3]:
    print(f"{ username}" * 1)