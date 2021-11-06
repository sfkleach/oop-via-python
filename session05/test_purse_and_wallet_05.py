from purse_and_wallet_05 import *

def test_Purse():
    customer = Purse(initial_cashmap={100:8, 50:2, 20:1, 10:1, 5:3, 2:1, 1:1})
    c_before = customer.total()
    vendor = Purse(initial_cashmap={100:100, 50:100, 20:100, 10:100, 5:100, 2:100, 1:100})
    v_before = vendor.total()
    assert transaction(499, vendor, customer)
    assert c_before == customer.total() + 499 
    assert v_before + 499 == vendor.total()

def test_Wallet():
    customer = Wallet(initial_cashmap={100:8, 50:2, 20:1, 10:1, 5:3, 2:1, 1:1})
    c_before = customer.total()
    vendor = Wallet(initial_cashmap={100:100, 50:100, 20:100, 10:100, 5:100, 2:100, 1:100})
    v_before = vendor.total()
    assert transaction(499, vendor, customer)
    assert c_before == customer.total() + 499 
    assert v_before + 499 == vendor.total()

def test_crossover_purse_to_wallet():
    customer = Purse(initial_cashmap={100:8, 50:2, 20:1, 10:1, 5:3, 2:1, 1:1})
    c_before = customer.total()
    vendor = Wallet(initial_cashmap={100:100, 50:100, 20:100, 10:100, 5:100, 2:100, 1:100})
    v_before = vendor.total()
    assert transaction(499, vendor, customer)
    assert c_before == customer.total() + 499 
    assert v_before + 499 == vendor.total()

def test_crossover_wallet_to_purse():
    customer = Wallet(initial_cashmap={100:8, 50:2, 20:1, 10:1, 5:3, 2:1, 1:1})
    c_before = customer.total()
    vendor = Purse(initial_cashmap={100:100, 50:100, 20:100, 10:100, 5:100, 2:100, 1:100})
    v_before = vendor.total()
    assert transaction(499, vendor, customer)
    assert c_before == customer.total() + 499 
    assert v_before + 499 == vendor.total()

def test_self_transaction():
    customer = Purse(initial_cashmap={100:8, 50:2, 20:1, 10:1, 5:3, 2:1, 1:1})
    c_before = customer.total()
    assert transaction(499, customer, customer)
    assert c_before == customer.total()