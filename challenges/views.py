from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponse
from django.template.loader import render_to_string

goals = {
    "january": "Read 5 books",
    "february": "Exercise 3 times a week",
    "march": "Learn a new skill",
    "april": "Save $500",
    "may": "Start a personal project",
    "june": "Travel to a new place",
    "july": "Volunteer for a cause",
    "august": "Improve coding skills",
    "september": "Eat healthier",
    "october": "Plan for the future",
    "november": "Practice gratitude daily",
    "december": "Spend quality time with family"
}

def month_index(request):
   month_keys_list = list(goals.keys())
   return HttpResponse(render(request, 'challenges/index.html', {
      "months": month_keys_list
   }))

def monthly_challanges(request, month):
    try:
       response = goals[month]
       next_month = ''
       month_keys_list = next_month = list(goals.keys())
       for index, (key, value) in enumerate(goals.items()):
           if key == month:
              next_month_index = index  + 1

              if next_month_index >= 12:
                 next_month = 'january'
              else:
                 next_month = month_keys_list[next_month_index]
       response_Data = render(request, "challenges/challenge.html", {
          'month': month,
          'response': response,
          'next_month' : next_month
       })
    except Exception as e:
         print(e) 
         raise Http404()
    return HttpResponse(response_Data)
