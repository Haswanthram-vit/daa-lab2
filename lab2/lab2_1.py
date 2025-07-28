import random
import string
import os

def generate_name():
    names=['Alice','Lois','Peter','Mike','Ben','Joe','Phil','Luke']
    return random.choice(names)

def generate_department():
    departments=['HR','Finance','Engineering','Sales','Marketing']
    return random.choice(departments)

def generate_salary():
    return round(random.uniform(30000,150000),2)

def create_employee_record(emp_id):
    return f"{emp_id} {generate_name()} {generate_department()} {generate_salary()}\n"

def generate_files(size):
    base_ids=list(range(1,size+1))
    
    #asc
    with open(f"ascending_employees_{size}.txt","w") as f:
        for emp_id in base_ids:
            f.write(create_employee_record(emp_id))

    #des
    with open(f"descending_employees_{size}.txt","w") as f:
        for emp_id in reversed(base_ids):
            f.write(create_employee_record(emp_id))
    
    #avg
    shuffled_ids=base_ids.copy()
    random.shuffle(shuffled_ids)
    with open(f"random_employees_{size}.txt","w") as f:
        for emp_id in shuffled_ids:
            f.write(create_employee_record(emp_id))

if __name__=="__main__":
    for size in [5000,10000,20000]:
        generate_files(size)