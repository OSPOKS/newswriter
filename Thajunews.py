import requests
import json

# Define the API endpoint
endpoint = "https://newsapi.org/v2/top-headlines?country=us&apiKey=<4cd6347c23954323b4811a814f86d535>"

# Fetch the latest news
response = requests.get(endpoint)

# Parse the JSON data
data = json.loads(response.text)

# Extract the news articles
articles = data["articles"]

# Loop through the articles and print their titles
for article in articles:
    print(article["title"])

# Publish the latest news on a website
with open("index.html", "w") as f:
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("<title>Latest News</title>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("<h1>Latest News</h1>\n")
    f.write("<ul>\n")
    for article in articles:
        f.write("<li>" + article["title"] + "</li>\n")
    f.write("</ul>\n")
    f.write("</body>\n")
    f.write("</html>\n")
