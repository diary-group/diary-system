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



