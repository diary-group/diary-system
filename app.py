# =========================================
# DIARY SYSTEM - GROUP ACTIVITY (GITHUB)
#
# Student A: Initialization (X mode)
# Student B: TUPAG - Write (W mode)
# Student C: MIJE - Append (A mode)
# Student D: VELEZ - Read (R mode)
# =========================================


# ================================
# STUDENT A - INITIALIZATION (X MODE)
# Task: Create shared project file
# ================================
try:
    f = open("diary.txt", "x")
    f.close()
except:
    pass

f = open("diary.txt", "w")
f.write("1. Project Initialized by Student A\n")
f.close()

print("Student A: File initialized.\n")


# ================================
# STUDENT B - TUPAG (W MODE)
# Task: Write initial data
# ================================
entry_b = input("Student B (TUPAG) - Enter initial log entry: ")

f = open("diary.txt", "a")
f.write("2. " + entry_b + "\n")
f.close()

print("Student B (TUPAG): Initial data written.\n")


# ================================
# STUDENT C - MIJE (A MODE)
# Task: Append multiple entries
# ================================
entry_c = input("Student C (MIJE) - Add log entry: ")

f = open("diary.txt", "a")
f.write("3. " + entry_c + "\n")
f.close()

print("Student C (MIJE): Entry appended.\n")


# ================================
# STUDENT D - VELEZ (R MODE)
# Task: Read file and count entries
# ================================
f = open("diary.txt", "r")
lines = f.readlines()
f.close()

print("=== STUDENT D (VELEZ) OUTPUT ===")
print("Diary Contents:\n")

for i, line in enumerate(lines, start=1):
    print(i, line.strip())

print("\nTotal entries:", len(lines))
print("Student D (VELEZ): Read complete.\n")