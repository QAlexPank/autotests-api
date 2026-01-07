from faker import Faker

fake = Faker('ru_RU')
for _ in range(10):
    print(fake.first_name_male())

user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=100),
    "address": fake.address()

}
print(user_data)
