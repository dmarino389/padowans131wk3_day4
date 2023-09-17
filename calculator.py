class RentalProperty:
    def __init__(self, purchase_price, annual_rental_income, annual_expenses, holding_period_years):
        self.purchase_price = purchase_price
        self.annual_rental_income = annual_rental_income
        self.annual_expenses = annual_expenses
        self.holding_period_years = holding_period_years

    def calculate_roi(self):
        total_investment = self.purchase_price + sum(self.annual_expenses) * self.holding_period_years
        total_return = self.annual_rental_income * self.holding_period_years
        roi = ((total_return - total_investment) / total_investment) * 100
        return roi

def main():
    purchase_price = float(input("Enter the purchase price of the property: "))
    annual_rental_income = float(input("Enter the annual rental income: "))
    annual_expenses = []
    for expense_name in ["property tax", "insurance", "maintenance"]:
        expense = float(input(f"Enter the annual {expense_name} expense: "))
        annual_expenses.append(expense)
    holding_period_years = int(input("Enter the holding period in years: "))

    property = RentalProperty(purchase_price, annual_rental_income, annual_expenses, holding_period_years)
    roi = property.calculate_roi()

    print(f"Return on Investment (ROI) for the rental property is: {roi:.2f}%")

if __name__ == "__main__":
    main()
