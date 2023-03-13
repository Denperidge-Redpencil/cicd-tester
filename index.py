from requests import request

with open("index.py.txt", "w") as file:
    file.write(str(request(method="GET", url="https://github.com/")))
print("Succesful python run!")