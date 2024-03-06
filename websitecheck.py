import requests

def is_secure_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.url.startswith("https://")
    except requests.exceptions.RequestException:
        return False
    
if __name__ == "__main__":
    while True:
        website_url = input("Enter the website URL (or type 'exit' to quit):  ")

        if website_url.lower() == "exit":
            break

        try:
            if not website_url.startswith("https://"):
                website_url = "https://" + website_url
            if is_secure_website(website_url):
                print(f"{website_url} is a secure website!")
            else:
                print(f"{website_url} is NOT a secure website!")
        except:
            print("Invalid URL format. Try again!")