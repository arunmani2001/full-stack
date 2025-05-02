from django.shortcuts import render,redirect
from .models import RTCRecord
from .utils import detect_year, scrape_missing_years

def Home(request):
    mydata=RTCRecord.objects.all()
    if (mydata!=''):
        return render(request,'list.html',{'datas':mydata})
    else:
        return render(request,'list.html')
    


def AddData(request):
    if request.method=="POST":
        survey_number = request.POST['survey_number']
        surnoc = request.POST['surnoc']
        hissa = request.POST['hissa']
        village = request.POST['village']
        hobli = request.POST['hobli']
        taluk = request.POST['taluk']
        district = request.POST['district']
        year = request.POST['year']
        owner_name = request.POST['owner_name']
        document = request.POST.get('document')
        extracted = request.POST['extracted']
        # period = request.POST['period']

        obj = RTCRecord(
            survey_number=survey_number or 0,
            surnoc=surnoc,
            hissa=hissa or 0,
            village=village,
            hobli=hobli,
            taluk=taluk,
            district=district,
            year=year,
            owner_name=owner_name,
            document=document,
            extracted=True,  # or False, depending on logic
            # period=period
        )
        obj.save()
        return redirect('Home')
    return render(request,'list.html')