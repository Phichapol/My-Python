def qt(n):
    sum_price = 0
    for i in range(n):
        price = int(input("ราคาสินค้า %d:"% (i+1)))
        sum_price += price
    return sum_price

def tax(total):
    vat = (7/100)*total
    return vat

def change(money, net_price):
    c = money - net_price
    return c

num = int(input("จำนวนรายการสินค้า : "))
total = qt(num)
print(f"ราคารวม : {total}") #นำ qt มาใช้
print(f"ภาษีมูลค่าเพิ่ม %.2f"% (tax(total)))
net_price = total + tax(total)
print("รวมทั้งสิน %.2f" % net_price)
money = int(input("จำนวนเงิน : "))
print(f"เงินทอนทั้งหมด : %.2f"%change(money,net_price))
                  
