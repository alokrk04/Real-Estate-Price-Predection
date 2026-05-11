import google.generativeai as genai

API_KEY =
"AIzaSyCvnsxyM7yefjnFOGJpHkFzqxBHzpo20"
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

response = chat.send_message("hello")
print("Gemini :",response.text)