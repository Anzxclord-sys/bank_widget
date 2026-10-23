from typing import Any


def filter_by_state(data_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрует список словарей по значению ключа state."""
    filtered_list = []
    for item in data_list:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(data_list: list[dict[str, Any]], is_reverse: bool = True) -> list[dict[str, Any]]:
    """Функция сортирует список словарей по дате (по умолчанию — по убыванию)."""
    sorted_list = sorted(data_list, key=lambda x: x["date"], reverse=is_reverse)
    return sorted_list
