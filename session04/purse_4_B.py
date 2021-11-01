import math
from typing import Protocol

class Account(Protocol):
    def pay_in(self, other): ...
    def please_pay(self, amount: int): ...
    def please_pay_exactly(self, amount: int): ...

class Purse(Account):

    def __init__(self, initial_cashmap = {}):
        """Creates a purse optionally using the int->int pairs of a dict as
        representing an initial map from denomination (face value) to quantity.
        """
        self._cashmap = { fv:n for (fv, n) in initial_cashmap.items() if isinstance(fv, int) and isinstance(n, int) }

    def _ensure(self, face_values):
        for fv in face_values:
            if fv not in self._cashmap:
                self._cashmap[fv] = 0

    def _addm(self, cashmap, multiplier):
        """Add in a multiple of the cashmap"""
        self._ensure(cashmap.keys())
        for (fv, n) in cashmap.items():
            self._cashmap[fv] += multiplier * n

    def total(self):
        """Returns the total value of a purse"""
        return sum(fv * n for (fv, n ) in self._cashmap.items())

    def _can_pay(self, amount):
        return self.total() >= amount

    def pay_in(self, other_purse: Account):
        """Drains the coins from the other_purse into this one"""
        cash = other_purse._cashmap                 # Q: Is this OK? If not, why not?
        other_purse = {}
        self._addm(cash, 1)

    def _cash_list(self):
        """Return the cashmap as a list of tuples sorted by face-value"""
        return [(k, self._cashmap[k]) for k in sorted(self._cashmap.keys(), reverse=True)]

    def please_pay(self, amount):
        """
        This should return an offer purse. The total must be >= the amount
        and it must also be <= the total value of this purse. The coins in 
        the offer purse must be a subbag of the coins in this purse. This
        purse must be debited by the coins of the offer purse.

        If we cannot make a good offer, return None.
        """
        if not self._can_pay(amount):
            return None
        cashmap = self._generate_offer_cashmap(amount, math.inf)
        return self._split_purse(cashmap)

    def please_pay_exactly(self, amount):
        """
        This should return a change purse. The total must <= the total value 
        of this purse and the coins in the change purse must be a subbag of 
        those in this purse. This purse must be debited by the coins of the
        change purse.
        """
        if not self._can_pay(amount):
            return None
        cashmap = self._generate_offer_cashmap(amount, 0)
        return self._split_purse(cashmap)

    def _split_purse(self, cashmap):
        if cashmap is not None:
            offer_purse = Purse()
            offer_purse._addm(cashmap, 1)
            self._addm(cashmap, -1)
            return offer_purse

    def _generate_offer_cashmap(self, amount, best_offer_excess):
        """Returns the best offer cashmap"""
        cash_list = self._cash_list()
        available_total = self.total()
        best_offer_cashmap = None
        for (excess, cashmap) in Purse._find_offers(cash_list, available_total, amount, {}):
            # print("solution", excess, cashmap)    # Comment back in to show the trace of solutions.
            improvement = False
            if excess < best_offer_excess:
                improvement = True
            elif excess == best_offer_excess:
                if not best_offer_cashmap: 
                    improvement = True
                elif sum(cashmap.values()) < sum(best_offer_cashmap.values()):
                    improvement = True
            if improvement:
                best_offer_excess = excess
                best_offer_cashmap = cashmap                
        return best_offer_cashmap   

    @staticmethod
    def _find_offers(available_cashlist, available_total, amount_remaining, sofar_cashmap):
        """Generator that finds solutions of the form (offer_excess, offer_cashmap)"""
        if amount_remaining <= 0:
            yield (-amount_remaining, sofar_cashmap)
        elif available_total == amount_remaining:
            yield (0, {**{ fv:n for (fv, n) in available_cashlist}, **sofar_cashmap})
        elif available_total > amount_remaining and available_cashlist:
            (fv, n) = available_cashlist[0]
            # No point in offering more than k where fv * k >= amount_remaining
            k = ( amount_remaining + fv - 1 ) // fv
            for i in range(min(k, n), -1, -1):   # Count down from n+1 to 0
                value_total = fv * n
                value_to_add = fv * i
                yield from Purse._find_offers(available_cashlist[1:], available_total - value_total, amount_remaining - value_to_add, {fv:i, **sofar_cashmap})

def transaction(target_amount, vendor_purse, customer_purse):
    success = False
    offer_purse = None
    change_purse = None
    try:
        offer_purse = customer_purse.please_pay(target_amount) or Purse()
        offer_purse_total = offer_purse.total()
        if offer_purse_total < target_amount:
            return False
        change_purse = vendor_purse.please_pay_exactly(offer_purse_total - target_amount) or Purse()
        if offer_purse_total != target_amount + change_purse.total():
            return False
        vendor_purse.pay_in(offer_purse)
        offer_purse = None
        customer_purse.pay_in(change_purse)
        change_purse = None
        return True
    finally:
        if offer_purse: customer_purse.pay_in(offer_purse)      # reimburse
        if change_purse: vendor_purse.pay_in(change_purse)      # reimburse            

if __name__ == "__main__":
    customer = Purse(initial_cashmap={100:8, 50:2, 20:1, 10:1, 5:3, 2:1, 1:1})
    c_before = customer.total()
    vendor = Purse(initial_cashmap={100:100, 50:100, 20:100, 10:100, 5:100, 2:100, 1:100})
    v_before = vendor.total()
    assert transaction(499, vendor, customer)
    assert c_before == customer.total() + 499 
    assert v_before + 499 == vendor.total()
    print( 'Transaction successful' )