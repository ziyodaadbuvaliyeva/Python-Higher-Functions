from randomusers import randomusers_data

def get_email_list(users: list[dict]) -> list[str]:
    emails = []
    for user in users:
        emails.append(user["email"])
    return emails

def get_name_list(users: list[dict]) -> list[str]:
    pass

def get_country_list(users: list[dict]) -> list[str]:
    pass

def get_phone_list(users: list[dict]) -> list[str]:
    pass

def get_city_list(users: list[dict]) -> list[str]:
    pass

def get_oldest_user(users: list[dict]) -> dict:
    pass

def get_youngest_user(users: list[dict]) -> dict:
    pass


def main() -> None:
    results = randomusers_data["results"]

    email_list = get_email_list(results)
    print(email_list)

if __name__ == "__main__":
    main()
