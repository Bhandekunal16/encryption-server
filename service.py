class service:
    def hex(data):
        hexadecimal_str = data.encode().hex()
        return hexadecimal_str

    def decodeHex(data):
        output = bytes.fromhex(data).decode()
        return output
