from import_data import load_members, load_activities

members = load_members()
activities = load_activities()

print("=== MEMBERS LIST ===")
for m in members:
    m.display_info()

print("\n=== ACTIVITIES LIST ===")
for a in activities:
    a.display_summary()
