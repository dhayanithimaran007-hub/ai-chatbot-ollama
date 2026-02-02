import ollama
messages=[]
print("World's fastest local bot is online🦅")
print("Give your commands🐧")
print("Press Q to exit🐲")
while True:
    user_input=input("You:")
    if user_input.lower() in ["exit","quit","q"]:
        print("Thank you for accessing me😘")
        break
    messages.append({"role":"user","content":user_input})
    messages=messages[-4:]
    response=ollama.chat(
        model="phi3",
        messages=messages
        )
    bot_reply=response["message"]["content"]
    messages.append({"role":"assistant","content":bot_reply})
    print("Bot🤖:",bot_reply)

    
