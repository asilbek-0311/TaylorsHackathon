# // make a script that will generate random number for 10 different varaibales and stores it in json file
import json
import random
import csv
import names

agents = []

def generate_kpi( quarter):
    quarter = f'Q{quarter:01}/24'
    avg_resp_time = round(random.uniform(0, 10000),2)
    avg_reso_time = round(random.uniform(20, 300), 2) if (avg_resp_time < 200) else round(random.uniform(300, 1200), 2)
    avg_contact_time = round(random.uniform(100, 1000), 2) if (avg_reso_time < 300) else round(random.uniform(500, 2000), 2)
    csat = random.randint(1, 5)
    tickets_total = random.randint(40, 200)
    tickets_done = random.randint(0, (tickets_total - 1))
    tickets_escalated = random.randint(0, (tickets_total - tickets_done))
    tickets_open = (tickets_total - tickets_done - tickets_escalated) 

    return {
        "quarter": quarter,
        "avg_resp_time": avg_resp_time,
        "avg_reso_time": avg_reso_time,
        "avg_contact_time": avg_contact_time,
        "csat": csat,
        "tickets_total": tickets_total,
        "tickets_done": tickets_done,
        "tieckts_escalated": tickets_escalated,
        "tickets_open": tickets_open
    }



for i in range(1, 21):
    employee_id = f"CS{i:07}"
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    kpi = []

    for quarter in range(1, 5):
        quarter_kpi = generate_kpi(quarter)
        kpi.append(quarter_kpi)
    


    employee = {
        "employee_id": employee_id,
        "first_name": first_name,
        "last_name": last_name,
        "kpi": kpi
    }
    agents.append(employee)


data = {"employees": agents}

    

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# with open('data.csv', 'w') as f:
#     fieldnames = ['employee_id', 'first_name', 'last_name', 'quarter', 'avg_resp_time', 'avg_reso_time', 'avg_contact_time', 'csat', 'tickets_total', 'tickets_done', 'tieckts_escalated', 'tickets_open']
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(agents)


# employee id
# first name
# last Name
# gender
