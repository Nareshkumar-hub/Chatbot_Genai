from langchain.llms import GooglePalm
api_key = "AIzaSyBc0I2Cf1FW2xEgm6aI4OX7C2zOt2iazVU"
palm = Googlepalm(api_key=api_key, temperature=0.4)
text = palm("give me the list of name for my automation tool")
print(text)