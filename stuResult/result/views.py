from django.shortcuts import render

# Create your views here.
def showIndex(req):
    return render(req,"index.html")
def getStudentDetails(req):
    roll_no=req.POST.get("srno")
    stu_name=req.POST.get("sna")
    marks1=req.POST.get("mm")
    marks2=req.POST.get("pm")
    marks3=req.POST.get("cm")
    maths_marks=float(marks1)
    physics_marks=float(marks2)
    computer_marks=float(marks3)
    Total_marks = maths_marks + physics_marks + computer_marks
    Average_marks = Total_marks / 3
    if (computer_marks < 40 and physics_marks<40 and maths_marks<40):
        return render(req, "result.html",
                      {"sturoll":roll_no,"stuname":stu_name,"Total": Total_marks, "Average": Average_marks, "message": "your failed in maths,physics,computer"})
    elif (physics_marks < 40 and computer_marks < 40):
        return render(req, "result.html",
                      {"sturoll":roll_no,"stuname":stu_name,"Total": Total_marks, "Average": Average_marks, "message": "your failed in physics,computer"})

    elif (physics_marks < 40 and maths_marks < 40):
        return render(req, "result.html",
                      {"sturoll":roll_no,"stuname":stu_name,"Total": Total_marks, "Average": Average_marks, "message": "your failed in physics,maths"})

    elif (computer_marks < 40 and maths_marks<40):
        return render(req, "result.html",
                      {"sturoll":roll_no,"stuname":stu_name,"Total": Total_marks, "Average": Average_marks, "message": "your failed in maths,computers"})
    elif(maths_marks<40):
        return render(req,"result.html",{"sturoll":roll_no,"stuname":stu_name,"Total":Total_marks,"Average":Average_marks,"message":"your failed in maths"})
    elif(physics_marks<40):
        return render(req,"result.html",{"sturoll":roll_no,"stuname":stu_name,"Total":Total_marks,"Average":Average_marks,"message":"your failed in physics"})
    elif(computer_marks<40):
        return render(req, "result.html",{"sturoll":roll_no,"stuname":stu_name,"Total": Total_marks, "Average": Average_marks, "message": "your failed in computers"})
    else:
        return render(req, "result.html",{"sturoll":roll_no,"stuname":stu_name,"Total": Total_marks, "Average": Average_marks, "message": "your passed"})
