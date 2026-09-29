import os

base_dir = r"c:\Users\Dell\Downloads\peralatankantor.web.id-20260823T095322Z-1-001\peralatankantor.web.id"
template_path = os.path.join(base_dir, "_detail_template.html")

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

def generate_list_html(items):
    html = ""
    for item in items:
        html += f'<li class="mb-2"><i class="bi bi-check-circle-fill text-gold me-2"></i> {item}</li>\n'
    return html

packages = [
    {
        "slug": "detail-paket-atk-kantor-baru",
        "title": "Paket ATK Kantor Baru",
        "description": "Paket komprehensif alat tulis dan perlengkapan meja untuk instansi atau cabang baru. Kami menyiapkan seluruh kebutuhan administrasi dasar sehingga karyawan Anda bisa langsung bekerja sejak hari pertama tanpa pusing memikirkan ATK yang kurang.",
        "image_url": "assets/img/paket/paket-atk-kantor-baru.webp",
        "badge": "Kantor Baru / Cabang Instansi",
        "parent_name": "Paket",
        "parent_link": "paket.html",
        "tanya_type": "Paket",
        "list_title": "Isi Paket",
        "items": [
            "Kertas HVS (A4 & F4) 1 Dus",
            "Pulpen, Pensil, Stabilo, Spidol (1 Set per meja)",
            "Ordner & Map File plastik",
            "Stapler, Perforator, Gunting",
            "Buku Ekspedisi & Blocknote",
            "Tinta Printer (Sesuai merk)",
            "Gratis ongkos kirim (S&K berlaku)"
        ]
    },
    {
        "slug": "detail-paket-furniture-kantor-lengkap",
        "title": "Paket Furniture Kantor Lengkap",
        "description": "Paket lengkap pengadaan furnitur untuk satu ruang kerja standar. Mulai dari meja direktur/staff, kursi ergonomis yang nyaman untuk bekerja seharian, hingga lemari arsip berbahan metal yang anti rayap dan kokoh.",
        "image_url": "assets/img/paket/paket-furniture-kantor-lengkap.webp",
        "badge": "Renovasi Kantor / Ruang Kerja Baru",
        "parent_name": "Paket",
        "parent_link": "paket.html",
        "tanya_type": "Paket",
        "list_title": "Isi Paket",
        "items": [
            "1 Meja Kerja Utama (Desain Minimalis/Modern)",
            "1 Kursi Ergonomis Mesh (Sandaran Punggung & Kepala)",
            "1 Lemari Arsip Besi (Pintu Tarik/Sliding)",
            "1 Laci Dorong (Mobile Drawer) 3 Susun",
            "Jasa Perakitan dan Instalasi di Lokasi"
        ]
    },
    {
        "slug": "detail-paket-videotron-instansi",
        "title": "Paket Videotron Instansi",
        "description": "Solusi display LED Videotron indoor maupun outdoor beresolusi tinggi untuk kebutuhan auditorium, lobi, atau papan informasi depan gedung pemerintahan. Harga sudah termasuk survei lokasi, pemasangan struktur, dan garansi.",
        "image_url": "assets/img/paket/paket-videotron-instansi.webp",
        "badge": "Gedung Pemerintahan / Auditorium",
        "parent_name": "Paket",
        "parent_link": "paket.html",
        "tanya_type": "Paket",
        "list_title": "Fasilitas Paket",
        "items": [
            "Layar LED Videotron (Pixel Pitch P1.8 - P4 Indoor / P4 - P10 Outdoor)",
            "Video Processor & Sending Card System",
            "Struktur Rangka Besi (Custom sesuai lokasi)",
            "Instalasi Kelistrikan & Panel Distribusi",
            "Training Penggunaan Software (Novastar, dll)",
            "Uji Coba & Garansi 1 Tahun"
        ]
    },
    {
        "slug": "detail-paket-atk-bulanan-instansi",
        "title": "Paket ATK Bulanan Instansi",
        "description": "Program kontrak berlangganan suplai alat tulis kantor setiap bulan. Anda tidak perlu repot melakukan pengadaan ulang, karena kami akan mengirimkan stok ATK secara rutin sesuai daftar kebutuhan (SLA) yang disepakati.",
        "image_url": "assets/img/paket/paket-atk-bulanan-instansi.webp",
        "badge": "Kontrak Suplai / Pengadaan Rutin",
        "parent_name": "Paket",
        "parent_link": "paket.html",
        "tanya_type": "Paket",
        "list_title": "Keuntungan Berlangganan",
        "items": [
            "Pengiriman rutin terjadwal setiap awal/akhir bulan",
            "Sistem pembayaran termin (Tempo) untuk B2B/B2G",
            "Satu pintu untuk semua kebutuhan operasional",
            "Prioritas stok barang",
            "Laporan penggunaan per divisi"
        ]
    },
    {
        "slug": "detail-paket-ruang-meeting-lengkap",
        "title": "Paket Ruang Meeting Lengkap",
        "description": "Paket komprehensif untuk melengkapi 1 ruang rapat atau meeting room, mencakup furnitur dan sistem display. Cukup satu paket, ruang meeting Anda siap digunakan secara profesional untuk rapat, presentasi, dan diskusi instansi.",
        "image_url": "assets/img/paket/paket-ruang-meeting-lengkap.webp",
        "badge": "Ruang Rapat Baru / Meeting Room",
        "parent_name": "Paket",
        "parent_link": "paket.html",
        "tanya_type": "Paket",
        "list_title": "Isi Paket",
        "items": [
            "1 Meja meeting ukuran besar (kapasitas 6-8 orang)",
            "6-8 Kursi rapat dengan sandaran nyaman",
            "1 Layar videotron/display presentasi (Atau Interactive Flat Panel)",
            "Instalasi & penataan ruang oleh tim kami",
            "Uji coba sistem display presentasi"
        ]
    }
]

products = [
    {
        "slug": "detail-produk-kursi-kantor-ergonomis-mesh",
        "title": "Kursi Kantor Ergonomis Mesh",
        "description": "Kursi staff yang dirancang khusus untuk kesehatan tulang belakang. Menggunakan material mesh (jaring) yang breathable agar tidak panas saat diduduki berjam-jam. Dilengkapi dengan sandaran kepala dan tangan yang bisa diatur (adjustable).",
        "image_url": "assets/img/produk/kursi-kantor-ergonomis-mesh.webp",
        "badge": "Staff & Karyawan",
        "parent_name": "Katalog Produk",
        "parent_link": "produk-kursi-kantor.html",
        "tanya_type": "Produk",
        "list_title": "Spesifikasi Unggulan",
        "items": [
            "Material sandaran punggung Mesh Breathable",
            "Dudukan busa density tinggi (High-Density Foam)",
            "Mekanisme ayun (Tilt-mechanism) dengan pengunci",
            "Gaslift hidrolik garansi 1 tahun",
            "Roda nylon mulus dan kokoh",
            "Tersedia berbagai pilihan warna"
        ]
    },
    {
        "slug": "detail-produk-kursi-direktur-kulit-hitam",
        "title": "Kursi Direktur Kulit Hitam Premium",
        "description": "Kursi eksekutif dengan desain high-back yang elegan dan mewah. Dibalut material kulit sintetis premium yang mudah dibersihkan. Dudukan sangat empuk, memberikan representasi wibawa bagi pimpinan instansi atau manajerial.",
        "image_url": "assets/img/produk/kursi-direktur-kulit-hitam.webp",
        "badge": "Direktur & Pimpinan",
        "parent_name": "Katalog Produk",
        "parent_link": "produk-kursi-kantor.html",
        "tanya_type": "Produk",
        "list_title": "Spesifikasi Unggulan",
        "items": [
            "Material PU Leather (Kulit Sintetis Premium Hitam)",
            "Desain High-Back menopang seluruh punggung",
            "Busa ekstra tebal di bagian kepala dan dudukan",
            "Sandaran tangan berlapis bantalan empuk",
            "Kaki kursi (Footbase) berbahan metal chrome anti karat",
            "Mampu menahan beban hingga 120kg"
        ]
    },
    {
        "slug": "detail-produk-meja-kantor-minimalis-kayu",
        "title": "Meja Kantor Minimalis Kayu",
        "description": "Meja kerja dengan desain perpaduan industrial dan minimalis modern. Permukaan meja terbuat dari material olahan kayu (engineering wood / MFC) dengan finishing halus, ditopang oleh rangka kaki besi yang kuat dan tidak goyang.",
        "image_url": "assets/img/produk/meja-kantor-minimalis-kayu.webp",
        "badge": "Meja Staff / Meja Kerja Utama",
        "parent_name": "Katalog Produk",
        "parent_link": "produk-meja-kantor.html",
        "tanya_type": "Produk",
        "list_title": "Spesifikasi Unggulan",
        "items": [
            "Permukaan meja MFC tebal 25mm (Tahan Gores & Air)",
            "Dimensi: P 120cm x L 60cm x T 75cm",
            "Kaki besi dengan powder coating anti karat",
            "Dilengkapi lubang kabel (Grommet) untuk kerapian",
            "Warna kayu cerah (Maple / Cherry / Oak)",
            "Desain mudah dirakit (Knockdown)"
        ]
    }
]

for item in packages + products:
    html = template
    html = html.replace('{TITLE}', item['title'])
    html = html.replace('{SLUG}', item['slug'])
    html = html.replace('{DESCRIPTION}', item['description'])
    html = html.replace('{IMAGE_URL}', item['image_url'])
    html = html.replace('{BADGE}', item['badge'])
    html = html.replace('{PARENT_NAME}', item['parent_name'])
    html = html.replace('{PARENT_LINK}', item['parent_link'])
    html = html.replace('{TANYA_TYPE}', item['tanya_type'])
    html = html.replace('{LIST_TITLE}', item['list_title'])
    html = html.replace('{LIST_HTML}', generate_list_html(item['items']))
    
    if "paket" in item['slug']:
        html = html.replace('{PAKET_ACTIVE}', 'active')
        html = html.replace('{PRODUK_ACTIVE}', '')
    else:
        html = html.replace('{PAKET_ACTIVE}', '')
        html = html.replace('{PRODUK_ACTIVE}', 'active')
        
    out_path = os.path.join(base_dir, f"{item['slug']}.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {item['slug']}.html")
