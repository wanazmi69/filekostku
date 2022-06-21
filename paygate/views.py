from multiprocessing import context
from django.shortcuts import render

# Create your views here.


def pay(request):
    pesan_dana = "Assalamuallaikum pak Sharip \nini bukti pembayaran kost MALINDO yang dikirim melalui DANA bulan ini. \nTerimakasih"
    pesan_bni = "Assalamuallaikum pak Sharip \nini bukti pembayaran kost MALINDO yang dikirim melalui BNI bulan ini. \nTerimakasih"
    pesan_linkAJA = "Assalamuallaikum pak Sharip \nini bukti pembayaran kost MALINDO yang dikirim melalui LINK-AJA bulan ini. \nTerimakasih"
    api_wa1 = f"https://api.whatsapp.com/send/?phone=6285394739760&text={pesan_dana}&app_absent=0"
    api_wa2 = f"https://api.whatsapp.com/send/?phone=6285394739760&text={pesan_bni}&app_absent=0"
    api_wa3 = f"https://api.whatsapp.com/send/?phone=6285394739760&text={pesan_linkAJA}&app_absent=0"
    
    
    bni = 'BNI PAY'
    nomor_bni = '0378942533'
    dana = 'DANA PAY'
    linkAja = 'LINK-AJA PAY'
    nomor_pay = '085394739760'
    context = {
        'bni': bni,
        'dana' : dana,
        'linkAja': linkAja,
        'nomor_pay': nomor_pay,
        'nomor_bni': nomor_bni,
        'pesan_dana':api_wa1,
        'pesan_bni':api_wa2,
        'pesan_linkAja':api_wa3,
    }
    return render(request, 'paygate/pay.html', context)
