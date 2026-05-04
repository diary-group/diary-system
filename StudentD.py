f = open("diary.txt", "r")
lines = f.readlines()
f.close()

print("=== STUDENT D (VELEZ) OUTPUT ===")
print("Diary Contents:\n")

for i, line in enumerate(lines, start=1):
    print(i, line.strip())

print("\nTotal entries:", len(lines))
print("Student D (VELEZ): Read complete.\n")
