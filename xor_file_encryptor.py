import itertools
import argparse
import hashlib

def xor_hex_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, itertools.cycle(b2)))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('key')
    parser.add_argument('output_file')

    args = parser.parse_args()

    with open(args.input_file, 'rb') as f:
        input_data = f.read()

    input_checksum = hashlib.md5(input_data).hexdigest()
    print(f"Checksum: {input_checksum}")

    key = args.key.encode()
    xor_result = xor_hex_bytes(input_data, key)

    with open(args.output_file, 'wb') as f:
        f.write(xor_result)

if __name__ == "__main__":
    main()
