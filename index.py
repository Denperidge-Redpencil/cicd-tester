from requests import request

with open("index.py.txt", "w") as file:
    file.write(str(request("https://github.com/")))
print("Succesful python run!")