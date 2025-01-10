def comanda(*args, **kwargs):
    print("Am primit comanda generala:")
    for _item in args:
        print(f"{_item}")

    print("\nAm primit comanda detaliata:")
    for _produs, _cantitate in kwargs.items():
        print(f"{_cantitate} x {_produs}")

comanda("fructe", "jucarii", mar = 3, banana = 2, jucarii = 5)

def magazin1(*args):
    for item in args:
        print(f"Avem {item} in magazin")

magazin1("mar", "banana", "biscuit")

def magazin2(**kwargs):
    for key, value in kwargs.items():
        print(f"Avem {value} {key}")

magazin2(pere=2, pepeni=3)

