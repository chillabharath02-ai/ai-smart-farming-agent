from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def farming_agent(query):
    prompt = f"""
    You are an expert agriculture advisor.

    Farmer query:
    {query}

    Give:
    1. Best crop recommendation
    2. Reason
    3. Step-by-step farming plan
    4. Expected profit
    5. Disease prevention tips
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


while True:
    q = input("Enter farming query (type exit to stop): ")

    if q.lower() == "exit":
        break

    print("\n🌱 Advice:\n", farming_agent(q))
