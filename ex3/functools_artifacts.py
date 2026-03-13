import functools
import operator


def spell_reducer(spells: list[int], operations: str) -> int:
    if operations == 'add':
        return functools.reduce(operator.add, spells)
    if operations == 'multiply':
        return functools.reduce(operator.mul, spells)
    if operations == 'max':
        return functools.reduce(max, spells)
    if operations == 'min':
        return functools.reduce(min, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": functools.partial(base_enchantment, 50, "Fire"),
        "ice_enchant": functools.partial(base_enchantment, 50, "Ice"),
        "lightning_enchant": functools.partial(base_enchantment, 50,
                                               "Lightning")
    }


@functools.lru_cache
def memorized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memorized_fibonacci(n - 1) + memorized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def dispatch(spell: int) -> str:
        return f"deal {spell}"

    @dispatch.register
    def _(spell: str) -> str:
        return f"spell {spell} cast"

    @dispatch.register
    def _(spell: list) -> list:
        return f"multi-cast {spell}"

    return dispatch


if __name__ == "__main__":
    spell_powers = [20, 14, 20, 29, 41, 15]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [19, 13, 10]

    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, operations[0])}")
    print(f"Product: {spell_reducer(spell_powers, operations[1])}")
    print(f"Max: {spell_reducer(spell_powers, operations[2])}")

    print("\nTesting memorized fibonacci...")
    print(f"Fib(10): {memorized_fibonacci(10)}")
    print(f"Fib(15): {memorized_fibonacci(15)}")
