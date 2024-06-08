# // make a script that will generate random number for 10 different varaibales and stores it in json file
import json
import random

metrics = ['employee_id', 'name', 'avg_rsp_time', 'avg_rsl_time', 'fst_contact_res_rt', 'csat', 'nps', 'ticket_vlm', 'ticket_backlog', 'agent_utalization_rate', 'escalation_rate', 'resolution_rate']
agents = []


for i in range(1, 21):
    employee = {
        "Employee_ID": i,
        "Name": f"Employee_{i}",
        "Average Response Time (min)": round(random.uniform(0, 5), 2),
        "Average Resolution Time (min)": round(random.uniform(30, 60), 2),
        "First Contact Resolution Rate (%)": round(random.uniform(40, 80), 2),
        "Customer Satisfaction Score (CSAT)": round(random.uniform(1.0, 5.0), 2),
        "Net Promoter Score (NPS)": round(random.uniform(30, 70), 2),
        "Ticket Volume": random.randint(100, 300),
        "Ticket Backlog": random.randint(0, 30),
        "Agent Utilization Rate (%)": round(random.uniform(70, 90), 2),
        "Escalation Rate (%)": round(random.uniform(5, 15), 2),
        "Resolution Rate (%)": round(random.uniform(80, 95), 2)
    }
    agents.append(employee)


data = {"employees": agents}

    

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)


# employee id
# first name
# last Name
# gender
