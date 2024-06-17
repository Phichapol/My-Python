print("โปรแกรมคำนวณดัชนีมวลกาย")
w = input("น้ำหนักตัว กิโลกรัม : ")
t = input("ส่วนสูง เซนติเมตร : ")

w = float(w)
t = float(t)/100
bmi = w / (t * t)
print("%.2f" %bmi)

if bmi < 18.50:
    print("น้ำหนักน้อย/ผอม")
elif bmi >= 18.50 and bmi <= 22.90:
    print("ปกติ/สุขภาพดี")
elif bmi >= 23.00 and bmi <= 24.90:
    print("ท้วม/โรคอ้วนระดับ1")
elif bmi >= 25.00 and bmi <= 29.90:
    print("อ้วน/โรคอ้วนระดับ2")
elif bmi >= 30:
    print("อ้วนมาก/โรคอ้วนระดับ3")

    