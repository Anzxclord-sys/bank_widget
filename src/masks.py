def get_mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер банковской карты."""
    # Берем цифры блоками и собираем в нужный формат
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер банковского счета."""
    # Берем только последние 4 цифры и подставляем звездочки
    return f"**{account_number[-4:]}"