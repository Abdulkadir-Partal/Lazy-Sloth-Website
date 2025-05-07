from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import now
from .models import TimeTracking
from datetime import timedelta
from django.db.models import Sum
from .models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def save_time_data(request):
    if request.method == "POST":
        # Get the work time and break time from the form (you need to pass these from JavaScript)
        work_time = request.POST.get("work_time")  # Time spent working (in seconds)
        break_time = request.POST.get("break_time")  # Time spent breaking (in seconds)

        # Convert work_time and break_time from seconds to timedelta
        work_time_duration = timedelta(seconds=int(work_time))
        break_time_duration = timedelta(seconds=int(break_time))

        # Check if there's already an entry for today
        today_entry, created = TimeTracking.objects.get_or_create(date=now().date())

        # Add the new work and break time to the current entry
        today_entry.work_time += work_time_duration
        today_entry.break_time += break_time_duration
        today_entry.save()

        return render(request, "concentrate_now.html", {"success": True})

    return render(request, "concentrate_now.html")

def report_view(request):
    # Get today's date
    today = now().date()

    # Calculate time spent today
    today_time = TimeTracking.objects.filter(date=today).aggregate(
        work_sum=Sum('work_time'), break_sum=Sum('break_time')
    )

    # Calculate time spent this week
    start_of_week = today - timedelta(days=today.weekday())  # Monday of the current week
    week_time = TimeTracking.objects.filter(date__gte=start_of_week).aggregate(
        work_sum=Sum('work_time'), break_sum=Sum('break_time')
    )

    # Calculate time spent this month
    start_of_month = today.replace(day=1)  # First day of the current month
    month_time = TimeTracking.objects.filter(date__gte=start_of_month).aggregate(
        work_sum=Sum('work_time'), break_sum=Sum('break_time')
    )

    return render(request, "report.html", {
        "today_time": today_time,
        "week_time": week_time,
        "month_time": month_time,
    })

def home(request):
    return render(request, 'home.html')

def concentrate_now(request):
    return render(request, 'concentrate_now.html')

def my_goals(request):
    return render(request, 'my_goals.html')

def report(request):
    return render(request, 'report.html')






