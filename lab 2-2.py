s = int(input("คะแนน : "))

if s > 0 and s < 100:

        if s >= 80 and s <= 100:
            print("เกรดA")
        elif s >= 70 and s <= 79:
            print("เกรดB")
        elif s >= 60 and s <= 69:
            print("เกรดC")
        elif s >= 50 and s <= 59:
            print("เกรดD")
        elif s >= 0 and s <=49:
            print("เกรดF")

else:
    print("กรุณากอกข้อมูล 0-100")