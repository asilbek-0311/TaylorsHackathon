# import openai

# system_content = "You are a travel agent. Be descriptive and helpful."
# user_content = "Tell me about San Francisco"

# client = openai.OpenAI(
#     api_key="c541ad3ecf394b7dadf603071211c251",
#     base_url="https://api.aimlapi.com",
# )

# chat_completion = client.chat.completions.create(
#     model="mistralai/Mistral-7B-Instruct-v0.2",
#     messages=[
#         {"role": "system", "content": '''
#         You will be provided with data from customer service employees, using the data evaluate the following:

#         Agent KPI
#         Key performance metrics
#         Wether they have improved or worsened in performance
#         What may have caused that difference
#         Give pointers for each individual employee and what can be done to improve their performance in the future
#          '''
#          },
        
#         {"role": "user", "content": 
#          '''
#             "Employee_ID": 1,
#             "Name": "CS001",
#             "Average Response Time (min)": 0.36,
#             "Average Resolution Time (min)": 58.9,
#             "First Contact Resolution Rate (%)": 59.63,
#             "Customer Satisfaction Score (CSAT)": 1.14,
#             "Net Promoter Score (NPS)": 41.3,
#             "Ticket Volume": 134,
#             "Ticket Backlog": 20,
#             "Agent Utilization Rate (%)": 73.15,
#             "Escalation Rate (%)": 8.86,
#             "Resolution Rate (%)": 92.09
#          '''},
#     ],
#     temperature=0.7,
#     max_tokens=128,
# )

# response = chat_completion.choices[0].message.content
# print("AI/ML API:\n", response)

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.aimlapi.com",
)
system_content = '''
        You will be provided with data from customer service employees, using the data evaluate the following:

        Agent KPI
        Key performance metrics
        Wether they have improved or worsened in performance
        What may have caused that difference
        Give pointers for each individual employee and what can be done to improve their performance in the future
        '''
user_content = ''' 
            "Employee_ID": 1,
            "Name": "CS001",
            "Average Response Time (min)": 0.36,
            "Average Resolution Time (min)": 58.9,
            "First Contact Resolution Rate (%)": 59.63,
            "Customer Satisfaction Score (CSAT)": 1.14,
            "Net Promoter Score (NPS)": 41.3,
            "Ticket Volume": 134,
            "Ticket Backlog": 20,
            "Agent Utilization Rate (%)": 73.15,
            "Escalation Rate (%)": 8.86,
            "Resolution Rate (%)": 92.09
            '''

response = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=[
        {
            "role": "system",
            "content": system_content
        },
        {
            "role": "user",
            "content": user_content
        },
    ],
)

message = response.choices[0].message.content
print(f"Assistant: {message}")