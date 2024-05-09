import random

char_pool = [chr(x) for x in range(49, 127)]
random.shuffle(char_pool)
print(char_pool)

print(''.join(random.sample(char_pool, 12)))