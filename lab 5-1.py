def calavgscore(n):
    
    sum_score = 0
    
    for i in range(n):
        score = int(input(f"กรอกคะแนนนักศึกษาคนที่ {i+1}: "))
        sum_score += score
        
    avgscore = sum_score/n
    return avgscore
    
n = int(input("กรอกจำนวนนักศึกษา : "))
average = calavgscore(n)
print(f"คะแนนเฉลี่ยของนักศึกษา {n} คน คือ {average}")