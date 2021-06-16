def taxCalculation(salary, taxRate):
	taxRate /= 100
	return (salary*taxRate)


def inHandSalary(salary):
	if salary<=250000:
		tax = taxCalculation(salary, 0)
		remaining = salary
		return tax, remaining, "Slab A: <=2,50,000"
		

	if salary>250000 and salary<=500000:
		tax = taxCalculation(salary, 5)
		remaining = salary-tax
		return tax, remaining, "Slab A: <=5,00,000"
		

	if salary>500000 and salary<=1000000:
		tax = 12500+taxCalculation(salary-500000, 20)
		remaining = salary-tax
		return tax, remaining, "Slab A: <=5,00,000"


if __name__ == '__main__':

	# salary = int(input("salary: ")) or float("250000")
	salary = 1000000
	
	tax, remaining, slab = inHandSalary(salary)
	print(f"Salary = {salary}\nTax Slab: {slab}\nTax Paid: {tax}\nIn Hand Salary: {remaining}")