from django.utils.crypto import get_random_string

def get_a_large_random_number():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    print(get_random_string(50, chars))

def main():
    get_a_large_random_number()
    
if __name__ == '__main__':
    main()
