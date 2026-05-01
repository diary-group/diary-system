# =========================================
# DIARY SYSTEM - GROUP ACTIVITY (GITHUB)
#
# STUDENT A - X MODE: Initialize file (PUSH)
# STUDENT B - W MODE: Write initial data (CLONE/PUSH)
# STUDENT C - A MODE: Append entries (PULL/PUSH)
# STUDENT D - R MODE: Read + count entries (PULL/PUSH)
# =========================================


# ================================
# STUDENT A - INITIALIZE FILE (X MODE)
# Git Action: PUSH
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
# STUDENT B - WRITE MODE (W)
# Git Action: CLONE + PUSH
# Task: Write initial data
# ================================
entry_b = input("Student B - Enter initial log entry: ")

f = open("diary.txt", "a")
f.write("2. " + entry_b + "\n")
f.close()

print("Student B: Initial data written.\n")


# ================================
# STUDENT C - APPEND MODE (A)
# Git Action: PULL + PUSH
# Task: Append multiple entries
# ================================
entry_c = input("Student C - Add log entry: ")

f = open("diary.txt", "a")
f.write("3. " + entry_c + "\n")
f.close()

print("Student C: Entry appended.\n")


# ================================
# STUDENT D - READ MODE (R)
# Git Action: PULL + PUSH
# Task: Read file and count entries
# ================================
f = open("diary.txt", "r")
lines = f.readlines()
f.close()

print("=== STUDENT D OUTPUT ===")
print("Diary Contents:\n")

for i, line in enumerate(lines, start=1):
    print(i, line.strip())

print("\nTotal entries:", len(lines))
print("Student D: Read complete.\n")