from django.utils.crypto import get_random_string


def main():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    print(get_random_string(50, chars))


if __name__ == '__main__':
    main()
