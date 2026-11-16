
def convert_value(value):
    value = value.strip().lower()

    if value.startswith("0x"):
        value = value[2:]

    if not value:
        raise ValueError("Empty input")

    number = int(value, 16)

    if number < 0 or number > 0xFFFFFFFFFFFFFFFF:
        raise ValueError("Value exceeds 8 bytes")

    hex_value = f"{number:016X}"
    decimal_value = number

    raw_bytes = bytes.fromhex(hex_value)

    ascii_value = "".join(
        chr(b) if 32 <= b <= 126 else "."
        for b in raw_bytes
    )

    print(f"Hexadecimal : 0x{hex_value}")
    print(f"Decimal     : {decimal_value}")
    print(f"ASCII       : {ascii_value}")

user_input=(input("Enter a hexadecimal value (with or without 0x prefix): "))
convert_value(user_input)
