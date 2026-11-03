import requests
import json

API_KEY = "8216f4117077f98f9a166a292aefb603"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)

    temperature = data["main"]["temp"]
    condition = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print("\n--- Weather Report ---")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Condition:", condition)
    print("Humidity:", humidity, "%")

else:
    print("\nError:", response.status_code)
    print("Details:", response.text)
