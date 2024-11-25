import requests

def fetch_ramdom_user_data():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)

    data = response.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        name = f"{user_data["name"]["title"]} {user_data["name"]["first"]} {user_data["name"]["last"]}"
        gender = user_data["gender"]
        email = user_data["email"]
        phone = user_data["phone"]
        country = user_data["location"]["country"]
        return name, gender, email, phone, country

    else:
        raise Exception("Failed to fetch user data :(")

def main():
    try:
        name, gender, email, phone, country = fetch_ramdom_user_data()
        print("\n----------------User Profile---------------- \n")
        print(f"Name : {name}")
        print(f"Gender : {gender}")
        print(f"Email : {email}")
        print(f"Phone : {phone}")
        print(f"Country : {country}")
        print("\n-------------------------------------------- \n")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()