from randomuser import randomuser_data

def get_email_list(users: list[dict]) -> list[str]:
    pass
    emails=[]
    for user in users:
        emails.append(user['email'])
        return emails

def get_name_list(users: list[dict]) -> list[str]:
    pass
    names=[]
    for user in users:
        full_name=f'{user['name']['first']}{user['name']['last']}'
        names.append(full_name)
        return names

def get_country_list(users: list[dict]) -> list[str]:
    pass
countries=[]
for user in users:
    countries.append(user['location']['country']
                     return countries
def get_phone_list(users: list[dict]) -> list[str]:
    pass
    phones=[]
    for user in users:
        phones.append(user['phone])
                      return phones

def get_city_list(users: list[dict]) -> list[str]:
    pass
cities=[]
for user in users:
cities.append(user['location']['city'])
return cities
def get_oldest_user(users: list[dict]) -> dict:
    pass
oldest=users[0]
for user in users:
if user['date of birth']['age']>oldest['date of birth']['age']:
oldest=user
return oldest
def get_youngest_user(users: list[dict]) -> dict:
    pass
youngest=users[0]
for user in users:
if user['date of birth']['age']<youngest['date of birth']['age']:
youngest=user
return youngest
def get_oldest_user(users: list[dict]) -> dict:
    pass
for user in users:
min_age=min(user['age'])
for user in users:
if user['age']min_age:
return user
def main() -> None:
    pass
    print('randomusers')
if __name__ == "__main__":
    main()
