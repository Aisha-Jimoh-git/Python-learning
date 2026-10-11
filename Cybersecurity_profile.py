print("===== CYBERSECURITY STUDENT PROFILE =====")
name = input("What is your name? ")
interest = input("What cybersecurity area interests you? ")
tool = input("What is your favourite cybersecurity tool? ")
while True:
    try:
        months = int(input("How many months have you been learning cybersecurity? "))
        if months < 0:
            print("Months cannot be negative. Please enter a positive number.")
            continue

        break
    
    except ValueError:
        print("Please enter the number of months using digits only.")
certification = input("What cybersecurity certifications are you currently pursuing? ")
experience = input("What is your current cybersecurity experience level? ")

if months < 6:
    message = "You are still building your cybersecurity foundation."
elif months < 12:
    message = "You are now developing your cybersecurity skills."
else:
    message = "You have been learning cybersecurity for a significant amount of time, well done!"

if experience.lower() == "beginner":
    advice = "Focus on networking fundamentals, Linux, and basic security concepts."
elif experience.lower() == "intermediate":
    advice = "Practise hands-on labs and build projects to strengthen your technical skills."
elif experience.lower() == "advanced":
    advice = "Explore complex security investigations and work on real-world security scenarios."
else:
    advice = "Keep learning, practising, and building your cybersecurity skills."

print()
print("===== YOUR PROFILE =====")
print("Name:", name)
print("Cybersecurity Interest:", interest)
print("Favourite Tool:", tool)
print("Learning Experience:", months, "months")
print("Certifications Pursuing:", certification)
print("Experience Level:", experience)
print("Message:", message)
print("Career Advice:", advice)