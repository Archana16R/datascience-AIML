#how sets handle uniqueness and perform membership testing.
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)

print("Is ID05 a unique user?")
print("ID05" in unique_users)

print("\nCount comparison:")
print("Total log entries:", len(raw_logs))
print("Unique users:", len(unique_users))

print("\nUnique User IDs:")
print(unique_users)
