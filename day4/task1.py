#dictionary creation, updating, and safe data retrieval using .get()
contacts = {
    "Archana": 9876543210,
    "Ravi": 9123456789,
    "Sneha": 9988776655
}

contacts["Anil"] = 9012345678

contacts["Ravi"] = 9000011111

print("Lookup existing contact:")
print("Archana:", contacts.get("Archana", "Contact not found"))

print("\nLookup non-existing contact:")
print("Kiran:", contacts.get("Kiran", "Contact not found"))

print("\n Contact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
