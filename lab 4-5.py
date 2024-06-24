def triangle(base, height):
    area = 1/2*base*height
    #print("พื้นที่ 3 เหลี่ยม %.3f" % triangle(2,3))
    return area
#print("พื้นที่ 3 เหลี่ยม %.3f" % triangle(2,3))

base = int(input("ฐาน : "))
height = int(input("สูง : "))
print("พื้นที่ 3 เหลี่ยม %.3f" % triangle(base,height))
