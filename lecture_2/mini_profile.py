def generate_profile(age):
    if age in range(0, 13):
        return str('Child')
    if age in range(13, 20):
        return str('Teenager')
    if age > 20:
        return str('Adult')


full_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = list()
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == 'stop':
        break
    else:
        hobbies.append(hobby)

life_stage = generate_profile(current_age)

user_profile = dict()
user_profile["name"] = full_name
user_profile["age"] = current_age
user_profile["stage"] = life_stage
user_profile["hobbies"] = hobbies

print(
    f"\n---\nProfile Summary:\nName: {user_profile['name']}\nAge: {user_profile['age']}\nLife Stage: {user_profile['stage']}")

if len(user_profile["hobbies"]) == 0:
    print("You didn't mention any hobbies")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):\n" + "\n".join('- ' + h for h in user_profile['hobbies']))
print('---')