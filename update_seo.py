import os
import glob
import re

template = '''<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="canonical" href="{CANONICAL}">
  <link rel="preload" href="{ASSETS}css/main.css?v=128" as="style">
  
  <title>{TITLE}</title>
  <meta name="description" content="{DESC}">
  <meta name="keywords" content="{KW}">

  <!-- Favicons -->
  <link href="{ASSETS}img/favicon-peralatan-kantor.webp" rel="icon" type="image/webp">
  <link href="{ASSETS}img/favicon-peralatan-kantor.webp" rel="apple-touch-icon">

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com" rel="preconnect">
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <!-- Vendor CSS -->
  <link href="{ASSETS}vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="{ASSETS}vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="{ASSETS}vendor/aos/aos.css" rel="stylesheet">
  <link href="{ASSETS}vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="{ASSETS}vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

  <!-- Main CSS -->
  <link href="{ASSETS}css/main.css?v=128" rel="stylesheet">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{CANONICAL}">
  <meta property="og:title" content="{TITLE}">
  <meta property="og:description" content="{DESC}">
  <meta property="og:image" content="{IMAGE}">
  <meta property="og:locale" content="id_ID">
  <meta property="og:site_name" content="Peralatan Kantor">

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="{CANONICAL}">
  <meta property="twitter:title" content="{TITLE}">
  <meta property="twitter:description" content="{DESC}">
  <meta property="twitter:image" content="{IMAGE}">

  <!-- JSON-LD: LocalBusiness Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Peralatan Kantor",
    "image": "https://peralatankantor.web.id/assets/img/logo-peralatan-kantor.webp",
    "@id": "https://peralatankantor.web.id/#organization",
    "url": "https://peralatankantor.web.id/",
    "telephone": "6288989643555",
    "priceRange": "Rp15.000 - Rp150.000.000",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Jl. Soekarno Hatta No. 45",
      "addressLocality": "Malang",
      "addressRegion": "Jawa Timur",
      "postalCode": "65141",
      "addressCountry": "ID"
    }},
    "geo": {{
      "@type": "GeoCoordinates",
      "latitude": -7.9467,
      "longitude": 112.6155
    }},
    "openingHoursSpecification": {{
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
      ],
      "opens": "08:00",
      "closes": "17:00"
    }},
    "sameAs": [
      "https://www.instagram.com/peralatankantor",
      "https://www.facebook.com/peralatankantor"
    ]
  }}
  </script>
</head>'''

def update_html_files():
    html_files = glob.glob('*.html') + glob.glob('blog/*.html')
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        head_match = re.search(r'<head>.*?</head>', content, flags=re.DOTALL | re.IGNORECASE)
        if not head_match:
            continue
            
        head_html = head_match.group(0)
        
        # Extract variables
        title_match = re.search(r'<title>(.*?)</title>', head_html, re.IGNORECASE)
        title = title_match.group(1) if title_match else "Peralatan Kantor"
        if "Parenza" not in title and "parenza" not in title:
            title = "Parenza - " + title
        if "Peralatan Kantor" not in title and "peralatan kantor" not in title.lower():
            title = title + " | Peralatan Kantor"
        
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', head_html, re.IGNORECASE)
        desc = desc_match.group(1) if desc_match else ""
        if "Parenza" not in desc and "parenza" not in desc.lower():
            desc = "Parenza: " + desc
        
        kw_match = re.search(r'<meta\s+name=["\']keywords["\']\s+content=["\'](.*?)["\']', head_html, re.IGNORECASE)
        kw = kw_match.group(1) if kw_match else "peralatan kantor, vendor atk"
        kw_list = [k.strip() for k in kw.split(',')]
        if not any(k.lower() == 'parenza' for k in kw_list):
            kw_list.insert(0, "parenza")
        if not any(k.lower() == 'peralatan kantor' for k in kw_list):
            kw_list.insert(0, "peralatan kantor")
        kw = ", ".join(kw_list)
        
        can_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', head_html, re.IGNORECASE)
        if can_match:
            canonical = can_match.group(1)
        else:
            canonical = "https://peralatankantor.web.id/" + filename.replace('\\', '/')
            if filename == "index.html":
                canonical = "https://peralatankantor.web.id/"
                
        img_match = re.search(r'<meta\s+property=["\']og:image["\']\s+content=["\'](.*?)["\']', head_html, re.IGNORECASE)
        img = img_match.group(1) if img_match else "https://peralatankantor.web.id/assets/img/bg-hero-maroon-gradasi.webp"
        
        assets = "assets/" if "/" not in filename.replace('\\', '/') else "../assets/"
        
        new_head = template.format(
            CANONICAL=canonical,
            ASSETS=assets,
            TITLE=title,
            DESC=desc,
            KW=kw,
            IMAGE=img
        )
        
        new_content = content[:head_match.start()] + new_head + content[head_match.end():]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")

update_html_files()
