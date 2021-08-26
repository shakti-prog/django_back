from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
import joblib

@csrf_exempt
def func2(request):
   if(request.method=="POST"):
      a = request.body
      s = a.decode('UTF-8')
      d = s[9:len(s)-2]
      cld = joblib.load('svd_final.sav')
      pred = []
      products = ['Mutual Funds', 'Home Loan', 'Asset Care', 'Home Insurance', 'Personal Loan', 'Credit Card',
                  'Demat Account', 'Health insurance', '2&3 Wheeler Loan', 'EMI NETWORK Card','Motor Insurance']
      for prod in products:
         anss = cld.predict(d, prod)
         dict = {'name': anss.iid, 'est': anss.est}
         pred.append(dict)
      result = sorted(pred, key=lambda k: k['est'], reverse=True)
      tosend = []
      for i in range(0, 6):
         tosend.append(result[i])
      print(tosend)
      return JsonResponse({"resp":tosend,"name":d})


@csrf_exempt
def func1(request):
    #return HttpResponse("You are on django field")
        if(request.method=="POST"):
           print(request.body)
           cls = joblib.load('df_final (1).sav')
           list1 = []
           list = []
           print(cls)
           products = ['Mutual Funds', 'Home Loan', 'Asset Care', 'Home Insurance', 'Personal Loan', 'Credit Card',
                  'Demat Account', 'Health insurance', '2&3 Wheeler Loan', 'EMI NETWORK Card','Motor Insurance']
           cust_name = 'A1'
           #scheme = 'Home Loan'
           for prod in products:
              ans = cls.predict(cust_name,prod)
              list.append(ans) 
           list = sorted(list,reverse=True)
           for i in range (len(list)-1,3,-1):
              list1.append(list[i])
           print(list1)
           return JsonResponse({'response':list1})







