# search employe details using id

employees = {
    101: {"Name": "Rahul", "Salary": 50000},
    102: {"Name": "Aman", "Salary": 45000}
}

emp_id = int(input("Enter employee id: "))

if emp_id in employees:
    print("Employee found:", employees[emp_id])
else:
    print("Employee not found")