print("Enter the  math marks:")
math=int(input(""))
print("Enter the  english marks:")
english=int(input(""))
print("Enter the  scinece marks:")
science=int(input(""))
print("Enter the  hindi marks:")
hindi=int(input(""))
print("Enter the  sanskrit marks:")
sanskrit=int(input(""))
sum=math+english+science+hindi+sanskrit
percentage=(sum/500*100)
if(percentage<40):
    print("failed")
if(percentage>=40 and percentage<55):
    print("good")
if(percentage>=55 and percentage<65):
    print(" very good")
if(percentage>=65 and percentage<90):
    print("Excellent")
    
