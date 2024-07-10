import re

def password_strength(password):
  
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[@$!%*?&#]', password) is not None

    
    strength = 0

    # Check each criteria
    if length_criteria:
        strength += 1
    if upper_criteria:
        strength += 1
    if lower_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if special_criteria:
        strength += 1

    # Feedback messages
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lower_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character (@$!%*?&#).")

    return strength, feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = password_strength(password)
    
    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Medium",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }
    
    print(f"Password Strength: {strength_levels[strength]}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")

if __name__ == "__main__":
    main()