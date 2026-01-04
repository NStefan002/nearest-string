import random

__all__ = ['create_instance_file']


def _generate_central_string(m, alphabet):
    return ''.join(random.choice(alphabet) for _ in range(m))

def _perturb_string(s, max_changes, alphabet):
    s = list(s)
    positions = random.sample(range(len(s)), max_changes)

    for pos in positions:
        old = s[pos]
        choices = [c for c in alphabet if c != old]
        s[pos] = random.choice(choices)

    return ''.join(s)

def _generate_instance(n, m, alphabet, radius=None):
    """
    Ako je radius zadat:
        svi stringovi su na Hamming udaljenosti <= radius
        od skrivenog centralnog stringa
    Ako radius nije zadat:
        random instance
    """
    central = _generate_central_string(m, alphabet)
    strings = []

    for _ in range(n):
        if radius is None:
            s = _generate_central_string(m, alphabet)
        else:
            changes = random.randint(0, radius)
            s = _perturb_string(central, changes, alphabet)
        strings.append(s)

    return central, strings

def create_instance_file(n, m, alphabet, radius=None, output_file="input.txt"):
    central, strings = _generate_instance(n, m, alphabet, radius)

    with open(output_file, "w") as f:
        f.write(alphabet + "\n")
        for s in strings:
            f.write(s + "\n")

    print("Instance generated:")
    print(f"  n = {n}")
    print(f"  m = {m}")
    print(f"  alphabet = {alphabet}")
    if radius is not None:
        print(f"  hidden optimal radius ≤ {radius}")
        print(f"  (central string: {central})")
    print(f"  saved to: {output_file}")
