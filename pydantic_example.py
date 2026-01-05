from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    address: Address

user = User(
    id=1,
    name="Alice",
    email="alice@example.com",
    is_active=False,
    address={"city": "Moscow", "zip_code": "10001"}
)
print(user)
print(user.address.city)
