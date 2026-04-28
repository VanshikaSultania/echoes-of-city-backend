from django.core.management.base import BaseCommand
from sites.models import HeritageSite

SITES = [
    {
        "site_id": "bangalore-palace",
        "place_id": "ChIJN1ZKKUkWrjsRzxIVM363-LE",
        "lat_lng": "12.9988,77.5921",
        "hero_image": "https://images.unsplash.com/photo-1738694054579-de87e2590048?w=1600&auto=format&fit=crop&q=80",
        "title_line1": "Bangalore", "title_line2": "Palace",
        "subtitle": "The Tudor Jewel of the Royal City.",
        "metrics": [
            {"label": "YEAR BUILT", "value": "1887"},
            {"label": "STYLE", "value": "Tudor Revival"},
            {"label": "STATUS", "value": "Open to Public", "span": True}
        ],
        "history_title": "The Wodeyar Dynasty &\nThe Windsor Inspiration",
        "history_paragraph1": "Purchased in 1873 by King Chamarajendra Wadiyar X from the Rev. J. Garrett, the grounds of what is now Bangalore Palace became the canvas for a royal dream. Influenced by the architectural grandeur of England's Windsor Castle, the construction began in 1874.",
        "history_paragraph2": "The palace is renowned for its fortified towers, battlements, and turrets. The interiors are a masterclass in elegant craftsmanship, featuring floral motifs, cornices, and wood carvings. The ballroom, where the Maharaja hosted legendary banquets, still resonates with the whispers of Bangalore's aristocratic past.",
        "history_image1": "https://upload.wikimedia.org/wikipedia/commons/7/7b/HH_Sri_Chamarajendra_Wadiyar_X.jpg",
        "history_image2": "https://www.electronic-city.in/images/places/palace-200.jpg",
        "video_title": "Watch and Discover", "video_subtitle": "A CINEMATIC GLIMPSE INTO THE PALACE", "youtube_id": "vDg7xO7Odvg",
        "gallery_title": "The Visual Archive", "gallery_subtitle": "A CURATED COLLECTION OF HERITAGE MOMENTS",
        "gallery_images": [
            "https://images.unsplash.com/photo-1738694054579-de87e2590048?w=800&auto=format&fit=crop&q=80",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/BANGALORE_PALACE_INTERIOR_VIEW.jpg/960px-BANGALORE_PALACE_INTERIOR_VIEW.jpg",
            "https://images.pexels.com/photos/17744269/pexels-photo-17744269.jpeg",
            "https://media.istockphoto.com/id/2198322007/photo/iconic-bangalore-palace-built-in-1887.jpg",
            "https://imgstaticcontent.lbb.in/lbbnew/wp-content/uploads/sites/2/2016/10/BangalorePalace-i.jpg",
            "https://www.holidify.com/images/cmsuploads/compressed/BangalorePalace6_20190919124025.jpg",
            "https://www.holidify.com/images/cmsuploads/compressed/BangalorePalace7_20190920111051.jpg",
        ],
        "address": "Vasanth Nagar, Bengaluru, 560052",
        "theme_text_root": "text-[#434b18]", "theme_border_light": "border-[#434b18]/20",
    },
    {
        "site_id": "tipu-sultan-palace",
        "place_id": "ChIJAeY0tOQVrjsRdZ8hleP7aRo",
        "lat_lng": "12.9593,77.5736",
        "hero_image": "https://media.istockphoto.com/id/178845414/photo/tipu-sultans-summer-palace.jpg?s=612x612&w=0&k=20&c=QCVIS7GrgLfh8MaBmdjrQFNeQ71BgP-K322BJVkGTmo=",
        "title_line1": "Tipu Sultan's", "title_line2": "Summer Palace",
        "hero_title_weight": "font-black",
        "subtitle": 'The "Rash-e-Jannat" (Envy of Heaven)',
        "metrics": [{"label": "ESTABLISHED", "value": "1791"}],
        "history_title": "An Edifice of\nTeak and Triumph",
        "history_paragraph1": "Begun by Hyder Ali in 1781 and completed by his son Tipu Sultan in 1791, the Summer Palace remains one of the most significant examples of Indo-Islamic architecture in South India.",
        "history_paragraph2": "Unlike the stone fortresses of the era, the palace is constructed almost entirely of teakwood. The two-story structure is supported by massive fluted wooden pillars that terminate in beautifully carved scalloped arches.",
        "history_paragraph3": "The ground floor houses a small museum curated by the Archaeological Survey of India, showcasing various artifacts from the Haidar Ali and Tipu era.",
        "history_image1": "https://media.gettyimages.com/id/542381564/photo/daria-daulat-bagh-is-the-summer-palace-of-sultan-fateh-ali-tipu-ruler-of-the-kingdom-of-mysore.jpg?s=612x612",
        "history_image2": "https://media.gettyimages.com/id/170967432/photo/a-wooden-palace-with-beautifully-carved-pillars-arches-and-balconies-which-served-as-the.jpg?s=612x612",
        "video_title": "The Tiger of Mysore", "video_subtitle": "A CINEMATIC DOCUMENTARY EXPLORATION", "youtube_id": "etqxOXLdsZM",
        "gallery_title": "The Visual Archive", "gallery_subtitle": "A CURATED COLLECTION OF ARCHITECTURAL GRANDEUR",
        "gallery_images": [
            "https://s7ap1.scene7.com/is/image/incredibleindia/2-tipu-sultan-summer-palace-bangalore-karnataka-attr-hero-1?qlt=82",
            "https://s7ap1.scene7.com/is/image/incredibleindia/tipu-sultans-summer-palace-bengaluru-karnataka-8-musthead-hero?qlt=82",
            "https://s7ap1.scene7.com/is/image/incredibleindia/tipu-sultans-summer-palace-bengaluru-karnataka-11-musthead-hero?qlt=82",
            "https://s7ap1.scene7.com/is/image/incredibleindia/tipu-sultans-summer-palace-bengaluru-karnataka-9-musthead-hero?qlt=82",
        ],
        "address": "Albert Victor Road, Chamrajpet, Bengaluru, 560018",
        "theme_text_root": "text-[#111111]", "theme_border_light": "border-[#111111]/30",
    },
    {
        "site_id": "vidhana-soudha",
        "place_id": "ChIJpwxMCXIWrjsRfedVMltgoP8",
        "lat_lng": "12.9796,77.5908",
        "hero_image": "https://t4.ftcdn.net/jpg/07/52/84/27/240_F_752842748_TMfPQUmG4kffW5uaZTdjj9yVLYDeRSm2.jpg",
        "title_line1": "Vidhana", "title_line2": "Soudha",
        "hero_title_color": "text-[#4b2e1f]", "metric_text_color": "text-[#3b2418]",
        "subtitle": "",
        "metrics": [
            {"label": "COMPLETED", "value": "1956"},
            {"label": "STYLE", "value": "Neo-Dravidian"},
            {"label": "ROLE", "value": "State Legislature", "span": True}
        ],
        "history_title": "An Architectural Marvel of\nNeo-Dravidian Splendor",
        "history_paragraph1": "Conceived by Kengal Hanumanthaiah, the then Chief Minister of Mysore, the Vidhana Soudha was born out of a desire to create a spectacular edifice that would overshadow the colonial structures of the Cantonment.",
        "history_paragraph2": "The building features sweeping staircases, massive pillars, and majestic domes, incorporating elements from Chalukyan, Hoysala, and Vijayanagara styles.",
        "history_paragraph3": "Today, it houses the Karnataka State Legislature and the Secretariat. While public access to the interiors is restricted, the sheer scale and grandeur of the exterior make it one of the most magnificent public buildings in the country.",
        "history_image1": "https://thumbs.dreamstime.com/b/vidhana-soudha-bangalore-india-105169934.jpg",
        "history_image2": "https://thumbs.dreamstime.com/b/vidhana-soudha-bangalore-152008902.jpg",
        "video_title": "The Heart of Democracy", "video_subtitle": "A GLIMPSE OF THE NEO-DRAVIDIAN MASTERPIECE", "youtube_id": "Vjj2OCS3Cl4",
        "gallery_title": "The Visual Archive", "gallery_subtitle": "A CURATED COLLECTION OF DEMOCRATIC GRANDEUR",
        "gallery_images": [
            "https://cdn.pixabay.com/photo/2014/03/22/17/11/suvarna-vidhana-soudha-292732__480.jpg",
            "https://mir-s3-cdn-cf.behance.net/project_modules/1400/80737620134923.562e619eab40a.jpg",
            "https://live.staticflickr.com/5544/11638045765_c8ca0fdcfe_b.jpg",
            "https://wallpapercave.com/wp/wp15408952.jpg",
            "https://eindiatourism.in/wp-content/uploads/2023/05/Vidhana_Soudha_in_night_4.jpg",
        ],
        "address": "Dr Ambedkar Veedhi, Sampangi Rama Nagar, Bengaluru, 560001",
        "theme_text_root": "text-[#eeeae2]", "theme_border_light": "border-[#eeeae2]/30",
    },
    {
        "site_id": "bull-temple",
        "place_id": "ChIJX9XqWswVrjsRRH3ymQ8yCDQ",
        "lat_lng": "12.9416,77.5683",
        "hero_image": "https://temple.yatradham.org/public/Product/temple/temple_hzOxj2OQ_202408171754050.jpeg",
        "title_line1": "Bull", "title_line2": "Temple",
        "hero_title_color": "text-[#4b2e1f]", "hero_subtitle_color": "text-[#4b2e1f]",
        "metric_text_color": "text-[#4b2e1f]", "hero_title_weight": "font-bold",
        "subtitle": "The Sacred Guardian of Basavanagudi",
        "metrics": [
            {"label": "ESTABLISHED", "value": "1537"},
            {"label": "STYLE", "value": "Dravidian"},
            {"label": "FESTIVAL", "value": "Kadalekai Parishe", "span": True}
        ],
        "history_title": "A Monument to Local Legends",
        "history_paragraph1": "Built in 1537 by Kempe Gowda I, the founder of Bangalore, the Bull Temple is situated on the picturesque Bugle Hill in the historic neighborhood of Basavanagudi. It is exclusively dedicated to Nandi, the celestial bull and vehicle of Lord Shiva.",
        "history_paragraph2": "The story behind its construction is rooted in local folklore. A wild bull was said to be ravaging the groundnut crops of local farmers. To appease the magnificent creature, Kempe Gowda erected this temple.",
        "history_paragraph3": "The centerpiece of the temple is the colossal Nandi statue, carved entirely from a single granite rock. Measuring 4.5 meters in height and 6 meters in length, the statue is continuously rubbed with coconut oil and butter by devotees.",
        "history_image1": "https://www.holidify.com/images/cmsuploads/compressed/Outside_the_Bull_Temple,_Bangalore,_India_20170916114001.jpg",
        "history_image2": "https://chalbanjare.com/crm/sys_images/Shri_Doddabasavanna_Temple1765526202.webp",
        "video_title": "Basavanagudi's Beating Heart", "video_subtitle": "EXPERIENCE THE KADALEKAI PARISHE", "youtube_id": "B1oqWZMttGc",
        "gallery_title": "The Sacred Archive", "gallery_subtitle": "A CURATED GLIMPSE INTO DEVOTION",
        "gallery_images": [
            "https://www.holidify.com/images/cmsuploads/compressed/Outside_the_Bull_Temple,_Bangalore,_India_20170916114001.jpg",
            "https://lh3.googleusercontent.com/p/AF1QipOfMT_tY7NhQyX73nrCiZLL14ROX_ffwjUQxAi1=s680-w680-h510",
            "https://chalbanjare.com/crm/sys_images/Shri_Doddabasavanna_Temple1765526202.webp",
            "https://eindiatourism.in/wp-content/uploads/2023/05/Nandi_Temple_252276307-1-640x440.jpeg",
            "https://thumbs.dreamstime.com/b/bull-temple-detail-bangalore-india-28249071.jpg",
        ],
        "address": "Bugle Rock Rd, Basavanagudi, Bengaluru, 560004",
        "theme_text_root": "text-[#eeeae2]", "theme_border_light": "border-[#eeeae2]/30",
    },
    {
        "site_id": "cubbon-park",
        "place_id": "ChIJL2fQ53MWrjsRuN9D6aalLMY",
        "lat_lng": "12.9765,77.5946",
        "hero_image": "https://karnatakatourism.org/wp-content/uploads/2020/06/cabbon-park.jpg",
        "title_line1": "Cubbon", "title_line2": "Park",
        "hero_title_color": "text-[#6b4423]", "hero_subtitle_color": "text-[#6b4423]",
        "metric_text_color": "text-[#6b4423]", "hero_title_weight": "font-black",
        "subtitle": "The Lung of the City",
        "metrics": [
            {"label": "ESTABLISHED", "value": "1870"},
            {"label": "AREA", "value": "300 Acres"},
            {"label": "COMMISSIONED BY", "value": "Maj. Gen. Richard Sankey", "span": True}
        ],
        "history_title": "An Eden in the\nHeart of the Metropolis",
        "history_paragraph1": "Originally spanning 100 acres, this historic park was commissioned in 1870 by Major General Richard Sankey, the then Chief Engineer of the State. Over the years, the park expanded to its current footprint of 300 acres.",
        "history_paragraph2": "The park is renowned for its rich botanical diversity, hosting over 6,000 trees and plants, encompassing indigenous species and exotic introductions.",
        "history_paragraph3": "Dotted amongst the verdant landscapes are numerous red-stone colonial buildings, marble statues of historical luminaries, and elegant pavilions.",
        "history_image1": "https://karnatakatourism.org/wp-content/uploads/2020/06/cabbon-park.jpg",
        "history_image2": "https://www.trawell.in/admin/images/upload/148027234CubbonPark_Main.jpg",
        "video_title": "A Walk Through Time", "video_subtitle": "EXPLORING THE GREEN HEART", "youtube_id": "CldXQKZHzP8",
        "gallery_title": "Botanical Archives", "gallery_subtitle": "A CURATED GLIMPSE INTO NATURE'S ARTISTRY",
        "gallery_images": [
            "https://karnatakatourism.org/wp-content/uploads/2020/06/cabbon-park.jpg",
            "https://blogs.revv.co.in/blogs/wp-content/uploads/2020/01/Cubbon-Park-Bangalore.jpeg",
            "https://www.holidify.com/images/cmsuploads/compressed/C1_20170905112652.PNG",
            "https://media.istockphoto.com/id/1416330148/photo/the-beautiful-gardens-of-the-cubbon-park-in-bangalore.jpg?s=612x612",
        ],
        "address": "Kasturba Road, Sampangi Rama Nagar, Bengaluru, 560001",
        "theme_text_root": "text-[#eeeae2]", "theme_border_light": "border-[#eeeae2]/30",
    },
    {
        "site_id": "lalbagh-glass-house",
        "place_id": "ChIJHdPykcEVrjsRIr4v35kLEY4",
        "lat_lng": "12.9507,77.5848",
        "hero_image": "https://gumlet.assettype.com/homegrown/2023-04/e0496c82-b789-4698-8fd7-89026c8b088d/lalbagh2.jpeg?auto=format%2Ccompress&w=1200",
        "title_line1": "Lalbagh", "title_line2": "Botanical Garden",
        "hero_title_color": "text-[#1a3a1a]", "hero_subtitle_color": "text-[#1a3a1a]",
        "metric_text_color": "text-[#1a3a1a]", "hero_title_weight": "font-black",
        "subtitle": "The Garden of the Red Flowers",
        "metrics": [
            {"label": "ESTABLISHED", "value": "1760"},
            {"label": "AREA", "value": "240 Acres"},
            {"label": "COMMISSIONED BY", "value": "Hyder Ali", "span": True}
        ],
        "history_title": "A Royal Garden Born\nof Mughal Vision",
        "history_paragraph1": "Laid out by Hyder Ali in 1760 on the southern fringes of Bangalore, Lalbagh — meaning 'Red Garden' — was inspired by the magnificent Mughal gardens of Northern India.",
        "history_paragraph2": "After the fall of Tipu Sultan in 1799, the British took over Lalbagh and commissioned Scottish botanist William Roxburgh to formalize the garden as a botanical research centre.",
        "history_paragraph3": "The iconic Glass House, constructed in 1889 and inspired by London's famed Crystal Palace, remains Lalbagh's crown jewel, hosting the celebrated biannual Flower Shows.",
        "history_image1": "https://www.citybit.in/wp-content/uploads/2024/05/Things-to-See-at-Lalbagh-Botanical-Garden-1024x576.jpg",
        "history_image2": "https://www.tusktravel.com/blog/wp-content/uploads/2023/08/Lalbagh-Botanical-Garden-Bangalore.jpg",
        "video_title": "Inside the Glass House", "video_subtitle": "A CINEMATIC WALK THROUGH LALBAGH", "youtube_id": "EBWcFcRBqdA",
        "gallery_title": "The Botanical Archive", "gallery_subtitle": "A CURATED COLLECTION OF LALBAGH'S SPLENDOUR",
        "gallery_images": [
            "https://www.citybit.in/wp-content/uploads/2024/05/Things-to-See-at-Lalbagh-Botanical-Garden-1024x576.jpg",
            "https://sceneloc8.com/wp-content/uploads/2024/03/Lalbagh-Botanical-Garden-2.png",
            "https://www.tusktravel.com/blog/wp-content/uploads/2023/08/Lalbagh-Botanical-Garden-Bangalore.jpg",
            "https://images.trvl-media.com/media/content/shared/images/travelguides/destination/622/Lalbagh-Botanical-Gardens-98413.jpg",
            "https://thumbs.dreamstime.com/b/lalbagh-botanical-gardens-bangalore-karnataka-116604066.jpg",
        ],
        "address": "Lalbagh Road, Mavalli, Bengaluru, Karnataka 560004",
        "theme_text_root": "text-[#eeeae2]", "theme_border_light": "border-[#eeeae2]/30",
    },
    {
        "site_id": "begur-fort",
        "place_id": "ChIJUeP-lDRrrjsR1wQxWlw79Y4",
        "lat_lng": "12.8821,77.6256",
        "hero_image": "https://3.bp.blogspot.com/_QQ7MLfwirhM/TDBJOLlEDlI/AAAAAAAAAAM/cqnKoq_AAEk/s1600/Begur+033.JPG",
        "title_line1": "Begur", "title_line2": "Fort",
        "hero_title_color": "text-[#3c1414]", "hero_subtitle_color": "text-[#3c1414]",
        "metric_text_color": "text-[#3c1414]", "hero_title_weight": "font-black",
        "subtitle": "The Threshold of Bengaluru's Earliest Memory",
        "metrics": [
            {"label": "CENTURY", "value": "8th – 9th CE"},
            {"label": "DYNASTY", "value": "Ganga Kingdom"},
            {"label": "SIGNIFICANCE", "value": "Oldest Bengaluru Inscription", "span": True}
        ],
        "history_title": "Where the Name Bengaluru Was Born",
        "history_paragraph1": "Nestled 15 km south of the city, Begur Fort is one of the most historically significant sites in the entire Bangalore region. The fortification dates to the rule of the Ganga dynasty in the 8th and 9th centuries CE.",
        "history_paragraph2": "Within the fort complex stands the remarkable Panchalingeswara Temple, a celebrated example of Dravidian architecture housing five Shivalingas within five separate sanctums.",
        "history_paragraph3": "A stone inscription dated 890 CE discovered within the fort contains one of the earliest written references to 'Bengaluru' — making it a foundational document in the city's recorded history.",
        "history_image1": "https://www.visitacostabrava.com/media/items/fullhd/cbca1-castillo-de-begur.jpg",
        "history_image2": "https://2.bp.blogspot.com/-LEDgpx_dN8Q/XJUc1iRjWiI/AAAAAAAATns/VnBftSHBug8ZuCFYW7lfp2BOfyEKQuA8gCLcBGAs/s1600/10.%2BBegur%2BForts%2Bof%2BKarnataka-01.jpeg",
        "video_title": "Echoes of the Gangas", "video_subtitle": "A JOURNEY INTO BEGUR'S ANCIENT PAST", "youtube_id": "EfIl7LkR-ec",
        "gallery_title": "The Stone Archive", "gallery_subtitle": "A CURATED RECORD OF BEGUR'S ANCIENT LEGACY",
        "gallery_images": [
            "https://2.bp.blogspot.com/-LEDgpx_dN8Q/XJUc1iRjWiI/AAAAAAAATns/VnBftSHBug8ZuCFYW7lfp2BOfyEKQuA8gCLcBGAs/s1600/10.%2BBegur%2BForts%2Bof%2BKarnataka-01.jpeg",
            "https://lakshmisharath.com/wp-content/uploads/2015/08/Begur-temple-1024x685.jpg",
            "https://lakshmisharath.com/wp-content/uploads/2015/08/Begur-ruins.jpg",
            "https://3.bp.blogspot.com/_QQ7MLfwirhM/TDBJOLlEDlI/AAAAAAAAAAM/cqnKoq_AAEk/s1600/Begur+033.JPG",
        ],
        "address": "Begur, South Bengaluru, Karnataka 560068",
        "theme_text_root": "text-[#f5efe6]", "theme_border_light": "border-[#f5efe6]/30",
    },
    {
        "site_id": "ulsoor-lake",
        "place_id": "ChIJeT03x54VrjsRi14iL9r8w9Q",
        "lat_lng": "12.9818,77.6190",
        "hero_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/8e/cb/3f/caption.jpg?w=1200&h=-1&s=1",
        "title_line1": "Ulsoor", "title_line2": "Lake",
        "hero_title_color": "text-[#1a3a1a]", "hero_subtitle_color": "text-[#1a3a1a]",
        "metric_text_color": "text-[#1a3a1a]", "hero_title_weight": "font-black",
        "subtitle": "A Sprawling Expanse of Historic Waters",
        "metrics": [
            {"label": "COMMISSIONED", "value": "16th Century"},
            {"label": "AREA", "value": "123 Acres"},
            {"label": "FOUNDER", "value": "Kempe Gowda II", "span": True}
        ],
        "history_title": "An Ancient Reservoir\nin the Heart of the City",
        "history_paragraph1": "Ulsoor Lake, also known as Halasuru Kere, is one of the largest and oldest lakes in Bangalore, sprawling over an area of 123 acres. The history of a water body at this site dates back to the time of Kempe Gowda II in the late 16th century.",
        "history_paragraph2": "Dotted with picturesque islands and lined with verdant greenery, the lake has been an integral part of the city's ecosystem and cultural landscape.",
        "history_paragraph3": "Today, it serves as a popular recreational spot, offering boating facilities and a tranquil escape from the urban rush. The lake also plays a central role during the Ganesha Chaturthi festival.",
        "history_image1": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Ulsoor_Lake_Bangalore.jpg",
        "history_image2": "https://images.travelandleisureasia.com/wp-content/uploads/sites/2/2023/12/12104523/ulsoor-lake.jpeg",
        "video_title": "Tranquil Waters", "video_subtitle": "A GLIMPSE INTO ULSOOR'S SERENITY", "youtube_id": "vH_D4U0r5M4",
        "gallery_title": "The Water Archive", "gallery_subtitle": "A CURATED GLIMPSE INTO NATURE'S MIRROR",
        "gallery_images": [
            "https://upload.wikimedia.org/wikipedia/commons/e/ec/Ulsoor_Lake_Bangalore.jpg",
            "https://images.travelandleisureasia.com/wp-content/uploads/sites/2/2023/12/12104523/ulsoor-lake.jpeg",
            "https://media-cdn.tripadvisor.com/media/photo-s/0e/46/58/01/ulsoor-lake.jpg",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/8e/cb/3f/caption.jpg?w=1200&h=-1&s=1",
            "https://www.holidify.com/images/cmsuploads/compressed/Ulsoor_Lake_20191212140416.jpg",
        ],
        "address": "Ulsoor, Bengaluru, Karnataka 560008",
        "theme_text_root": "text-[#eeeae2]", "theme_border_light": "border-[#eeeae2]/30",
    },
    {
        "site_id": "nandi-hills",
        "place_id": "ChIJF-r860XksTsRCGYZWSn3ORY",
        "lat_lng": "13.3702,77.6835",
        "hero_image": "https://s7ap1.scene7.com/is/image/incredibleindia/nandi-hills-bangalore-karnataka-1-attr-hero?qlt=82&ts=1742171255239",
        "title_line1": "Nandi", "title_line2": "Hills",
        "hero_title_color": "text-[#2d3a1a]", "hero_subtitle_color": "text-[#2d3a1a]",
        "metric_text_color": "text-[#2d3a1a]", "hero_title_weight": "font-black",
        "subtitle": "The Hill of Happiness",
        "metrics": [
            {"label": "ALTITUDE", "value": "1,478 m"},
            {"label": "ESTABLISHED", "value": "Ganga Dynasty"},
            {"label": "FAMOUS FOR", "value": "Sunrise Views", "span": True}
        ],
        "history_title": "A Fortress in the Clouds",
        "history_paragraph1": "Nandi Hills, or Nandidurga, is an ancient hill fortress in southern India, in the Chikkaballapur district of Karnataka state. It is located 60 km from Bengaluru. The hills are nestled near the town of Nandi.",
        "history_paragraph2": "In traditional belief, the hills are the origin of the Arkavathy, Ponnaiyar, Palar, Papagni, and Penna rivers. The hills are named after the ancient Dravidian temple dedicated to the bull Nandi, which stands on the hillock.",
        "history_paragraph3": "The fort was fortified by Tipu Sultan and later used by British officials as a summer retreat due to its cool climate and scenic beauty.",
        "history_image1": "https://theroamingshoes.com/wp-content/uploads/2020/10/IMG_20200115_063704.jpg",
        "history_image2": "https://theroamingshoes.com/wp-content/uploads/2020/10/IMG_20200115_062336.jpg",
        "video_title": "Above the Clouds", "video_subtitle": "A CINEMATIC JOURNEY TO NANDI HILLS", "youtube_id": "iRQ8KidoXFE",
        "gallery_title": "The Cloud Archive", "gallery_subtitle": "A CURATED GLIMPSE INTO THE HILL'S SPLENDOUR",
        "gallery_images": [
            "https://s7ap1.scene7.com/is/image/incredibleindia/nandi-hills-bangalore-karnataka-2-attr-hero?qlt=82&ts=1742174246149",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Sunrise_at_Nandi_Hills.jpg/500px-Sunrise_at_Nandi_Hills.jpg",
            "https://theroamingshoes.com/wp-content/uploads/2020/10/IMG_20200115_062336.jpg",
        ],
        "address": "Chikkaballapur, Karnataka 562101",
        "theme_text_root": "text-[#eeeae2]", "theme_border_light": "border-[#eeeae2]/30",
    },
]


class Command(BaseCommand):
    help = 'Seeds the database with all heritage site data from heritageSites.js'

    def handle(self, *args, **kwargs):
        # --- Create/Reset Admin ---
        from django.contrib.auth.models import User
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'Admin@123')
            self.stdout.write(self.style.SUCCESS('  ✓ Created Superuser: admin / Admin@123'))
        else:
            # Optional: Reset password if you want to be sure
            u = User.objects.get(username='admin')
            u.set_password('Admin@123')
            u.save()
            self.stdout.write(self.style.SUCCESS('  ↻ Updated Admin Password: Admin@123'))

        created_count = 0
        updated_count = 0
        for data in SITES:
            # We don't want to pass 'type_tag' to defaults if it's not in the model
            # but I added it to SITES earlier. Let's make sure it's handled.
            site_data = data.copy()
            obj, created = HeritageSite.objects.update_or_create(
                site_id=site_data.pop('site_id'),
                defaults=site_data,
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created: {obj}'))
            else:
                updated_count += 1
                self.stdout.write(self.style.WARNING(f'  ↻ Updated: {obj}'))

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! {created_count} created, {updated_count} updated.'
        ))

