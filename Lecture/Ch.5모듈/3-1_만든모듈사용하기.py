import pay_module

print(pay_module.version)

print(pay_module.printAuthoor())

pay_info = pay_module.Pay("A1234", "2022-01-11", 20000)
print(pay_info.get_pay_info())

print(pay_module.__name__)