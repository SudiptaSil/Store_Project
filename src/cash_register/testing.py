from MyStore import Store
from MyStore import Payment
from MyStore import Change
from MyStore import Updater

store, payment, updater, change = Store(), Payment(), Updater(), Change()

payment.transaction("Milk", 3)
payment.pay()
updater.new_cash()
print(updater)
