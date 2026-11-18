
MULTIPLIER = 0xF0F0F0F1
MASK = 0xFFFFFFFF

def generate_keys(count=10):
    found = 0

    print("[*] Generating valid serial pairs...\n")

    for key in range(17, 0x100000000, 17):
        product = MULTIPLIER * key

        edx = (product >> 32) & MASK
        edx >>= 4

        ecx = (edx * 17) & MASK

        if key == ecx:
            second_key = ((key ^ 0x1337) + 0x2A) & MASK

            print(f"First key : {key:10d} (0x{key:08X})")
            print(f"Second key: {second_key:10d} (0x{second_key:08X})")
            print("-" * 40)

            found += 1

            if found >= count:
                break

generate_keys(10)
