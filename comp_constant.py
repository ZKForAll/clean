
def bitfield(n):
    return [1 if digit=='1' else 0 for digit in bin(n)[2:]]

def pad(input, size):
    if len(input) < size:
        pad = [0] * (size - len(input))
        input = pad + input
    return input

def comp_constant(ct : int, input : list):
    # parts and sout are signals. How come they get assigned to?
    # output out
    # len(input) == 254
    # len(parts) == 127

    input = pad(input, 254)
    parts = [0] * 127
    # sout = 0

    clsb = 0
    cmsb = 0
    slsb = 0
    smsb = 0

    sum = 0

    b = (1 << 128) -1
    a = 1
    e = 1
    # i = 0

    for i in range(127):
        clsb = ((ct >> (i * 2))) & 1
        cmsb = ((ct >> (i * 2 + 1))) & 1
        slsb = input[i * 2]
        smsb = input[i * 2 + 1]

        if cmsb == 0 and clsb == 0:

            parts[i] = -b * smsb * slsb + b * smsb + b * slsb
        
        elif cmsb == 0 and clsb == 1: 
        
            parts[i] = a * smsb * slsb - a * slsb + b * smsb - a * smsb + a
        
        elif cmsb == 1 and clsb == 0:

            parts[i] = b * smsb * slsb - a * smsb + a

        else:
            parts[i] = -a * smsb * slsb + a

        sum = sum + parts[i]

        b -= e
        a += e
        e *= 2

    out = pad(bitfield(sum), 135)
    return out[127]

print(comp_constant(12, bitfield(12)))