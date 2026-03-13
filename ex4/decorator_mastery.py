import functools
import time


def spell_time(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Casting {args[0]}...")
        result = func(*args, **kwargs)
        print(f"Spell completed in {time.time() - start:.3f} seconds")
        print(f"Result: {result}")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, spell_name, power):
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self, spell_name, power)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> str:
            result = f"Spell casting failed after {max_attempts} attempts"
            for n in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                    break
                except Exception:
                    print(f"Spell failed, retrying... ({n}/{max_attempts})")
            return result
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        is_valid = True
        if len(name) < 3:
            is_valid = False
        for i in name:
            if not i.isalpha() and not i.isspace():
                is_valid = False
        return is_valid

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    mage = MageGuild()

    print("\nTesting spell timer...")
    spell_time(mage.cast_spell)("fireball", 15)

    print("\nTesting MageGuild...")
    print(mage.validate_mage_name("Joao"))
    print(mage.validate_mage_name("Joao@"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 5))
