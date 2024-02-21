from faker import Faker
import re

fake = Faker()
name = fake.name()

# Extract first name and last name from the generated name
first_name, last_name = re.findall(r'\w+', name)[:2]

# Derive email address using the first name and last name
email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"

# Generate introduction statement
introduction = f"My name is {name}. I am a {fake.job()}. And I am {fake.random_int(min=18, max=80)} years old."

print(introduction)
print(fake.address())
print(email)
print(f"I am originally from {fake.country()}")
print(fake.latitude(), fake.longitude())
print(fake.url())