import subprocess
import matplotlib.pyplot as plt
import numpy as np
from tikzplotlib import save as tikz_save

#plt.style.use("fivethirtyeight")
#plt.style.use("ggplot")
plt.style.use("seaborn-whitegrid")

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

print()
print()

key_list = sorted([x for x in count_chars.keys()])
value_list = [count_chars.get(key) for key in key_list]

print("\\begin{tabular}{@{} cc @{}} % @{} removes white spaces \n \
        \\toprule \n \
        \\textsc{Character} & \\textsc{Occurrences} \\\\ \n \
        \\midrule")
for i in range(0, len(count_chars)):
    print("        " + key_list[i] + " & " + str(value_list[i]) + " \\\\")
print("    \\bottomrule \n \
\\end{tabular} ")

plt.bar(range(len(count_chars)), value_list, align='center')
plt.ylabel('Occurrences')
plt.yticks(np.arange(0, 1000001, 200000))
plt.xticks(range(len(count_chars)), key_list)

tikz_save(
    "fig/char_count.tex",
    axis_height='\\figH',
    axis_width='\\figW',
    extra_axis_parameters=["tick label style={font=\\footnotesize}", "ytick distance=200000"]
)

plt.show()

print()
print()

key_list = sorted([x for x in count_key_pairs.keys()])
value_list = [count_key_pairs.get(key) for key in key_list]

print("\\begin{tabular}{@{} cc @{}} % @{} removes white spaces \n \
        \\toprule \n \
        \\textsc{Character Pair} & \\textsc{Occurrences} \\\\ \n \
        \\midrule")
for i in range(0, len(count_key_pairs)):
    print("        " + key_list[i][0] + " + " + key_list[i][1] + " & " + str(value_list[i]) + " \\\\")
print("    \\bottomrule \n \
\\end{tabular} ")

print()
print()

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

    if value > 25000:
        freq_typed_key_pairs[key] = value

print(freq_typed_key_pairs)
print("double char:   " + str(count_double_char) + ", total: " + str(total_double_char))
print("double number: " + str(count_double_number) + ",   total: " + str(total_double_number))
print("char + number: " + str(count_char_number) + ", total: " + str(total_char_number))
print("number + char: " + str(count_number_char) + ", total: " + str(total_number_char))

key_list = sorted([x for x in freq_typed_key_pairs.keys()])
value_list = [freq_typed_key_pairs.get(key) for key in key_list]

plt.bar(range(len(freq_typed_key_pairs)), value_list, align='center')
plt.ylabel('Occurrences')
plt.yticks(np.arange(0, 175001, 25000))
plt.xticks(range(len(freq_typed_key_pairs)), key_list)

tikz_save(
    "fig/char_pair_count.tex",
    axis_height='\\figH',
    axis_width='\\figW',
    extra_axis_parameters=["tick label style={font=\\scriptsize}", "ytick distance=25000"]
)

plt.show()


key_list = sorted([x for x in count_key_pairs.keys()])
value_list = [count_key_pairs.get(key) for key in key_list]

print("Total amount of key pairs: " + str(len(count_key_pairs)))

plt.bar(range(len(count_key_pairs)), value_list, align='center')
plt.ylabel('Occurrences')
plt.yticks(np.arange(0, 175001, 25000))

tikz_save(
    "fig/char_pair_full_count.tex",
    axis_height='\\figH',
    axis_width='\\figW',
    extra_axis_parameters=["tick label style={font=\\scriptsize}", "ytick distance=25000", "xmajorticks=false", "xlabel={Character Pairs}"])

plt.show()

