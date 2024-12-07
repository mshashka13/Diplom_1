import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Тесты на класс Burger
class TestBurger:
    # Проверка добавления булки в объект бургера
    def test_burger_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Проверка добавления ингредиента в объект бургера
    def test_burger_add_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert mock_sauce in burger.ingredients

    # Проверка удаления ингредиента из списка ингредиентов бургера
    def test_burger_remove_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1 and mock_filling in burger.ingredients

    # Проверка корректного изменения порядка ингредиентов в списке ингредиентов бургера
    @pytest.mark.parametrize(
        "ingredients, indices, expected_order", [
            (
            [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING], (1, 0), [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE]),
            ([INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE], (0, 1), [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]), ], )
    def test_burger_move_ingredient(self, mock_sauce, mock_filling, ingredients, indices, expected_order):
        burger = Burger()
        ingredient_map = {INGREDIENT_TYPE_SAUCE: mock_sauce, INGREDIENT_TYPE_FILLING: mock_filling, }
        for ingredient_type in ingredients:
            burger.add_ingredient(ingredient_map[ingredient_type])
        burger.move_ingredient(*indices)
        actual_order = [mock.get_type() for mock in burger.ingredients]
        assert actual_order == expected_order

    # Проверка правильного расчета общей стоимости бургера
    def test_burger_get_price(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_price = (200 * 2) + 100 + 150
        assert burger.get_price() == expected_price

    # Проверка корректного отображения названия булки в чеке
    def test_burger_receipt_contains_bun(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        receipt = burger.get_receipt()
        assert "(==== булка ====)" in receipt

    # Проверка корректного отображения названия соуса в чеке
    def test_burger_receipt_contains_sauce(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        receipt = burger.get_receipt()
        assert "= sauce горячий соус =" in receipt

    # Проверка корректного отображения названия начинки в чеке
    def test_burger_receipt_contains_filling(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        receipt = burger.get_receipt()
        assert "= filling котлета =" in receipt

    # Проверка корректного отображения общей суммы в чеке
    def test_burger_receipt_contains_price(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        receipt = burger.get_receipt()
        assert "Price: 650" in receipt
