import jwt
import pyperclip


def main():
    try:
        key = input("input your secret key:\n>>> ")

        token = input("input your token:\n>>> ")

        decoded = jwt.decode(token, key, algorithms="HS256")

        pyperclip.copy(decoded.get('pwd'))

        print('The password to be copied to the clipboard.')
    except Exception:
        print("Something went wrong.")


if __name__ == "__main__":
    main()
