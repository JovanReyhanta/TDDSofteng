import pytest
from src.fare import compute_food_delivery

def test_amount_above_50_4():
     assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=True,
        isMembership=False,
        delivery_distance=21,
    ) == -1

def test_amount_above_50_5():
     assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=False,
        isMembership=True,
        delivery_distance=10,
    ) == 51

def test_amount_above_50_6():
     assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=False,
        isMembership=False,
        delivery_distance=10,
    ) == 51

def test_amount_above_50_7():
     assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=False,
        isMembership=True,
        delivery_distance=21,
    ) == -1

def test_amount_above_50_8():
      assert compute_food_delivery(
        amount_orders=51,
        isPeakHours=False,
        isMembership=False,
        delivery_distance=21,
    ) == -1