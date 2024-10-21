def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))

 #Add code here to calculate BMI
 bmi = weight/(height**2)
 
 #Add code here to display calculate BMI
 print("BMI = "+str(round(bmi,2)))

 if bmi<18.5:
  print("Under Weight")
 elif 18.5 <= bmi <= 25.0:
  print("Normal Weight")
 else: 
  print("Over Weight")


calculate_bmi(weight=57, height=1.73) 
