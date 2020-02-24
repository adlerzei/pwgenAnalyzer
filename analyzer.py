import subprocess
import matplotlib.pyplot as plt

out = subprocess.check_output(["pwgen", "-A", "8", "1000000"])
passwords = out.decode("utf-8").split("\n")
del passwords[-1]

count_chars = {}
count_key_pairs = {}

for pw in passwords:
    last_char = ""
    for char in pw:
        # count keys
        if char not in count_chars:
            count_chars[char] = 0
        count_chars[char] += 1

        # count key pairs
        if last_char == "":
            last_char = char
        else:
            if last_char+char not in count_key_pairs:
                count_key_pairs[last_char+char] = 0
            count_key_pairs[last_char+char] += 1
            last_char = char

print(count_chars)
print(count_key_pairs)
print(sorted(count_key_pairs.items(), key=
             lambda kv: (kv[1]), reverse=True))

plt.bar(range(len(count_chars)), count_chars.values(), align='center')
plt.xticks(range(len(count_chars)), list(count_chars.keys()))

plt.show()

count_double_number = 0
count_char_number = 0
count_number_char = 0
count_double_char = 0
total_double_number = 0
total_char_number = 0
total_number_char = 0
total_double_char = 0

freq_typed_key_pairs = {}
for key, value in count_key_pairs.items():
    if str.isdigit(key[0]) & str.isdigit(key[1]):
        count_double_number += 1
        total_double_number += value
    if str.isalpha(key[0]) & str.isdigit(key[1]):
        count_char_number += 1
        total_char_number += value
    if str.isdigit(key[0]) & str.isalpha(key[1]):
        count_number_char += 1
        total_number_char += value
    if str.isalpha(key[0]) & str.isalpha(key[1]):
        count_double_char += 1
        total_double_char += value

    if value > 20000:
        freq_typed_key_pairs[key] = value

print(freq_typed_key_pairs)
print("double char:   " + str(count_double_char) + ", total: " + str(total_double_char))
print("double number: " + str(count_double_number) + ",   total: " + str(total_double_number))
print("char + number: " + str(count_char_number) + ", total: " + str(total_char_number))
print("number + char: " + str(count_number_char) + ", total: " + str(total_number_char))

plt.bar(range(len(freq_typed_key_pairs)), freq_typed_key_pairs.values(), align='center')
plt.xticks(range(len(freq_typed_key_pairs)), list(freq_typed_key_pairs.keys()))

plt.show()
