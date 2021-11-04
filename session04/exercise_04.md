# Exercise for Session 04 - Reimplement Account

In the file `purse_04_B.py` you will see an implementation of the class
`Purse`, which is an implementation of the protocol `Account`. The aim
of this exercise is to add a second implementation of `Account`, which
might be called `Wallet`. You will note that I have marked the non-public
methods with a leading underscore.

You are free to choose the basis of the `Wallet`s implementation. However,
when it is done, you should check that it works correctly with regard to the 
function `transaction`. And once you are satisified it is working, you should
try the same but with a mixed implementation of `Purse` and `Wallet`.

In doing this, you will probably want to move surface methods such as
`_generate_offer_cashmap` to the `Account` protocol, so that it can be
shared by both `Purse` and `Wallet`.

If you have left the `_pay_in` method undisturbed, and I encourage you to
do that so you can see the issue, then you will find that the mixed 
transaction will fail. (In fact you may even find the `Wallet` transaction
fails as well.) 

In the workshop I argued that the implementation of `_pay_in` is flawed 
because it is open to the implementation. Try eliminating the problem and
see if you can explain why this is your prefered answer.
