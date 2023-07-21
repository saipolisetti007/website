products_list = {
        1: {
            "name": "Televisions",
            "img": "Tv.jpg",
            "title": "Microsoft Surface Laptop 4 AMD Ryzen 5 4680U 13.5 inches Touchscreen Laptop"
        },
        2: {
            "name": "Laptops",
            "img": "Laptop.jpg",
            "title": "HP Pavilion Laptop 14-dv2014TU SCREEN SIZE 35.6 cm (14) COLOUR Natural silver"
        },
        3: {
            "name": "Mobiles",
            "img": "Iphone.jpg",
            "title": "15 cm (6.1-inch) Super Retina XDR display with ProMotion for a faster, more responsive feel"
        },
        4: {
            "name": "Headsets",
            "img": "Headset.jpg",
            "title": "Razer BlackShark V2 Pro Wireless THX White Gaming Headset"
        },
        5: {
            "name": "Camera",
            "img": "Camera.jpg",
            "title": "Canon M50 Mark II 15-45mm f3.5-6.3 is STM"
        },
        6: {
            "name": "Bicycle",
            "img": "Cycles.jpg",
            "title": "Original Factory 20 21 22 24 26 29 Inch Cheap Freestyle Street BMX Bycycle Bisicletas Bike for Adults"
        }
        
        
    }
  
empty_cart={}
for key,value in products_list.items():
    empty_cart[key]={
        'name':value['name']
        ,
        'quantity':0
    }
