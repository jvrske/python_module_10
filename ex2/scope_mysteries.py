def mage_counter() -> callable:
    counter = 0

    def increment():
        nonlocal counter
        counter += 1
        return counter
    return increment


def spell_accumulator(initial_power: int) -> callable:
    def increment_power(power: int = 0) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power
    return increment_power


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key: str, value: str) -> None:
        vault.update({key: value})

    def recall(key: str) -> str:
        stored_value = vault.get(key)
        if stored_value is None:
            stored_value = "Memory not found"
        return stored_value

    return {'store': store,
            'recall': recall}


if __name__ == "__main__":
    count_mage = mage_counter()

    print("\nTesting mage counter...")
    for i in range(3):
        print(f"Call {i}:", count_mage())

    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print("\nTesting enchantment factory...")
    print(f"{flaming('Sword')}")
    print(f"{frozen('Shield')}")
