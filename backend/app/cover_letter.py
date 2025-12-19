import os, openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_cover_letter(data):
    prompt = f"Write a short cover letter for {data['job']} using skills {data['skills']}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"cover_letter": response.choices[0].message.content}
