def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(artifacts, key=lambda x: x["power"])
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages = list(filter(lambda x: x["power"] >= min_power, mages))
    return filtered_mages


def spell_transformer(spells: list[str]) -> list[str]:
    prefix = '* '
    suffix = ' *'
    spells_map = list(map(lambda x: prefix + x + suffix, spells))
    return spells_map


def mage_stats(mages: list[dict]) -> dict:
    most_powerful = max(mages, key=lambda x: x["power"])
    least_powerful = min(mages, key=lambda x: x["power"])
    average_power = sum([mage.get('power') for mage in mages]) / len(mages)

    return {'max_power': most_powerful.get('power'),
            'min_power': least_powerful.get('power'),
            'avg_power': f'{average_power:.2f}'}


if __name__ == "__main__":
    artifacts = [
        {'name': 'Fire Staff', 'power': 68, 'type': 'relic'},
        {'name': 'Earth Shield', 'power': 88, 'type': 'armor'},
        {'name': 'Light Prism', 'power': 113, 'type': 'armor'},
        {'name': 'Ice Wand', 'power': 91, 'type': 'focus'}
    ]

    mages = [
        {'name': 'Zara', 'power': 50, 'element': 'ice'},
        {'name': 'Ash', 'power': 66, 'element': 'shadow'},
        {'name': 'Riley', 'power': 78, 'element': 'water'},
        {'name': 'Alex', 'power': 76, 'element': 'light'},
        {'name': 'Ember', 'power': 60, 'element': 'water'}
    ]

    spells = ['darkness', 'flash', 'heal', 'tornado']

    print("\nTesting artifact sorter...")
    sorted_a = artifact_sorter(artifacts)

    print(f"{sorted_a[0].get('name')} ({sorted_a[0].get('power')} power) \
comes before {sorted_a[1].get('name')} ({sorted_a[1].get('power')} power)")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    for spell in transformed:
        print(spell, end=' ')
    print()
