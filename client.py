import google.generativeai as genai

genai.configure(api_key="AIzaSyBiP3HJCO1KDGqkvlexosQDAQA-Pd16z74")

model = genai.GenerativeModel("gemini-2.5-flash")  # Valid model
response = model.generate_content("Hello, Gemini!")
print(response.text)
