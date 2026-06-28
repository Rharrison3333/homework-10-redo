def calculate_payment(principal, rate, compounds, years):
    monthly_rate = rate / compounds
    total_payments = compounds * years

    payment = principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)

    return payment


def main():
    principal = float(input("Enter the loan amount: "))
    rate = float(input("Enter the annual interest rate as a decimal: "))
    compounds = int(input("Enter the number of payments per year: "))
    years = int(input("Enter the number of years: "))
    filename = input("Enter the output file name: ")

    payment = calculate_payment(principal, rate, compounds, years)
    balance = principal

    output_file = open(filename, "w")

    output_file.write("Payment\tPayment Amount\tInterest\tPrincipal\tBalance\n")

    for payment_number in range(1, compounds * years + 1):
        interest = balance * (rate / compounds)
        principal_paid = payment - interest
        balance = balance - principal_paid

        if balance < 0:
            balance = 0

        output_file.write(str(payment_number) + "\t")
        output_file.write("$" + format(payment, ".2f") + "\t")
        output_file.write("$" + format(interest, ".2f") + "\t")
        output_file.write("$" + format(principal_paid, ".2f") + "\t")
        output_file.write("$" + format(balance, ".2f") + "\n")

    output_file.close()

    print("Amortization report saved to", filename)


main()
