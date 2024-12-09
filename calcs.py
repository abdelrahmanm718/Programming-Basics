# الهدف : إنشاء دوال تقوم بعمليات حسابية مختلفة (جمع، طرح، ضرب، قسمة) واستدعاؤها من البرنامج.
# الخطوات:

    # أنشئ دالة لكل عملية (مثل add للجمع، subtract للطرح...).
def add (a,b):
    return a + b 
def subtract (a,b):
    return a - b 
def multiply (a,b):
    return a * b 
def divide (a,b): 
    if b ==0 :
        return "cannot divide by zero "
    return a / b
# اختبر دالة الجمع
print(add(3, 5))  # الناتج: 8

# اختبر دالة الطرح
print(subtract(10, 4))  # الناتج: 6

# اختبر دالة القسمة
print(divide(9, 3))  # الناتج: 3.0
print(divide(5, 0))  # الناتج: Cannot divide by zero
 
def calculator ():
    process = input ("Enter your process (add) or (multiply) or (divide) : ")
    if process == "add":
        a = float(input("Enter your first number: "))
        b = float(input("Enter your second number: "))

# print (add(a,b))
    # اجعل المستخدم يختار العملية التي يريدها.
    # اطلب من المستخدم إدخال رقمين.
    # استدعِ الدالة المناسبة بناءً على العملية المختارة.