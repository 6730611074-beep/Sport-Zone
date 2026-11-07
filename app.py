
from flask import Flask, render_template, request

app = Flask(__name__)

# ข้อมูลอุปกรณ์กีฬา
products = [
    {
        "name": "ลูกฟุตบอล",
        "category": "ฟุตบอล",
        "price": 1100,
        "description": "เหมาะสำหรับฝึกซ้อมและเล่นฟุตบอล",
        "image": "https://www.supersports.co.th/cdn/shop/files/AD001SH809EMTH-0.jpg?v=1751527462&width=900",
        "shop_url":" https://www.supersports.co.th/collections/sports-football-balls/products/adidas-soccer-accessories-ball-4-5-ad001sh809emth-jp1541?tab=description"
    },
    {
        "name": "F50 ELITE LAMINE YAMAL",
        "category": "ฟุตบอล",
        "price": 3010,
        "description": "เหมาะสำหรับเล่นฟุตบอลตำแหน่งกองหน้า",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0IcWiI0DuIm8-3hSGXSe5OTv6xZDZ6MrEi_lJL1Nd-w&s=10",
        "shop_url":" https://www.adidas.co.th/th/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%9F%E0%B8%B8%E0%B8%95%E0%B8%9A%E0%B8%AD%E0%B8%A5%E0%B9%84%E0%B8%A3%E0%B9%89%E0%B9%80%E0%B8%8A%E0%B8%B7%E0%B8%AD%E0%B8%81-f50-elite-lamine-yamal-firm-ground-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B9%80%E0%B8%94%E0%B9%87%E0%B8%81/KK3631.html"
    },
    {
        "name": "Adidas Predator League",
        "category": "ฟุตบอล",
        "price": 3600,
        "description": "เหมาะสำหรับเล่นฟุตบอลในตำแหน่งกองกลาง",
        "image": "https://assets.adidas.com/images/w_500,f_auto,q_auto/73ad11be965946229d2c8bc85ec05c74_9366/Predator_League_Fold-Over_Tongue_Firm_Ground_JP6278_HM1.jpg",
        "shop_url":"https://www.adidas.co.th/th/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%9F%E0%B8%B8%E0%B8%95%E0%B8%9A%E0%B8%AD%E0%B8%A5-predator-league-fold-over-tongue-artificial-ground/IH7164.html"
     },
    {
        "name": "Nike Tiempo LegendL",
        "category": "ฟุตบอล",
        "price": 2900,
        "description": "เหมาะสำหรับเล่นฟุตบอลในตำแหน่งกองหลัง",
        "image": "https://www.supersports.co.th/cdn/shop/files/NI083SH002EKTH-0.jpg?v=1743764697&width=900",
        "shop_url":" https://www.supersports.co.th/en/products/nike-soccer-shoes-firm-ground-ni083sh002ekth-ib9520-401?tab=description"
    },
    {
            "name": "NIKE Mercurial Vapor 17 Elite AG",
            "category": "ฟุตบอล",
            "price": 6370,
            "description": "รองเท้าที่นักบอลส่วนใหญ่ใช้กัน",
            "image": "https://static.nike.com/a/images/t_web_pdp_535_v2/f_auto,u_9ddf04c7-2a9a-4d76-add1-d15af8f0263d,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/c1451ee6-5fd7-4e1c-960c-c67c1bed1a35/VAPOR+17+ELITE+AG-PRO+T.png",
            "shop_url":" https://www.nike.com/th/t/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%B1%E0%B9%8A%E0%B8%94%E0%B8%9F%E0%B8%B8%E0%B8%95%E0%B8%9A%E0%B8%AD%E0%B8%A5%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%AB%E0%B8%B8%E0%B9%89%E0%B8%A1%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%AA%E0%B8%99%E0%B8%B2%E0%B8%A1%E0%B8%AB%E0%B8%8D%E0%B9%89%E0%B8%B2%E0%B9%80%E0%B8%97%E0%B8%B5%E0%B8%A2%E0%B8%A1-nike-mercurial-vapor-17-elite-Ua924uFT/IM5806-900?dplnk=member&cp=94625298346_search_%7CTH%7CShopping%3A+TH+-+Standard+Shopping+-+Clearance%7CNike+Clearance+Products%7CGOOGLE&gclsrc=aw.ds&gad_source=1&gad_campaignid=21324068799&gbraid=0AAAAADLM_Zkw0i-A-ehWz0Sg04SeoUYOa&gclid=Cj0KCQiA77DXBhCHARIsAHf2MNpa3flszD9BmLBqld7_f6yPyVwbWAJJdBC_lcCK47tdY1F1ttSNz3UaAhtzEALw_wcB"
    },
    {
            "name": "F50 Hyperfast Elite Laceless",
            "category": "ฟุตบอล",
            "price": 9500,
            "description": "รองเท้าเหมาะสำหรับปีกข้าง",
            "image": "https://assets.adidas.com/images/h_2000,f_auto,q_auto,fl_lossy,c_fill,g_auto/6f344ea6ddaf46b0b1cf37fc01f56a79_9366/F50_Hyperfast_Elite_Laceless_Firm_Ground_Football_Boots_White_KJ6074_HM1.jpg",
            "shop_url":" https://www.adidas.co.th/en/f50-hyperfast-elite-laceless-firm-ground-football-boots/KJ6074.html"
    },
    {
        "name": "PREDATOR GOALKEEPER GLOVE PRO JUNIOR",
        "category": "ฟุตบอล",
        "price": 1680,
        "description": "ถุงมือสำหรับตำแหน่งประตู",
        "image": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcTb0cuFrNpWNYrKQyD3KDUEMGMg4w2N1LXToygc09SR5_rDNTz1sCK4JYh88YCfugySVEixAeHI8-asRfbbVsCqxagPZzSD1oPybEcgQe9AAZHYCmrAiFhBnA&usqp=CAc",
        "shop_url":" https://www.adidas.co.th/en/predator-goalkeeper-glove-pro-junior/KA7794.html"
     },
    {
        "name": "ถุงเท้า Adidas",
        "category": "ฟุตบอล",
        "price": 550,
        "description": "ถุงเท้าเหมาะสำหรับกีฬาฟุบอล ซับเหงื่อได้ดี",
        "image": "https://assets.adidas.com/images/h_2000,f_auto,q_auto,fl_lossy,c_fill,g_auto/daf506c739db49678dd21985cde12b69_9366/ADI26_JF0615_01_01_00_standard.jpg",
        "shop_url":" https://www.adidas.co.th/th/%E0%B8%96%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2-adi26/JF0615.html"
    },

    {
        "name": "ลูกบาสเกตบอล",
        "category": "บาสเกตบอล",
        "price": 1050,
        "description": "เหมาะสำหรับฝึกเลี้ยงบอลและยิงห่วง",
        "image": "https://www.supersports.co.th/cdn/shop/files/MO079SP811BYTH-0.jpg?v=1734402185&width=900",
        "shop_url":" https://www.supersports.co.th/collections/molten-basketball-equipment-accessories/products/molten-b7g3200-basketball-ball-mo079sp811byth-mol-bb-b7g3200"
    },
    {
        "name": "Ja 4 Heat Check EP",
        "category": "บาสเกตบอล",
        "price": 5300,
        "description": "รองรับการเคลื่อนไหวแบบเปลี่ยนทิศทางเร็วน้ำหนักเบา ตำแหน่งการ์ด",
        "image": "https://static.nike.com/a/images/t_web_pdp_535_v2/f_auto,u_9ddf04c7-2a9a-4d76-add1-d15af8f0263d,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/4882373b-e4c6-40ca-82f9-26d271611d53/JA+4+RADAR+EP.png",
        "shop_url":" https://www.nike.com/th/t/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%AA%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%95%E0%B8%9A%E0%B8%AD%E0%B8%A5-ja-4-heat-check-ep-Y9qNSD2f/JA9746-400"
    },
    {
        "name": "Adidas AE 1",
        "category": "บาสเกตบอล",
        "price": 4600,
        "description": "รองเท้าบาสที่รองรับแรงกระแทก ตำแหน่งฟอร์เวิร์ด ",
        "image": "https://assets.adidas.com/images/w_500,f_auto,q_auto/7767d203be8c429db677a59af703c150_9366/AE_1_The_Future_IF1858_01_standard.jpg",
        "shop_url":" https://www.adidas.co.th/th/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%AA%E0%B9%80%E0%B8%81%E0%B8%95%E0%B8%9A%E0%B8%AD%E0%B8%A5-ae-1-the-future/IF1858.html"
    },
    {
        "name": "Nike LeBron 21",
        "category": "บาสเกตบอล",
        "price": 3650,
        "description": "รองเท้าบาสที่มั่นคง ตำแหน่งเซ็นเตอร์ ",
        "image": "https://www.supersports.co.th/cdn/shop/files/NI083SH041DXTH-0.jpg?v=1738568496&width=900",
        "shop_url":" https://www.supersports.co.th/products/nike-lebron-xxi-ep-men-basketball-shoes-ni083sh041dxth-hf5352-400?tab=description"
    },
    {
            "name": "PUMA MB.05 Low",
            "category": "บาสเกตบอล",
            "price": 3920,
            "description": "รองเท้าบาสที่มั่นคง ซัพพอร์ตเท้าได้ดี ",
            "image": "https://images.puma.com/image/upload/f_auto,q_auto,b_rgb:fafafa,w_2000,h_2000/global/312753/01/sv03/fnd/THA/fmt/png/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%AA%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%95%E0%B8%9A%E0%B8%AD%E0%B8%A5-MB.05-Lo-Flourish-%E0%B8%A2%E0%B8%B9%E0%B8%99%E0%B8%B4%E0%B9%80%E0%B8%8B%E0%B9%87%E0%B8%81%E0%B8%8B%E0%B9%8C",
            "shop_url":" https://th.puma.com/th/th/pd/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%AA%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%95%E0%B8%9A%E0%B8%AD%E0%B8%A5-mb.05-lo-flourish-%E0%B8%A2%E0%B8%B9%E0%B8%99%E0%B8%B4%E0%B9%80%E0%B8%8B%E0%B9%87%E0%B8%81%E0%B8%8B%E0%B9%8C/312753.html?dwvar_312753_color=01"
    },
    {
            "name": "Nike A'Two Dawn Staley EP",
            "category": "บาสเกตบอล",
            "price": 3500,
            "description": "รองเท้าบาสที่มั่นคง ตำแหน่งเซ็นเตอร์ ",
            "image": "https://static.nike.com/a/images/t_web_pdp_535_v2/f_auto,u_9ddf04c7-2a9a-4d76-add1-d15af8f0263d,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/d9be402a-ffad-475e-9ddc-03cacfc9c90f/A%27TWO+DS+EP.png",
            "shop_url":" https://www.nike.com/th/t/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%AA%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%95%E0%B8%9A%E0%B8%AD%E0%B8%A5-aja-wilson-atwo-dawn-staley-ep-3NgNKd0q/IX1924-100"
    },
    {
        "name": "ZAMST EK-5",
        "category": "บาสเกตบอล",
        "price": 2100,
        "description": "สนับเข่า กันบาดเจ็บได้ดี ",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSH_mYIW3V9AUsEO3dMsL7jjEJMr8ePxyOfsQ2wo0ZfPnElt-YtApG8nvrF&s=10",
        "shop_url":" https://shopee.co.th/%E0%B8%8B%E0%B8%B1%E0%B8%9E%E0%B8%9E%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%95%E0%B9%80%E0%B8%82%E0%B9%88%E0%B8%B2-Zamst-EK-5-knee-support-%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%A3%E0%B8%B1%E0%B8%94%E0%B9%80%E0%B8%82%E0%B9%88%E0%B8%B2-%E0%B8%9E%E0%B8%A2%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%AD%E0%B9%87%E0%B8%99%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B9%80%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%A5%E0%B8%B9%E0%B8%81%E0%B8%AA%E0%B8%B0%E0%B8%9A%E0%B9%89%E0%B8%B2-%E0%B9%81%E0%B8%99%E0%B9%88%E0%B8%99%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B8%8A%E0%B8%B1%E0%B8%9A%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%AA%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%B1%E0%B8%94-i.158395044.3647851539"
    },
    {
        "name": "Jordan Elite",
        "category": "บาสเกตบอล",
        "price": 600,
        "description": "ถุงเท้า ลดแรงกระแทกได้ดี ซัพพอร์ตเท้า ",
        "image": "https://static.nike.com/a/images/t_web_pdp_535_v2/f_auto,u_126ab356-44d8-4a06-89b4-fcdcc8df0245,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/c11c9e91-8748-4af8-9c07-b0ac34cb9923/U+J+ELITE+CREW+1PR+-+144+JM.png",
        "shop_url":" https://www.nike.com/th/t/%E0%B8%96%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A2%E0%B8%B2%E0%B8%A7-jordan-elite-1-%E0%B8%84%E0%B8%B9%E0%B9%88-9Hih1ZmT/IO0494-100"
    },
    {
        "name": "Adidas Adizero Adios Pro 4",
        "category": "วิ่ง",
        "price": 5600,
        "description": "เหมาะสำหรับวิ่งออกกำลังกายและวิ่งระยะไกล",
        "image": "https://assets.adidas.com/images/h_2000,f_auto,q_auto,fl_lossy,c_fill,g_auto/7183483eb91740a49f44a5472bbc0585_9366/Adizero_Adios_Pro_4_JR6362_HM3_hover.jpg",
        "shop_url":" https://www.adidas.co.th/th/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2-adizero-adios-pro-4/JR6362.html"    
    },
    {
            "name": "Nike Maxfly 2",
            "category": "วิ่ง",
            "price": 3960,
            "description": "เน้นความเร็วและการออกตัวอย่างรวดเร็ว",
            "image": "https://static.nike.com/a/images/t_web_pdp_535_v2/f_auto,u_9ddf04c7-2a9a-4d76-add1-d15af8f0263d,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/ee06e43e-d1b6-4ba9-a5a1-26026518f6fa/AIR+ZOOM+MAXFLY+2.png",
            "shop_url":"https://www.nike.com/th/t/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%81%E0%B8%A3%E0%B8%B5%E0%B8%91%E0%B8%B2%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%95%E0%B8%B0%E0%B8%9B%E0%B8%B9%E0%B8%AA%E0%B8%9B%E0%B8%A3%E0%B8%B4%E0%B8%99%E0%B8%97%E0%B9%8C-nike-maxfly-2-dQxG4T/FD8395-800?dplnk=member&cp=94625298346_search_%7CTH%7CShopping%3A+TH+-+Standard+Shopping+-+Clearance%7CNike+Clearance+Products%7CGOOGLE&gclsrc=aw.ds&gad_source=1&gad_campaignid=21324068799&gbraid=0AAAAADLM_Zkw0i-A-ehWz0Sg04SeoUYOa&gclid=Cj0KCQiA77DXBhCHARIsAHf2MNrR8cJnbTHFl1yO2jRzueU8kAZlGl-U8eQ89flPTV-RijmJp3d1TiMaAsYSEALw_wcB "
     },
    {
            "name": "Adidas HOLO PEAK Shoes",
            "category": "วิ่ง",
            "price": 4800,
            "description": "เน้นการวิ่งบนเส้นทางธรรมชาติและพื้นผิวขรุขระ",
            "image": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSba3uDjCyn7dffu5Kj1O4r7GAWavw109vAIQ-dI4393adRNp3wK8LTuuAybg66HfdCVbZ-ujpCSs8wdI6oHU5R1Y-yTAZHYMYI-m1TO5Kzr9QEsCsFDW1g&usqp=CAc",
            "shop_url":" https://www.adidas.co.th/en/holo-peak-shoes/KI1520.html?cm_mmc=AdieSEM_Feeds-_-GoogleProductAds-_-SEA-_-id&cm_mmca1=TH&cm_mmca2&cm_mmc=adiSEM_EM_TH_SEA_PMax_NA_LF_AlwaysOn_GoogleAds_COM_AUT_AdidasCore_NOO_26000038_EN-_--_--_-dv:eCom&cm_mmc1=TH&cm_mmc2=&adicl_gclid=Cj0KCQiA77DXBhCHARIsAHf2MNofoN57bFWsXbHNeXS8YMU1oPy7Ej6MNx2PPMnwR65VJQXQudIo9_0aAofvEALw_wcB&gclsrc=aw.ds&gad_source=1&gad_campaignid=24307651838&gbraid=0AAAAAC0ynH10BaoxevGEFn1OIOFGBIIW_&gclid=Cj0KCQiA77DXBhCHARIsAHf2MNofoN57bFWsXbHNeXS8YMU1oPy7Ej6MNx2PPMnwR65VJQXQudIo9_0aAofvEALw_wcB"
    },
    {
                "name": "Adizero Boston 13",
                "category": "วิ่ง",
                "price": 5800,
                "description": "เน้นการวิ่งบนเส้นทางที่เรียบ",
                "image": "https://assets.adidas.com/images/h_2000,f_auto,q_auto,fl_lossy,c_fill,g_auto/1b826951503e46a19cd8431f95897df9_9366/Adizero_Boston_13_EQT_JR4791_01_00_standard.jpg",
                "shop_url":" https://www.adidas.co.th/th/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2-adizero-boston-13-eqt/JR4791.html"
    },
        {
                        "name": "Nike Vomero 18",
                        "category": "วิ่ง",
                        "price": 5500,
                        "description": "เป็นรองเท้าวิ่งสายซัพพอร์ต",
                        "image": "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco,u_9ddf04c7-2a9a-4d76-add1-d15af8f0263d,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/509a2393-b637-48ad-aad6-dbf56994bfdf/NIKE+VOMERO+18.png",
                         "shop_url":"https://www.nike.com/th/t/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%B4%E0%B9%88%E0%B8%87%E0%B9%82%E0%B8%A3%E0%B9%89%E0%B8%94%E0%B8%A3%E0%B8%B1%E0%B8%99%E0%B8%99%E0%B8%B4%E0%B9%88%E0%B8%87%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%8A%E0%B8%B2%E0%B8%A2-nike-vomero-18-snsbkH/HM6803-114"
         },
        {
                        "name": "ASICS Novablast 5",
                        "category": "วิ่ง",
                        "price": 3120,
                        "description": "เน้นการวิ่งlong run ",
                        "image": "https://www.supersports.co.th/cdn/shop/files/AS206SH989ETTH-0.jpg?v=1768551392&width=900",
                         "shop_url":" https://www.supersports.co.th/collections/supersports-brand-day-deal-asics/products/asics-running-road-as206sh989etth-1012b991-300?tab=description"
         },
    {
            "name": " Photochromic MH900",
            "category": "วิ่ง",
            "price": 1800,
            "description": "เหมาะสำหรับวิ่งออกกำลังกายและป้องกันแสงแดดเข้าตาถนอมตา",
            "image": "https://contents.mediadecathlon.com/p3190980/k$409a1662adbf2fe86b60c7d3f36939b1/photochromic-sports-sunglasses-cat-2-to-4-explore-900-mono-decathlon-8827754.jpg?f=768x0&format=auto",
            "shop_url":"https://www.decathlon.co.th/en-TH/p/photochromic-sports-sunglasses-cat-2-to-4-explore-900-mono-decathlon-8827754.html?gad_campaignid=24271769493&gad_source=1&gbraid=0AAAABCtIZZf45tdApKVN2kTywG3CiUUhI&gclid=Cj0KCQiA77DXBhCHARIsAHf2MNqG113xx0C04cPZgTiAwBvRAyKEr67Vgzc5de928lnb2X-3hfP8EzgaAuq4EALw_wcB"
        },
    {
            "name": "แว่น Oakley รุ่น RADAR EV PITCH OO9211-17",
            "category": "วิ่ง",
            "price": 3400,
            "description": "เหมาะสำหรับวิ่งออกกำลังกายและมีความทนทานป้องกันตา",
            "image": "https://siameyewear.com/wp-content/uploads/2026/04/OO9211_921117-1024x512.webp",
            "shop_url":" https://siameyewear.com/%e0%b9%81%e0%b8%a7%e0%b9%88%e0%b8%99%e0%b8%81%e0%b8%b1%e0%b8%99%e0%b9%81%e0%b8%94%e0%b8%94-oakley-oo9211-17/"
        },
        
   {
               "name": "Deviate Pure NITRO",
               "category": "วิ่ง",
               "price": 5400,
               "description": "ออกแบบมาให้วิ่งสนุกและคล่องตัว ",
               "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuh2Xw3zrQM4mrHdXF2-DABgjaz1zok_2SWAF7KiiE5w&s=10",
               "shop_url":"https://th.puma.com/th/th/pd/%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%97%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%B4%E0%B9%88%E0%B8%87-deviate-pure-nitro%E2%84%A2-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%8A%E0%B8%B2%E0%B8%A2/4070033073773.html?gad_source=1&gad_campaignid=24043517265&gbraid=0AAAAAC8EoW8zrOylARtx0LBanxNauzfHA&gclid=Cj0KCQiA77DXBhCHARIsAHf2MNq8yGXgZXwLLLIPViWp06uDTeFN_x5zEPKxJWJAaYYY1sFFA7Ks4AEaAnYQEALw_wcB"
           },
     {
                "name": "HUAWEI WATCH FIT 5 Series ",
                "category": "วิ่ง",
                "price": 4690,
                "description": "เหมาะสำหรับวิ่งออกกำลังกายและใช้ได้หลายฟังชั่น",
                "image": "https://img01.huaweifile.com/sg/ms/th/pms/uomcdn/TH_HW_B2C/pms/202604/gbom/6942103190896/800_800_3F24283D1597EB81548D78B66D9343ABmp.webp",
                "shop_url":"https://consumer.huawei.com/th/offer/categories/wearable/watch-fit5-buy/?skuCode=80660114010017205"
        },
    {
        "name": "Forerunner 165",
        "category": "วิ่ง",
        "price": 5990,
        "description": "ใช้ติดตามเวลาและระยะทางในการวิ่ง",
        "image": "https://bananarun.com/media/catalog/product/0/1/010-02970-50_forerunner_570_-_42mm_slate_gray_aluminum_1_.jpg?w=800&q=80",
        "shop_url":" https://www.garmin.com/th-TH/p/1055469/pn/010-02863-A0/?utm_source=google&utm_campaign=pmax_shoppingads&utm_medium=pmax&gad_source=1&gad_campaignid=18170345206&gbraid=0AAAAADnByCIT5T5OaDnY4DajNdN2MyxPu&gclid=Cj0KCQiA77DXBhCHARIsAHf2MNoBKNhmao9YusQUHu_L2zn6IUR7eSua0VFo0YMfxjLXCRWNKqrhyLsaAvU5EALw_wcB"
    }
]
styles = [
    {
        "sport": "ฟุตบอล",
        "name": "กองหน้า",
        "description": "เน้นความเร็ว การยิงประตู และการเคลื่อนที่เข้าหาบอล",
        "equipment": "รองเท้าสตั๊ดน้ำหนักเบา และถุงเท้ากีฬา",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0IcWiI0DuIm8-3hSGXSe5OTv6xZDZ6MrEi_lJL1Nd-w&s=10"
    },
    {
        "sport": "ฟุตบอล",
        "name": "กองกลาง",
        "description": "เน้นการควบคุมบอล การส่งบอล และการวิ่งตลอดเกม",
        "equipment": "รองเท้าสตั๊ดที่กระชับ และสนับแข้ง",
        "image": "https://assets.adidas.com/images/w_500,f_auto,q_auto/73ad11be965946229d2c8bc85ec05c74_9366/Predator_League_Fold-Over_Tongue_Firm_Ground_JP6278_HM1.jpg"
    },
    {
        "sport": "ฟุตบอล",
        "name": "กองหลัง",
        "description": "เน้นการป้องกัน การเข้าสกัด และการทรงตัว",
        "equipment": "รองเท้าสตั๊ดที่ยึดเกาะสนามดี และสนับแข้ง",
        "image": "https://www.supersports.co.th/cdn/shop/files/NI083SH002EKTH-0.jpg?v=1743764697&width=900"
    },
    {
        "sport": "บาสเกตบอล",
        "name": "การ์ด (Guard)",
        "description": "เน้นความเร็ว การเลี้ยงบอล และการเปลี่ยนทิศทาง",
        "equipment": "รองเท้าบาสน้ำหนักเบา ",
        "image": "https://static.nike.com/a/images/t_web_pdp_535_v2/f_auto,u_9ddf04c7-2a9a-4d76-add1-d15af8f0263d,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/4882373b-e4c6-40ca-82f9-26d271611d53/JA+4+RADAR+EP.png"
    },
    {
        "sport": "บาสเกตบอล",
        "name": "ฟอร์เวิร์ด (Forward)",
        "description": "เน้นการกระโดด การทำคะแนน และการเล่นรอบวง",
        "equipment": "รองเท้าบาสที่รองรับแรงกระแทก ",
        "image": "https://assets.adidas.com/images/w_500,f_auto,q_auto/7767d203be8c429db677a59af703c150_9366/AE_1_The_Future_IF1858_01_standard.jpg"
    },
    {
        "sport": "บาสเกตบอล",
        "name": "เซ็นเตอร์ (Center)",
        "description": "เน้นการรีบาวด์ การป้องกันใต้แป้น และการปะทะ",
        "equipment": "รองเท้าบาสที่มั่นคง และอุปกรณ์ป้องกันข้อเข่า",
        "image": "https://www.supersports.co.th/cdn/shop/files/NI083SH041DXTH-0.jpg?v=1738568496&width=900"
    },
    {
        "sport": "วิ่งระยะสั้น",
        "name": "Nike Maxfly 2",
        "description": "เน้นความเร็วและการออกตัวอย่างรวดเร็ว",
        "equipment": "รองเท้าสำหรับวิ่งระยะสั้นหรือรองเท้าตะปูตามสนาม",
        "image": "https://static.nike.com/a/images/t_web_pdp_535_v2/f_auto,u_9ddf04c7-2a9a-4d76-add1-d15af8f0263d,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/ee06e43e-d1b6-4ba9-a5a1-26026518f6fa/AIR+ZOOM+MAXFLY+2.png"
    },
    {
        "sport": "วิ่งระยะไกล",
        "name": "Adidas Adizero Adios Pro 4",
        "description": "เน้นความทนทานและความสบายในการวิ่งต่อเนื่อง",
        "equipment": "รองเท้าวิ่งที่รองรับแรงกระแทก ",
        "image": "https://assets.adidas.com/images/h_2000,f_auto,q_auto,fl_lossy,c_fill,g_auto/7183483eb91740a49f44a5472bbc0585_9366/Adizero_Adios_Pro_4_JR6362_HM3_hover.jpg"
    },
    {
        "sport": "วิ่งเทรล",
        "name": "Adidas HOLO PEAK Shoes",
        "description": "เน้นการวิ่งบนเส้นทางธรรมชาติและพื้นผิวขรุขระ",
        "equipment": "รองเท้าวิ่งเทรลที่มีดอกยางยึดเกาะดี ",
        "image": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSba3uDjCyn7dffu5Kj1O4r7GAWavw109vAIQ-dI4393adRNp3wK8LTuuAybg66HfdCVbZ-ujpCSs8wdI6oHU5R1Y-yTAZHYMYI-m1TO5Kzr9QEsCsFDW1g&usqp=CAc"
    }
]


@app.route("/")
def home():
    category = request.args.get("category", "ทั้งหมด")

    # กำหนดสินค้าเริ่มต้นก่อน
    shown_products = products

    # กรองสินค้าตามหมวดหมู่
    if category != "ทั้งหมด":
        shown_products = [
            p for p in products
            if p["category"] == category
        ]
    # รับค่าราคาจากหน้าเว็บ
    min_price = request.args.get("min_price", 100, type=int)
    max_price = request.args.get("max_price", 10000, type=int)

# ป้องกันการใส่ราคาผิด
    min_price = max(100, min(min_price, 10000))
    max_price = max(100, min(max_price, 10000))

    # กรองสินค้าตามหมวดหมู่
    shown_products = [
        p for p in products
        if category == "ทั้งหมด" or p["category"] == category
    ]

    # กรองสินค้าตามราคา
    shown_products = [
        p for p in shown_products
        if min_price <= p["price"] <= max_price
    ]

    # ส่งข้อมูลไปยังหน้าเว็บ
    return render_template(
        "index.html",
        products=shown_products,
        category=category,
        styles=styles,
        min_price=min_price,
        max_price=max_price
    )


if __name__ == "__main__":
    app.run(debug=True)