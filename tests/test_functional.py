from src.manager import Manager
from src.models import Parameters


def test_tenants_total_due_matches_apartment_costs():
    manager = Manager(Parameters())

    settlement = manager.get_settlement('apart-polanka', 2025, 1)
    tenants_settlements = manager.create_tenants_settlements(settlement)

    total_tenants_due = sum(ts.total_due_pln for ts in tenants_settlements)

    assert total_tenants_due == settlement.total_due_pln


def test_get_tax():
    manager = Manager(Parameters())

    # 3 przelewy po 2500 PLN, 7500 * 0.085 = 637.5, zaokrąglenie w górę -> 638
    tax = manager.get_tax(2025, 1, 0.085)
    assert tax == 638

    # Brak przelewów w innym miesiącu -> podatek 0
    assert manager.get_tax(2025, 2, 0.085) == 0

