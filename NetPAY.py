grossPay = int(input("Input gross salary In £:  "))
# grossPay = 26000

taxRate = 0.2
NIRate = 0.12
SLRate = 0.09
pensionRate = 0.05

allowance = 12570
studentLoanThreshold = 20000 #27295

# Print gross salary
print("Gross: £" + str(grossPay))

net = grossPay
# Remove student loans
if (grossPay > studentLoanThreshold):
    net = (grossPay - studentLoanThreshold)*(1-SLRate) + studentLoanThreshold

print("After SL contributions: £" + str(net))
print("Lost to SLC: £" + str(round(grossPay - net ,2)))
# Pension contributions

temp = net
net *= (1-pensionRate)

print("After pension contributions: £" + str(net))
print("Paid to pension: £" + str(round(temp-net,2)))
totPensionContribution = (temp-net) * 2 + temp*0.015
print("Total to pension: £" + str(round(totPensionContribution,2)))

if (net > allowance):
    net -= allowance

    # Does the order matter for the final result?
    # It will change how much goes to each portion
    temp = net
    net *= (1-taxRate)*(1-NIRate)
    print("Lost to big brother: £" + str(round(temp-net,2)))

    net += allowance

print("Net salary: £" + str(round(net, 2)))
print("Net monthly PAYE: £" + str(round(net/12, 2)))
