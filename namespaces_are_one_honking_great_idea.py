#Bad
from instruments.guitars import fender, ibanez

fender(page)
ibanez(vai)

#Better
from instruments import guitars

guitars.fender(page)
guitars.ibanez(vai)
