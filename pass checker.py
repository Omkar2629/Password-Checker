import re
def validate_minimum_requirements(password):
    errors = []
    if len(password) < 8:
        errors.append("• At least 8 characters long")
    if not re.search(r'[A-Z]', password):
        errors.append("• At least 1 uppercase letter (A–Z)")
    if not re.search(r'[a-z]', password):
        errors.append("• At least 1 lowercase letter (a–z)")
    if not re.search(r'[0-9]', password):
        errors.append("• At least 1 digit (0–9)")
    if not re.search(r'[@#]', password):
        errors.append("• At least 1 special character (@ or #)")
    return errors
def password_strength(password):
    score = 0
    length = len(password)
    if length >= 8: score += 25
    if length >= 12: score += 10
    if length >= 16: score += 10
    if re.search(r'[A-Z]', password): score += 15
    if re.search(r'[a-z]', password): score += 15
    if re.search(r'[0-9]', password): score += 15
    if re.search(r'[@#]', password): score += 10

    return min(score, 100)
def strength_comment(score):
    if score < 40:
        return "❌ Weak — Easily hackable"
    elif score < 70:
        return "🟡 Moderate — Could be hacked"
    elif score < 90:
        return "🟢 Strong — Hard to hack"
    else:
        return "💪 Very Strong — Nearly unbreakable"

while True:
    password = input("Create password: ")
    errors = validate_minimum_requirements(password)
    if errors:
        print("\n❌ Password does NOT meet the required standards:")
        for err in errors:
            print(err)
        print("\n➡ Please try again.\n")
        continue
    score = password_strength(password)
    print(f"\n✔ Password meets minimum criteria!")
    print(f"Password Strength: {score}%")
    print(strength_comment(score))
    break