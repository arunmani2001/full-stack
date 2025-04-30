import openai
openai.api_key = 'your_openai_api_key'

def extract_info_from_rtc(text_content):
    prompt = f"Extract the Year and Owner Name from this RTC document:\n{text_content}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response['choices'][0]['message']['content']
    year_line, owner_line = answer.split('\n')
    year = year_line.split(':')[1].strip()
    owner = owner_line.split(':')[1].strip()
    return year, owner