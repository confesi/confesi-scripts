import json
import requests

# Get the data from the API

# {
#     "error": null,
#     "value": [
#       {
#         "text": "A",
#         "replies": 5,
#         "children": [
#           {
#             "text": "B",
#             "replies": 2,
#             "children": [
#               {
#                 "text": "G",
#                 "replies": 2,
#                 "children": []
#               }
#             ]
#           },
#           {
#             "parent_post": "EXi4jzwC8ABJAS-KcAzqjg",
#             "text": "D",
#             "replies": 2,
#             "children": []
#           },
#           {
#             "parent_post": "EXi4jzwC8ABJAS-KcAzqjg",
#             "text": "R",
#             "replies": 1,
#             "children": []
#           },
#           {
#             "parent_post": "EXi4jzwC8ABJAS-KcAzqjg",
#             "text": "C",
#             "replies": 0,
#             "children": []
#           },
#           {
#             "parent_post": "EXi4jzwC8ABJAS-KcAzqjg",
#             "text": "T",
#             "replies": 0,
#             "children": []
#           }
#         ]
#       }
#     ]
#   }
  
# A -> B or A -> c or A -> D or A-> R or A -> T
# B -> G or B -> E
# E -> F
# F -> H or F -> I
# H -> N or H -> O
# G -> J or G -> K
# J -> M
# K -> L
# D -> P or D -> Y
# P -> X or P -> U or P -> V or P -> W
# W -> T
# R -> S

def check_children_names(data_children: list, expected_children: list):
    for data_child in data_children:
        if data_child["text"] in expected_children:
            continue
        else: 
            return False
    return True



def check_data(data1) -> bool:
    for data in data1:
        if (data["text"] == "A" and check_children_names(data["children"], ["B", "C", "D", "R", "T"])) or (data["text"] == "B" and check_children_names(data["children"], ["G", "E"])) or (data["text"] == "E" and check_children_names(data["children"], ["F"])) or (data["text"] == "F" and check_children_names(data["children"], ["H", "I"])) or (data["text"] == "H" and check_children_names(data["children"], ["N", "O"])) or (data["text"] == "G" and check_children_names(data["children"], ["J", "K"])) or (data["text"] == "J" and check_children_names(data["children"], ["M"])) or (data["text"] == "K" and check_children_names(data["children"], ["L"])) or (data["text"] == "D" and check_children_names(data["children"], ["P", "Y"])) or (data["text"] == "P" and check_children_names(data["children"], ["X", "U", "V", "W"])) or (data["text"] == "W" and check_children_names(data["children"], ["T"])) or (data["text"] == "R" and check_children_names(data["children"], ["S"])):
            check_data(data['children'])
        else: 
            return False
    return True

payload = {
  "kind": "root",
  "sort": "best",
  "parent": "X7lggPyFb7-ec3PrGd_kWw",
  "seen": []
}
header = {
    "Accept": "*/*",
"User-Agent": "Thunder Client (https://www.thunderclient.com)"

}
for i in range(1, 10):
    url = "http://localhost:3000/comments/"
    response = requests.get(url, json=payload)
    data = response.json()["value"]
    if check_data(data):
        print("True")
    else:
        # print(data)
        print("False")
        pass