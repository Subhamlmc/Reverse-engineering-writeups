def generate_key(username):
 ascii_sum = sum(ord(c) for c in username)
 final_key = (ascii_sum * 0x539) ^ 0x5A5A
 print(f"Serial Key for {username}: {final_key}")
# Example: AAAAAAA -&gt; 594453
generate_key("subham")