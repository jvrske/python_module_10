def mage_counter() -> callable:
	counter = 0

	def increment():
		nonlocal counter
		counter += 1
		return counter
	return increment


def spell_accumulator(initial_power: int) -> callable:
	pass


def enchantment_factory(enchantment_type: str) -> callable:
	pass


def memory_vault() -> dict[str, callable]:
	pass


if __name__ == "__main__":
	count_mage = mage_counter()

	print("\nTesting mage counter...")
	for i in range(3):
		print(f"Call {i}:", count_mage())

	print("\n Testing enchantment factory...")
