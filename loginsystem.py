# 1. برنامج تسجيل الدخول (Login System)
# الخطوات:

#     تحديد الهدف:
#         برنامج يسمح للمستخدم بتسجيل الدخول عن طريق التحقق من اسم المستخدم وكلمة المرور.

#     إعداد البيانات:
#         إنشاء قائمة (أو قاموس) تحتوي على أسماء المستخدمين وكلمات المرور.

#     جمع المدخلات:
#         اطلب من المستخدم إدخال اسم المستخدم وكلمة المرور.

#     التحقق من المدخلات:
#         تحقق مما إذا كان اسم المستخدم موجودًا.
#         إذا كان موجودًا، تحقق مما إذا كانت كلمة المرور صحيحة.

#     رفع الأخطاء المناسبة:
#         إذا كان اسم المستخدم غير موجود، ارفع استثناء.
#         إذا كانت كلمة المرور خاطئة، ارفع استثناء.

#     معالجة الأخطاء:
#         التقط الأخطاء باستخدام try...except واطبع رسالة مناسبة.

#     عرض الرسالة النهائية:
#         إذا كانت المدخلات صحيحة، اطبع "تم تسجيل الدخول بنجاح".
# the goal is :
# program let the user to login using the validation of user name and password 
# collect the inputs 
# ________________________
user = {
    "user1": "password123",
    "user2": "mypassword",
    "admin":"admin123"
}
name = input("Enter your fullname :").strip()
password = input ("Enter your password :").strip()
# validate from the username and the userpassword 
try :
    #  تحقق مما اذا كان اسم المستخدم موجودا 
  if name not in user :
      raise ValueError ("Error user name is not exsited ")
#   تحقق من صحة الباسورد 
  if user[name] != password : 
      raise ValueError("error,password is incorrect")
except  ValueError as e : 
   print (e)
  