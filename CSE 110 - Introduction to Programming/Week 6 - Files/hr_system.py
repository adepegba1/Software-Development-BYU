"""
The program should iterate through each line of this file, 
gather the information from each field and display the values in this 
format: name (ID: id_number), job_title - $salary. 
Don't forget to convert the salary to a number and display it with two decimals.
"""
with open("hr_system.txt") as payroll:
    # next(payroll) -- Skip the first line of the file
    name = ""
    id  = ""
    title = ""
    salary = 0
    header_row = payroll.readline().strip()
    for list in payroll:
        information = list.split(" ")
        name = information[0]
        id = information[1]
        title = information[2]
        salary = float(information[3])
        paycheck = salary / 24
        if title == "Engineer":
            print(f"{name} (ID: {id}), {title} - ${1000 + paycheck:.2f}.")
        else:
            print(f"{name} (ID: {id}), {title} - ${paycheck:.2f}.")
