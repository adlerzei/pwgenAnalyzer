import subprocess

out = subprocess.check_output(["pwgen", "-A", "8", "1000000"])
passwords = out.decode("utf-8").split("\n")
del passwords[-1]

chars = ["o", "h", "a", "i", "s", "e", "p", "t", "u", "c", "9", "1", "0", "4", "7"]
not_included = False
good_pws = []

for pw in passwords:
    not_included = False
    for char in pw:
        if char not in chars:
            not_included = True
            break
    if not_included:
        continue
    good_pws.append(pw)

print(good_pws)
