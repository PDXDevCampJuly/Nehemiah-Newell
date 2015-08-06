from Bank import Bank

pig = Bank()

pig.new_customer("John Wayne", "oldman@chair.net")

pig.new_customer("Mr. President", "thanks@obama.cookie")

pig.new_customer("Samus Aran", "bounty@hunter.com")

pig.new_customer("October Daye", "noob@mob.org")

pig.make_customer_account("oldman@chair.net", 500.00)

pig.make_customer_account("oldman@chair.net", -10.00, "Savings Account")

pig.make_customer_account("thanks@obama.cookie", 400000.00)

pig.make_customer_account("thanks@obama.cookie", 365.00, "Savings Account")

pig.make_customer_account("bounty@hunter.com", 3.00)

pig.make_customer_account("bounty@hunter.com", 4.00, "Savings Account")

pig.make_customer_account("noob@mob.org", 1000)

pig.make_customer_account("noob@mob.org", 1000, "Savings Account")

pig.show_all_customers()