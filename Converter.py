
def convert_value(value):
    value = value.strip().lower()

    if value.startswith("0x"):
        value = value[2:]

    if not value:
        raise ValueError("Empty input")

    number = int(value, 16)

    if number > 0xFFFFFFFFFFFFFFFF:
        raise ValueError("Value exceeds 8 bytes (64 bits)")

    hex_value = f"{number:016X}"
    decimal_value = number

    raw_bytes = bytes.fromhex(hex_value)

    ascii_value = "".join(
        chr(b) if 32 <= b <= 126 else "."
        for b in raw_bytes
    )

    print(f"\nHexadecimal : 0x{hex_value}")
    print(f"Decimal     : {decimal_value}")
    print(f"ASCII       : {ascii_value}")
    print("-" * 40)


while True:
    try:
        user_input = input(
            "\nEnter hexadecimal value (or 'exit' to quit): "
        )

        if user_input.strip().lower() in ("exit", "quit"):
            print("Exiting...")
            break

        convert_value(user_input)

    except ValueError as e:
        print(f"Error: {e}")
