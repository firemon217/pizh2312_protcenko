from bonusDeposit import *
from capitalizationDeposit import *
from urgentDeposit import *

urg: BonusDeposit = BonusDeposit(50000.0, 12, 10000.0)
urg.topUpDeposit(50000)
urg.interestAccrualOnDeposit()
print(urg)