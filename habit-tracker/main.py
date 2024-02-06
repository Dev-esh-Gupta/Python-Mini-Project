import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_NAME = "deveshgupta"
TOKEN = "kdjh34kdj3dkid"

user_params = {
    "token": "kdjh34kdj3dkid",
    "username": "deveshgupta",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Account is created by below post request
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
graph_config = {
    "id" : "graph1",
    "name" : "Coding Graph",
    "unit" : "Hours",
    "type" : "int",
    "color" : "kuro"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# Graph Creating is done by below line of code
# graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(graph_response.text)

POST_DATA_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/graph1"

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

data_params = {
    "date" : formatted_date,
    "quantity" : input("How many hours you code today ? : "),
}

# Work of posting is successful
add_data_response = requests.post(url=POST_DATA_ENDPOINT, json=data_params, headers=headers)
print(add_data_response.text)

# Updation can be done by PUT request

UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/graph1/{formatted_date}"

update_value = {
    "quantity" : "4"
}

# Updation is done by below code
# update_pixel = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_value, headers=headers)
# print(update_pixel.text)

# Its time to delete a pixel

DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/graph1/{formatted_date}"

# delete_pixel = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=headers)
# print(delete_pixel.text)