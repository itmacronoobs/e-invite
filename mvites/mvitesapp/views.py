from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Group, Itinerary, Wish, Guestbook, Rsvp
from .forms import UploadFileForm
import xlrd
from django.http import HttpResponseRedirect
from django.db.models import Avg, Count, Min, Sum, F

# Create your views here.
def index(request): 
    customer = Customer.objects.all().order_by('-id')
    context = {
    'customer': customer,
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

            if not request.POST["update"]:
            
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
    
                for x in range(35,48):
                    if xlsheet.cell_value(rowx = x,colx=1) != "":
                        itinerary = Itinerary()
                        itinerary.starttime = xlsheet.cell_value(rowx=x,colx=1)
                        itinerary.endtime = xlsheet.cell_value(rowx=x,colx=2)
                        itinerary.title = xlsheet.cell_value(rowx=x,colx=3)
                        itinerary.body = xlsheet.cell_value(rowx=x,colx=4)
                        itinerary.save()
                
                
                rsvp = Rsvp()
                rsvp.status = "YES"
                rsvp.save()

                rsvp = Rsvp()
                rsvp.status = "NO"
                rsvp.save()

                rsvp = Rsvp()
                rsvp.status = "MAYBE"
                rsvp.save()

                rsvp = Rsvp()
                rsvp.status = "UNCONFIRMED"
                rsvp.save()
                
                x = 49
                while x >= 49:
                    if xlsheet.cell_value(rowx=x,colx=7) != 0.0:
                        group = Group()
                        group.name =  xlsheet.cell_value(rowx=x,colx=7)
                        group.save()
                        x = x + 1

                    else:
                        x = 48

            
            x = 49
            while x >= 49:
                if xlsheet.cell_value(rowx=x,colx=0) != "":
                    
                    guestbook = Guestbook()
                    guestbook.name = xlsheet.cell_value(rowx=x,colx=0)
                    guestbook.no_of_guests_invited = xlsheet.cell_value(rowx=x,colx=1)
                    guestbook.no_of_guests_attending = xlsheet.cell_value(rowx=x,colx=2)
                    guestbook.email = xlsheet.cell_value(rowx=x,colx=3)
                    guestbook.contact_number = xlsheet.cell_value(rowx=x,colx=4)
                    guestbook.rsvp = Rsvp.objects.get(status=xlsheet.cell_value(rowx=x,colx=5))
                    guestbook.group = Group.objects.get(name=xlsheet.cell_value(rowx=x,colx=6))
                    guestbook.save()
                    x = x + 1
                else:
                    x = 48



            return HttpResponseRedirect('/admin/')
    else:
        form = UploadFileForm()
    return render(request, 'mvitesapp/excel.html', {'form': form})

def guestbook(request): 
    group = Group.objects.all().annotate(total = Sum('guestbook__no_of_guests_attending'),total_invite = Sum('guestbook__no_of_guests_invited'))
    customer = Customer.objects.all().order_by('-id')
    guestbook = Guestbook.objects.all().order_by('-id').annotate(differences = F('no_of_guests_invited')- F ('no_of_guests_attending'))
    guest_count = Guestbook.objects.all().count()
    guest_attending1 = list(Guestbook.objects.aggregate(total = Sum('no_of_guests_attending')).values())[0]
    guest_invited1 = list(Guestbook.objects.aggregate(total = Sum('no_of_guests_invited')).values())[0]
    guest_attending = Guestbook.objects.aggregate(total = Sum('no_of_guests_attending'))
    guest_invited = Guestbook.objects.aggregate(total = Sum('no_of_guests_invited'))
    rsvp_yes = Guestbook.objects.filter(rsvp__status='YES').count()
    rsvp_no = Guestbook.objects.filter(rsvp__status='NO').count()
    rsvp_maybe = Guestbook.objects.filter(rsvp__status='MAYBE').count()
    rsvp_unconfirmed = Guestbook.objects.filter(rsvp__status='UNCONFIRMED').count()

    total_responded = guest_count - rsvp_unconfirmed
    rsvp_maybeplusunconfirmed = rsvp_maybe + rsvp_unconfirmed

    differences_list = guestbook.order_by('differences').values('differences').distinct()
    
    bar_totalinvites = str(round(total_responded/guest_count,3)*100) + "%"
    bar_totalresponded = str(round(total_responded/guest_count,3)*100) + "%"
    bar_yes = str(round(rsvp_yes/guest_count,3)*100) + "%"
    bar_no = str(round(rsvp_no/guest_count,3)*100) + "%"
    bar_maybe = str(round(rsvp_maybe/guest_count,3)*100) + "%"
    bar_unconfirmed = str(round(rsvp_unconfirmed/guest_count,3)*100+round(rsvp_maybe/guest_count,3)*100) + "%"
    
    bar_attending = str(round(guest_attending1/guest_invited1,3)*100) + "%"

    context = {
        'total_responded': total_responded ,
        'title': 'MvitesApp: Guestbook',
		'guestbook': guestbook,
        'customer': customer,
        'guest_count':  guest_count,
        'rsvp_yes': rsvp_yes,
        'rsvp_no': rsvp_no,
        'rsvp_maybe': rsvp_maybe,
        'rsvp_unconfirmed': rsvp_unconfirmed,
        'guest_attending' : guest_attending,
        'guest_invited' : guest_invited,
        'group' : group,
        'rsvp_maybeplusunconfirmed' : rsvp_maybeplusunconfirmed,
        'bar_totalinvites' : bar_totalinvites,
        'bar_totalresponded' : bar_totalresponded,
        'bar_yes' : bar_yes,
        'bar_no' : bar_no,
        'bar_maybe' : bar_maybe,
        'bar_unconfirmed' : bar_unconfirmed,
        'bar_attending' : bar_attending,
        'differences_list' : differences_list,
	}
	
    return render(request,'mvitesapp/guestbook.html',context)