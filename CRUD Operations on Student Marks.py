# CRUD means create read update delete

marks = []

# create
marks.append(80)
marks.append(75)
marks.append(90)

print("Student marks:", marks)

# update
marks[1] = 85
print("After update:", marks)

# delete
marks.remove(80)
print("After delete:", marks)