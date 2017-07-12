
def totalWholeSaleFor(copies):
  originalBookPrice = 24.95
  percentualDiscount = 40
  saleBookPrice = (originalBookPrice * percentualDiscount) / 100
  
  shipping = 3
  finalBookPrice = saleBookPrice + shipping
  if(copies == 1):
    return finalBookPrice

  additionalCopyValue = (copies - 1) * 0.75
  finalBookPrice += additionalCopyValue
  return finalBookPrice

print(totalWholeSaleFor(60))

