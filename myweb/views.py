from django.shortcuts import render


def index(request):
    pesan_sarif = "Assalamuallaikum pak Sharip, saya ingin menanyakan informasi seputar kost MALINDO"
    api_sarif = f"https://api.whatsapp.com/send/?phone=6285394739760&text={pesan_sarif}&app_absent=0"
    pesan_safar = "Assalamuallaikum pak Shappar, saya ingin menanyakan informasi seputar kost MALINDO"
    api_safar = f"https://api.whatsapp.com/send/?phone=6282187421886&text={pesan_safar}&app_absent=0"
    
    
    rp = 'Rp. '
    
    normal = 'Normal'
    promo = 'Promo'
    normal_tahunan = rp + '6.000.000'
    mingguan = '200.000'
    bulanan = '500.00'
    tahunan = '5.600.000'
    
    context = {
        'normal': normal,
        'promo': promo,
        'harga_mingguan': mingguan,
        'harga_bulanan': bulanan,
        'harga_tahunan': tahunan,
        'harga_normal_tahunan': normal_tahunan,
        'pesan_safar': api_safar,
        'pesan_sarif': api_sarif,

    }
    
    
    return render(request, 'index.html', context)