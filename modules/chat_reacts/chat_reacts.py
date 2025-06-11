def chat_react_run(model, username=None, chat=None, test_mode=False):
    if test_mode:
        if username is None:
            username = generate_random_username()  # Or your default value
        if chat is None:
            chat = generate_random_chat()
    else:
        # In production, missing required data is an error!
        if username is None or chat is None:
            raise ValueError("Production mode: username and chat are required, an error has occured.")
    print(f"{username}: {chat}")
    # Optionally show debug info
    # print(f"Model received: {model}")
    # print(f"T
