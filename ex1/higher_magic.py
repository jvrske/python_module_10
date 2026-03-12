def spell_combiner(spell1: callable, spell2: callable) -> callable:
	return lambda target: (spell1(target), spell2(target))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
	return lambda: base_spell() * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
	return (lambda target: spell(target) if condition(target) else "Spell fizzled")


def spell_sequence(spells: list[callable]) -> callable:
	return lambda target: [spell(target) for spell in spells]


if __name__ == "__main__":
	test_val = [10, 14, 12]
	test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
	spells = {
		'fireball': lambda target: f'Fireball hits {target}',
		'heal': lambda target: f'Heals {target}',
		'lightning': lambda target: f'Lightning hits {target}',
		'explosion': lambda target: f'Explosion hits {target}',
		'fire arrow': lambda target: f'Fire Arrow hits {target}'
	}
	combined = spell_combiner(spells['fireball'], spells['heal'])
	combined_result = combined(test_targets[0])

	print("\nTesting spell combiner...")
	print(f"Combined spell result: {combined_result[0]}, {combined_result[1]}")

	power_amp = power_amplifier(lambda: test_val[0], 3)
	print("\nTesting power amplifier...")
	print(f"Original: {test_val[0]}, Amplified: {power_amp()}")
