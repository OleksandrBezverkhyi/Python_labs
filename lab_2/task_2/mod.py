def required_money(stipend, expenses):
  total_expenses = 0
  for month in range(10):
    total_expenses += expenses
    expenses *= 1.05 
  return total_expenses - (stipend * 10)
