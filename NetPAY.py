# grossPay = int(input("Input gross salary In £:  "))
grossPay = 44800

taxRate = 0.2
NIRate = 0.135
SLRate = 0.09
pensionRate = 0.03

allowance = 12570
studentLoanThreshold = 27295

net = grossPay


# Benefit deductions
# Health cash benefits
net -= 300

# Pension contributions
temp = net
net *= (1-pensionRate)

# print("After pension contributions: £" + str(round(net,2))
print("Paid to pension: £" + str(round(temp-net,2)))
print("Paid to pension monthly: £" + str(round((temp-net)/12,2)))

# If company tops up pension contributions
# totPensionContribution = (temp-net) * 2 + temp*0.015
# print("Total to pension: £" + str(round(totPensionContribution,2)))

temp = net

# Remove student loans
if (net > studentLoanThreshold):
    net = (net - studentLoanThreshold)*(1-SLRate) + studentLoanThreshold

# print("After SL contributions: £" + str(net))
print("Lost to SLC: £" + str(round(temp - net ,2)))
print("Monthly SLC contributions: £" + str(round((temp - net)/12, 2)))



if (net > allowance):
    net -= allowance

    # Does the order matter for the final result?
    # It will change how much goes to each portion
    temp = net
    net *= (1-taxRate)
    print("Tax: £" + str(round(temp-net,2)))
    print("Monthly Tax: £" + str(round((temp-net)/12, 2)))

    temp = net
    net *= (1-NIRate)
    print("National Insurance: £" + str(round(temp-net,2)))
    print("Monthly NI: £" + str(round((temp-net)/12, 2)))

    net += allowance

print("Gross salary: £" + str(round(grossPay, 2)))
print("Gross monthly PAYE: £" + str(round(grossPay/12, 2)))

print("Net salary: £" + str(round(net, 2)))
print("Net monthly PAYE: £" + str(round(net/12, 2)))

print("Total Deducions: £" + str(round(grossPay-net, 2)))
print("Monthly Deducions: £" + str(round((grossPay-net)/12, 2)))
