from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Group, Itinerary, Wish, Guestbook, Rsvp
from .forms import UploadFileForm
import xlrd
from django.http import HttpResponseRedirect

# Create your views here.
def index(request): 

    context = {

    'title': 'MvitesApp: HomePage',
    }
    return render(request,'mvitesapp/index.html',context)

def excel(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            input_excel = request.FILES['input_excel']
            book = xlrd.open_workbook(file_contents=input_excel.read())
            xlsheet = book.sheet_by_index(0)

            customer = Customer()

            customer.bride  = xlsheet.cell_value(rowx=6,colx=1)
            customer.bridefullname  = xlsheet.cell_value(rowx=7,colx=1)
            customer.groom  = xlsheet.cell_value(rowx=8,colx=1)
            customer.groomfullname  = xlsheet.cell_value(rowx=9,colx=1)
            customer.addressline1  = xlsheet.cell_value(rowx=10,colx=1)
            customer.addressline2  = xlsheet.cell_value(rowx=11,colx=1)
            customer.addressline3  = xlsheet.cell_value(rowx=12,colx=1)
            customer.postalcode  = xlsheet.cell_value(rowx=13,colx=1)
            customer.host1  = xlsheet.cell_value(rowx=14,colx=1)
            customer.host2  = xlsheet.cell_value(rowx=15,colx=1)
            customer.host3  = xlsheet.cell_value(rowx=16,colx=1)
            customer.host4  = xlsheet.cell_value(rowx=17,colx=1)
            customer.bridecontactname  = xlsheet.cell_value(rowx=18,colx=1)
            customer.bridecontactname2  = xlsheet.cell_value(rowx=19,colx=1)
            customer.bridecontactno  = xlsheet.cell_value(rowx=20,colx=1)
            customer.bridecontactno2  = xlsheet.cell_value(rowx=21,colx=1)
            customer.groomcontactname  = xlsheet.cell_value(rowx=22,colx=1)
            customer.groomcontactname2  = xlsheet.cell_value(rowx=23,colx=1)
            customer.groomcontactno  = xlsheet.cell_value(rowx=24,colx=1)
            customer.groomcontactno2  = xlsheet.cell_value(rowx=25,colx=1)
            customer.eventdatetime  = xlsheet.cell_value(rowx=26,colx=1)
            customer.no_of_guests_attending  = xlsheet.cell_value(rowx=27,colx=1)
            customer.customeremail  = xlsheet.cell_value(rowx=28,colx=1)
            customer.bridecontact_number  = xlsheet.cell_value(rowx=29,colx=1)
            customer.groomcontact_number  = xlsheet.cell_value(rowx=30,colx=1)
            customer.eventstarttime  = xlsheet.cell_value(rowx=31,colx=1)
            customer.eventendtime  = xlsheet.cell_value(rowx=32,colx=1)


            customer.save()
            return HttpResponseRedirect('/admin/')
    else:
        form = UploadFileForm()
    return render(request, 'mvitesapp/excel.html', {'form': form})