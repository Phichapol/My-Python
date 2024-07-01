def score(w,mt,ft):
    
    n = w + mt +ft
    
    return n

def compare(n):
    if n < 50:
        print("ไม่ผ่าน")
    elif n >= 50 and n <= 79:
        print("ผ่าน")
    elif n >= 80 and n <= 100:
        print("ดีมาก")
        
    return n
    
w = int(input("คะแนนเก็บ : "))

mt = int(input("คะแนนกลางภาค : "))

ft = int(input("คะแนนปลายภาค : "))

tt = float(score(w,mt,ft))
if w <= 20:
    if mt <= 40:
        if ft <= 40:
            print("คะแนนทั้งหมด %.2f"%tt )
            compare(score(w,mt,ft))
        else:
            print("ใส่เกิน")
    else:
        print("ใส่เกิน")          
else:
    print("ใส่เกิน")




