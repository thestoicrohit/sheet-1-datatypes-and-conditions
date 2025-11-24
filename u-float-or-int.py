s = input().strip()

if '.' in s:
    int_part, dec_part = s.split('.')
    if int(dec_part) == 0:
        print("int", int(int_part))
    else:
        print("float", int(int_part), "0." + dec_part)
else:
    print("int", int(s))
