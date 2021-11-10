money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

money = int(input("교환할 돈은 얼마?"))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print(f"\n 500짜리는 {c500}이고 100원 짜리는 {c100}이며 50 짜리는 {c50} 10 짜리는 {c10}")
print("\n 500원짜리 => %d개" % c500)
print("\n 100원짜리 => {}개".format(c100))
print(f"\n 50원짜리 => {c50}개")
print("\n 10원짜리 => %d개" % c10)
print("\n 바꾸지 못한 잔돈 => %d개" % money)