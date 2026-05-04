entry_b = input("Student B (TUPAG) - Enter initial log entry: ")

f = open("diary.txt", "a")
f.write("2. " + entry_b + "\n")
f.close()

print("Student B (TUPAG): Initial data written.\n")