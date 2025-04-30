from django.shortcuts import render, redirect
from .forms import RTCUploadForm
from .models import RTCRecord
from .llm_integration import extract_info_from_rtc
from .scraper import fetch_missing_rtc
import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def upload_rtc(request):
    if request.method == 'POST':
        form = RTCUploadForm(request.POST, request.FILES)
        if form.is_valid():
            rtc = form.save()
            file = rtc.document.open(mode='rb')
            text = extract_text_from_pdf(file)
            file.close()
            year, owner = extract_info_from_rtc(text)
            rtc.year = year
            rtc.owner_name = owner
            rtc.extracted = True
            rtc.save()
            return redirect('list_rtc')
    else:
        form = RTCUploadForm()
    return render(request, 'rtc/upload.html', {'form': form})

def list_rtc(request):
    rtcs = RTCRecord.objects.all()
    return render(request, 'rtc/list.html', {'rtcs': rtcs})

def fetch_missing_years(request):
    fixed_details = {
        'survey_number': '22',
        'surnoc': '*',
        'hissa': '1',
        'village': 'Devanahalli',
        'hobli': 'Kasaba',
        'taluk': 'Devenahalli',
        'district': 'Bangalore Rural'
    }
    present_years = RTCRecord.objects.values_list('year', flat=True)
    all_years = [
        '2012-13', '2013-14', '2014-15', '2015-16', 
        '2016-17', '2017-18', '2018-19', '2019-20', '2020-21'
    ]
    missing = [y for y in all_years if y not in present_years]

    for year in missing:
        rtc_text = fetch_missing_rtc(year=year, **fixed_details)
        if rtc_text:
            year, owner = extract_info_from_rtc(rtc_text)
            RTCRecord.objects.create(
                year=year,
                owner_name=owner,
                extracted=True,
                document=None,
                **fixed_details
            )
    return redirect('list_rtc')
