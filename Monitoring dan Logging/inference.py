import json
import requests

url = "http://127.0.0.1:5001/invocations"

with open(r"C:\Users\LENOVO\Documents\Eksperimen_SML_Azizah_Salma_Ayunisa_Purnomo\preprocessing\mlruns\167048665530771541\792374292ac34a399f2b07d2303acd12\artifacts\input_example.json") as f:
    data = json.load(f)
    
payload = {
    "inputs" : data
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())