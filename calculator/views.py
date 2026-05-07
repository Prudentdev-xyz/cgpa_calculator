from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Result, Course
from .utils import calculate_gp, GRADE_POINTS

@login_required(login_url='/auth/login/')
def calculate_view(request):
    if request.method == 'POST':
        names = request.POST.getlist('course_name')
        units = request.POST.getlist('course_units')
        grades = request.POST.getlist('course_grade')

        courses = []
        for i in range(len(names)):
            if names[i] and units[i] and grades[i]:
                courses.append({
                    'name': names[i],
                    'units': units[i],
                    'grade': grades[i],
                })

        if not courses:
            messages.error(request, 'Please add at least one course')
            return redirect('calculate')

        gp, total_units = calculate_gp(courses)

        result = Result.objects.create(
            user=request.user,
            gp=gp,
            total_units=total_units
        )

        for c in courses:
            Course.objects.create(
                result=result,
                name=c['name'],
                units=int(c['units']),
                grade=c['grade'].upper(),
                grade_point=GRADE_POINTS.get(c['grade'].upper(), 0)
            )

        return redirect('result', id=result.id)

    num_range = range(3)
    return render(request, 'calculator/calculate.html', {'num_range': num_range})


@login_required(login_url='/auth/login/')
def result_view(request, id):
    result = get_object_or_404(Result, id=id, user=request.user)
    courses = result.courses.all()
    return render(request, 'calculator/result.html', {
        'result': result,
        'courses': courses,
    })


@login_required(login_url='/auth/login/')
def download_pdf(request, id):
    pass  # coming soon