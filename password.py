import random
import math

chars = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
special = "!;[]/?-+=@#$%&*"
pass_len = int(input("Enter Password Length"))
if pass_len < 8:
    print("\nPassword Length must be atleast 8")
    exit()
elif pass_len > 32:
    print("\nPassword Length must be less than 32")
    exit()
chars_len = pass_len // 2
num_len = math.ceil(pass_len * 30 / 100)
special_len = pass_len - (chars_len + num_len)


def generate_randoms(length, array, chars=False):
    result = []
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if chars:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        result.append(character)
    return result


buffer = []
buffer.extend(generate_randoms(chars_len, chars, True))
buffer.extend(generate_randoms(num_len, nums))
buffer.extend(generate_randoms(special_len, special))
random.shuffle(buffer)
password = "".join([str(i) for i in buffer])
print("\nGenerated Password:\n")
print(password)
