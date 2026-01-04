import random
import argparse


def generate_central_string(m, alphabet):
    return ''.join(random.choice(alphabet) for _ in range(m))


def hamming_distance(a, b):
    return sum(x != y for x, y in zip(a, b))


def perturb_string(s, max_changes, alphabet):
    s = list(s)
    positions = random.sample(range(len(s)), max_changes)

    for pos in positions:
        old = s[pos]
        choices = [c for c in alphabet if c != old]
        s[pos] = random.choice(choices)

    return ''.join(s)


def generate_instance(n, m, alphabet, radius=None):
    """
    Ako je radius zadat:
        svi stringovi su na Hamming udaljenosti <= radius
        od skrivenog centralnog stringa
    Ako radius nije zadat:
        random instance
    """
    central = generate_central_string(m, alphabet)
    strings = []

    for _ in range(n):
        if radius is None:
            s = generate_central_string(m, alphabet)
        else:
            changes = random.randint(0, radius)
            s = perturb_string(central, changes, alphabet)
        strings.append(s)

    return central, strings


def main():
    parser = argparse.ArgumentParser(description="Generate Nearest String NP-hard instance")
    parser.add_argument("-n", type=int, required=True, help="number of strings")
    parser.add_argument("-m", type=int, required=True, help="length of each string")
    parser.add_argument("-a", type=str, required=True, help="allowed characters, e.g. 01 or ABC")
    parser.add_argument("-r", type=int, default=None, help="max Hamming distance from central string")
    parser.add_argument("-o", type=str, default="input.txt", help="output txt file")

    args = parser.parse_args()

    central, strings = generate_instance(
        args.n, args.m, list(args.alphabet), args.radius
    )

    with open(args.output, "w") as f:
        f.write(args.alphabet + "\n")
        for s in strings:
            f.write(s + "\n")

    print("Instance generated:")
    print(f"  n = {args.n}")
    print(f"  m = {args.m}")
    print(f"  alphabet = {args.alphabet}")
    if args.radius is not None:
        print(f"  hidden optimal radius ≤ {args.radius}")
        print(f"  (central string: {central})")
    print(f"  saved to: {args.output}")


if __name__ == "__main__":
    main()
