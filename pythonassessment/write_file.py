file = open("student_notes.txt", "w")

file.write("This is a file containing student notes.\n")
file.write("Python is fun and easy to learn.\n")
file.write("We are learning file handling now.")

file.close()

print("Content written to student_notes.txt successfully.")
