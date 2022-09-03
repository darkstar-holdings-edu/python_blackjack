def user_option_handler(message: str, valid_options: list[str]) -> str:

    user_response = None
    while True:
        user_response = input(message)
        if user_response not in valid_options:
            print("huh?")
            continue

        break

    return user_response
