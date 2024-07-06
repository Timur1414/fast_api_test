import re


def validate_full_name(value: str) -> bool:
    return bool(re.fullmatch(r'^([А-ЯЁа-яё-]+ ){1, 3} ?[А-ЯЁа-яё-]+$', value.strip()))


def validate_group(value: str) -> bool:
    return bool(re.fullmatch(r'(^[А-ЯЁа-яё]+)\d{1, 2}-\d{2}[А-ЯЁа-яё]{,2}', value.strip()))
