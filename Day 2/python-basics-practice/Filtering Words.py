words = ["Antarctica","Zimbabwe","singapore","malaysia","peru","India","EU","Asia"]

print("Filtering Options:")
print("1. Words longer than a specified length")
print("2. Words shorter than a specified length")
print("3. Words starting with a specific letter")
print("4. Words containing a specific letter")

choice = input("Choose a filter (1-4): ")
filtered = []

if choice == "1":
    length = int(input("Minimum length: "))
    for word in words:
        if len(word) > length:
            filtered.append(word)

elif choice == "2":
    length = int(input("Maximum length: "))
    for word in words:
        if len(word) <= length:
            filtered.append(word)

elif choice == "3":
    letter = input("Enter starting letter: ").lower()
    for word in words:
        if word[0].lower() == letter:
            filtered.append(word)

elif choice == "4":
    letter = input("Enter letter to search for: ").lower()
    for word in words:
        if letter in word.lower():
            filtered.append(word)

else:
    print("Invalid choice")

print("\nFiltered Words:")
print(filtered)

