import random
import webbrowser

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

#Enterable Dictionaies
City = {'Goleta','Isla Vista','Santa Barbara'}
Price = {'$','$$','$$$'}

#List Dictionaries
IV_list = {
    "American": ['Buddha Bowls','Rockfire Grill','Habit','IV Deli','Deja Vu',"Sam's To Go",'Subway',"Kyle's",'Romaine','Root 217'],
    "Mexican": ['Freebirds',"Super Cuca's",'Rosarito','Tacos and Taproom',"Wahoo's"],
    "Asian": ['Panda Express','Poke Theory','Naan Stop',"Su's Bowl",'Hana Kitchen','PokeCeviche','Sizzling Lunch','Mojo Asian Fusion','Pho Bistro','Kaiju','Sushiya Express','Lao Wang'],
    "Italian": ["Woodstock's","Domino's",'Pizza My Heart'],
    "Greek": ['Santorini Island Grill']}
Buddha = 'https://www.yelp.com/biz/buddha-bowls-isla-vista'
Rockfire = 'https://www.yelp.com/biz/rockfire-grill-goleta-5'
Habit = 'https://www.yelp.com/biz/the-habit-isla-vista?osq=habit'
IV_Deli = 'https://www.yelp.com/biz/iv-deli-mart-goleta?osq=iv+deli'
Deja_Vu = 'https://www.yelp.com/biz/deja-vu-cafe-iv-goleta?osq=deja+vu'
Sams = 'https://www.yelp.com/biz/sams-to-go-isla-vista-isla-vista?osq=sams'
Subway = 'https://www.yelp.com/biz/subway-isla-vista-2?osq=subway'
Kyles = 'https://www.yelp.com/biz/kyles-isla-vista-isla-vista-2?osq=kyles'
Romaine = 'https://www.yelp.com/biz/romaines-goleta?osq=romaine'
Root_217 = 'https://www.yelp.com/biz/root-217-goleta?osq=root'
Freebirds = 'https://www.yelp.com/biz/freebirds-isla-vista?osq=freebirds'
Super_Cuca = 'https://www.yelp.com/biz/super-cucas-isla-vista?osq=super'
Rosarito = 'https://www.yelp.com/biz/rosarito-isla-vista?osq=rosarito'
Tacos_Taproom = 'https://www.yelp.com/biz/california-tacos-and-taproom-isla-vista?osq=tacos+and+taproom'
Wahoos = 'https://www.yelp.com/biz/wahoos-fish-tacos-isla-vista?osq=wahoos'
Panda = 'https://www.yelp.com/biz/panda-express-santa-barbara-8?osq=panda'
Poke_Theory = 'https://www.yelp.com/biz/poke-theory-sb-goleta-3?osq=poke'
PokeCeviche = 'https://www.yelp.com/biz/pokeceviche-goleta-2?osq=poke'
NaanStop = 'https://www.yelp.com/biz/naan-stop-isla-vista?osq=naan'
Sus_Bowls = 'https://www.yelp.com/biz/su-s-bowl-isla-vista?osq=sus'
Hana = 'https://www.yelp.com/biz/hana-kitchen-santa-barbara?osq=hana'
Sizzling = 'https://www.yelp.com/biz/sizzling-lunch-goleta?osq=sizzling'
Mojo = 'https://www.yelp.com/biz/mojo-asian-fusion-caf%C3%A9-isla-vista-2?osq=mojo'
Pho_Bistro = 'https://www.yelp.com/biz/pho-bistro-isla-vista'
Kaiju = 'https://www.yelp.com/biz/kaiju-isla-vista?osq=kaiju'
Sushiya = 'https://www.yelp.com/biz/sushiya-express-goleta-2?osq=sushiya'
Lao_Wang = 'https://www.yelp.com/biz/lao-wang-goleta?osq=lao+wang'
Woodstocks = 'https://www.yelp.com/biz/woodstocks-pizza-isla-vista-2?osq=woodstoclk'
Dominos = 'https://www.yelp.com/biz/dominos-pizza-santa-barbara?osq=dominos'
Pizza_My_Heart = 'https://www.yelp.com/biz/pizza-my-heart-isla-vista?osq=pizza+my+heart'
Santorini = 'https://www.yelp.com/biz/santorini-greek-island-grill-isla-vista-2?osq=santorini'




IV_breakfast = {
    "B": ['Bagel Cafe','Deja Vu','Spudnuts','Caje','Root 217']}
Bagel = 'https://www.yelp.com/biz/bagel-cafe-goleta'
Spudnuts = 'https://www.yelp.com/biz/spudnuts-donuts-isla-vista'
Caje = 'https://www.yelp.com/biz/caj%C3%A9-coffee-roasters-isla-vista-isla-vista'


    
Goleta_cheap = {
    "American": ["Kyle's Kitchen",'Sandpiper Grill','Three Pickles','Natural Cafe','Costco',"Dave's Dogs Grill",'In N Out','Home Plate Grill','Goleta Coffee Co','Santa Barbara Chicken Ranch',"Wendy's","McDonald's","Carl's Jr.",'IHOP',"Jersey Mike's",'Jack In The Box','KFC'],
    "Mexican": ["Altamirano's",'Del Valle Grill','La Tapatia','Chipotle','Taco Bell','Cal Taco',"Lilly's Taquiera","Pollofino's",'La Guerrerita','El Sitio','Del Pueblo'],
    "Asian": ['Noodle City','Saigon Noodle House','Phamous Cafe','L&L Hawaiian BBQ'],
    "Italian": ["Little Ceasdar's"]}

Kyles_Kitchen = 'https://www.yelp.com/biz/kyles-kitchen-goleta?osq=kyle'
Sandpiper = 'https://www.yelp.com/biz/sandpiper-grill-goleta?osq=sandpiper'
Three_Pickles = 'https://www.yelp.com/biz/three-pickles-goleta?osq=three+pickles'
Natural_Cafe = 'https://www.yelp.com/biz/natural-cafe-goleta?osq=natural+cafe'
Costco = 'https://www.yelp.com/biz/costco-goleta?osq=costco'
Daves = 'https://www.yelp.com/biz/daves-dogs-grill-santa-barbara?osq=daves'
In_N_Out = 'https://www.yelp.com/biz/in-n-out-burger-goleta?osq=in+n+out'
Home_Plate_Grill = 'https://www.yelp.com/biz/home-plate-grill-goleta-2?osq=home+plate'
Goleta_Coffee = 'https://www.yelp.com/biz/goleta-coffee-co-and-loca-vivant-kitchen-santa-barbara?osq=goleta+coffee'
SB_Chicken = 'https://www.yelp.com/biz/santa-barbara-chicken-ranch-goleta'
Wendys = 'https://www.yelp.com/biz/wendys-goleta?osq=wendys'
Mcdonalds = 'https://www.yelp.com/biz/mcdonalds-goleta-3?osq=mcdonalds'
Carls = 'https://www.yelp.com/biz/carls-jr-goleta?osq=carls'
IHOP = 'https://www.yelp.com/biz/ihop-santa-barbara-3?osq=ihop'
Jersey_Mikes = 'https://www.yelp.com/biz/jersey-mikes-subs-goleta-3?osq=jersey+mikes'
Jack_in_the_Box = 'https://www.yelp.com/biz/jack-in-the-box-goleta?osq=jack+in+the+box'
KFC = 'https://www.yelp.com/biz/kfc-goleta?osq=kfc'
Altamiranos = 'https://www.yelp.com/biz/altamiranos-mexican-grill-goleta'
Del_Valle_Grill = 'https://www.yelp.com/biz/del-valle-grill-goleta'
La_Tapatia = 'https://www.yelp.com/biz/la-tapatia-goleta'
Chipotle = 'https://www.yelp.com/biz/chipotle-mexican-grill-goleta?osq=chipotle'
Taco_Bell = 'https://www.yelp.com/biz/taco-bell-goleta'
Cal_Taco = 'https://www.yelp.com/biz/cal-taco-goleta?osq=cal+taco'
Lillys_Taquiera = 'https://www.yelp.com/biz/lillys-tacos-goleta'
Pollofinos = 'https://www.yelp.com/biz/pollofino-goleta-2?osq=pollofino'
La_Guerrerita = 'https://www.yelp.com/biz/la-guerrerita-mexican-food-goleta'
El_Sitio = 'https://www.yelp.com/biz/el-sitio-goleta'
Del_Pueblo = 'https://www.yelp.com/biz/del-pueblo-cafe-santa-barbara?osq=del+pueblo'
Noodle_City = 'https://www.yelp.com/biz/noodle-city-goleta?osq=noodle+city'
Saigon_Noodle_House = 'https://www.yelp.com/biz/saigon-noodle-house-goleta'
Phamous_Cafe = 'https://www.yelp.com/biz/phamous-cafe-goleta'
LL = 'https://www.yelp.com/biz/l-and-l-hawaiian-barbeque-goleta'
Little_Ceasar = 'https://www.yelp.com/biz/little-caesars-goleta-2'



Goleta_breakfast = {
    "B": ['IHOP','Cajun Kitchen',"Domingo's Cafe","Jeannine's",'Outpost','Home Plate Grill','On the Alley','Flir Cafe','Goodland Dining','La Guerrerita',"Cody's Cafe"]}

Cajun_Kitchen = 'https://www.yelp.com/biz/cajun-kitchen-cafe-goleta?osq=cajun+kitchen'
Domingos_Cafe = 'https://www.yelp.com/biz/domingos-cafe-goleta?osq=domingos'
Jeannines = 'https://www.yelp.com/biz/jeannines-american-bakery-restaurant-goleta'
Outpost = 'https://www.yelp.com/biz/outpost-goleta?osq=outpost'
On_The_Alley = 'https://www.yelp.com/biz/on-the-alley-goleta-goleta-2?osq=on+the+alley'
Flir_Cafe = 'https://www.yelp.com/biz/flir-cafe-goleta'
Goodland_Dining = 'https://www.yelp.com/biz/goodland-dining-goleta'
Codys_Cafe = 'https://www.yelp.com/biz/codys-cafe-santa-barbara'

Goleta_list = {
    "American": ['Frog Bar and Grill','Panino','Pickles & Swiss',"Woody's BBQ","Chili's",'The Nugget Bar and Grill','Mesa Burger','On the Alley','Hollister Brewing','Jane at the Marketplace','Outpost','Rooftop Bistro & Bar','Nikka Fish Market'],
    "Asian": ['Uniboil','Pattaya Thai','Itsuki','Sushiya Express','Nikka Ramen','China King','Meun Fan Thai Cafe','Masala Spice','Choppa Poke','Goleta Sushi House','Red Pepper','Choi Oriental Market'],
    "Italian": ["Ca'Dario","Rusty's Pizza"],
    "Mexican": ['Los Agaves','La Hacienda','Los Arroyos',"Pepe's",'Costa Terraza']}

Frog_Bar_And_Grill = 'https://www.yelp.com/biz/frog-bar-and-grill-santa-barbara'
Panino = 'https://www.yelp.com/biz/panino-goleta'
Pickles_Swiss = 'https://www.yelp.com/biz/pickles-and-swiss-goleta?osq=Pickles+%26+Swiss'
Woodys_BBQ = 'https://www.yelp.com/biz/woodys-bbq-santa-barbara'
Chilis = 'https://www.yelp.com/biz/chilis-goleta-2'
Nugget_Bar_And_Grill = 'https://www.yelp.com/biz/the-nugget-bar-and-grill-goleta-2'
Mesa_Burger = 'https://www.yelp.com/biz/mesa-burger-goleta-goleta'
Hollister_Brewing = 'https://www.yelp.com/biz/hollister-brewing-company-goleta'
Jane = 'https://www.yelp.com/biz/jane-at-the-marketplace-goleta'
Rooftop_Bistro_Bar = 'https://www.yelp.com/biz/roof-top-bistro-and-bar-goleta-2?osq=rooftop+bistro'
Nikka_Fish_Market = 'https://www.yelp.com/biz/nikka-fish-market-and-grill-goleta'
Uniboil = 'https://www.yelp.com/biz/uniboil-goleta'
Pattaya_Thai = 'https://www.yelp.com/biz/pattaya-thai-restaurant-goleta'
Itsuki = 'https://www.yelp.com/biz/itsuki-goleta'
Sushiya_Express = 'https://www.yelp.com/biz/sushiya-express-goleta-2'
Nikka_Ramen = 'https://www.yelp.com/biz/nikka-ramen-goleta-2'
China_King = 'https://www.yelp.com/biz/china-king-goleta'
Meun_Fan_Thai_Cafe = 'https://www.yelp.com/biz/meun-fan-thai-cafe-goleta'
Masala_Spice = 'https://www.yelp.com/biz/masala-spice-indian-cuisine-goleta'
Choppa_Poke = 'https://www.yelp.com/biz/choppa-poke-goleta'
Goleta_Sushi_House = 'https://www.yelp.com/biz/goleta-sushi-house-goleta'
Red_Pepper = 'https://www.yelp.com/biz/red-pepper-restaurant-goleta'
Choi_Oriental_Market = 'https://www.yelp.com/biz/chois-oriental-market-santa-barbara'
CaDario = 'https://www.yelp.com/biz/ca-dario-goleta-goleta'
Rustys_Pizza = 'https://www.yelp.com/biz/rustys-pizza-parlor-goleta-2'
Los_Agaves = 'https://www.yelp.com/biz/los-agaves-goleta-3'
La_Hacienda = 'https://www.yelp.com/biz/la-hacienda-mexican-restaurant-goleta'
Los_Arroyos = 'https://www.yelp.com/biz/los-arroyos-mexican-restaurant-and-take-out-goleta-2'
Pepes = 'https://www.yelp.com/biz/pepes-mexican-restaurant-goleta'
Costa_Terraza = 'https://www.yelp.com/biz/costa-terraza-santa-barbara'


Goleta_expensive = {
    "American": ['Angel Oak at Bacara'],
    "Italian": ['The Bistro']}
Angel_Oak = 'https://www.yelp.com/biz/angel-oak-at-bacara-santa-barbara-2?osq=angel+oak'
The_Bistro = 'https://www.yelp.com/biz/the-bistro-santa-barbara'

SB_breakfast = {
    "B": ['Char West',"Lito's",'Breakwater Restaurant','Shoreline Beach Cafe','The Shop Kitchen','Mesa Cafe','Farmer Boy',"Denny's",'Boathouse','Dawn Patrol',"Bree'osh",'Finch & Fork',"Chad's",'Scarlett Begonia','SB Sunshine Cafe','Helena Ave Bakery',"Garrett's Old Fashioned","Andersen's Danish Bakery",'State & Fig',"JJ's Diner",'Yellow Belly','Live Oak Cafe','4 Eggs & Pizza',"Jack's Bistro","Mulligan's Cafe & Bar",'La Paloma']}
Char_West = 'https://www.yelp.com/biz/char-west-santa-barbara'
Breakwater_Restaurant = 'https://www.yelp.com/biz/breakwater-restaurant-santa-barbara'
Shoreline_Beach_Cafe = 'https://www.yelp.com/biz/shoreline-beach-cafe-santa-barbara-2'
The_Shop_Kitchen = 'https://www.yelp.com/biz/the-shop-kitchen-santa-barbara'
Mesa_Cafe = 'https://www.yelp.com/biz/mesa-cafe-santa-barbara'
Farmer_Boy = 'https://www.yelp.com/biz/farmer-boy-santa-barbara-2'
Denny = 'https://www.yelp.com/biz/dennys-santa-barbara'
Boathouse = 'https://www.yelp.com/biz/boathouse-at-hendrys-beach-santa-barbara'
Dawn_Patrol = 'https://www.yelp.com/biz/dawn-patrol-santa-barbara'
Breeosh = 'https://www.yelp.com/biz/breeosh-santa-barbara'
Finch_Fork = 'https://www.yelp.com/biz/finch-and-fork-santa-barbara'
Chads = 'https://www.yelp.com/biz/chads-santa-barbara-2'
Scarlett_Begonia = 'https://www.yelp.com/biz/scarlett-begonia-santa-barbara'
SB_Sunshine_Cafe = 'https://www.yelp.com/biz/sb-sunshine-cafe-santa-barbara'
Helena_Ave_Bakery = 'https://www.yelp.com/biz/helena-avenue-bakery-santa-barbara'
Garretts = 'https://www.yelp.com/biz/garretts-old-fashioned-restaurant-santa-barbara-2'
Andersens = 'https://www.yelp.com/biz/andersens-danish-bakery-and-restaurant-santa-barbara'
State_And_Fig = 'https://www.yelp.com/biz/state-and-fig-santa-barbara'
JJs_Diner = 'https://www.yelp.com/biz/jj-s-diner-santa-barbara'
Yellow_Belly = 'https://www.yelp.com/biz/yellow-belly-santa-barbara'
Live_Oak_Cafe = 'https://www.yelp.com/biz/live-oak-cafe-santa-barbara'
Four_Eggs_Pizza = 'https://www.yelp.com/biz/4-eggs-and-pizza-santa-barbara'
Jacks_Bistro = 'https://www.yelp.com/biz/jacks-bistro-and-famous-bagels-santa-barbara-2'
Mulligans = 'https://www.yelp.com/biz/mulligans-cafe-and-bar-santa-barbara'
La_Paloma = 'https://www.yelp.com/biz/la-paloma-cafe-santa-barbara'
Litos = 'https://www.yelp.com/biz/litos-take-out-santa-barbara'

SB_cheap = {
    "Mexican": ['El Pollo Loco','Burger Express','Milpas Taqueria',"Mayo's Carniceria",'Su Casa','Taqueria Rincon','El Zarape',"Rudy's",'Taqueria el Buen Gusto',"Mony's Mexican Food","Rudy's Restaurant",'Taqueria el Bajio','Tacos Pipeye','La-Super-Rica','Buena Onda'],
    "American": ['Mels',"Jack's Bistro",'Chubbies Hamburgers','South Coast Deli','Plaza Deli','Chick-fil-A'],
    "Italian": ["Gino's Sicilian Express","Nona's Italian Deli"],
    "Enlgish": ['The Press Room']}
El_Pollo_Loco = 'https://www.yelp.com/biz/el-pollo-loco-santa-barbara-2'
Burger_Express = 'https://www.yelp.com/biz/burger-express-santa-barbara'
Milpas_Taqueria = 'https://www.yelp.com/biz/milpas-taqueria-santa-barbara-2'
Mayos_Carniceria = 'https://www.yelp.com/biz/mayos-carniceria-and-tacos-santa-barbara'
Su_Casa = 'https://www.yelp.com/biz/su-casa-fresh-mexican-grill-santa-barbara'
Taqueria_Rincon = 'https://www.yelp.com/biz/taqueria-rincon-alteno-santa-barbara'
El_Zarape = 'https://www.yelp.com/biz/el-zarape-santa-barbara'
Rudys = 'https://www.yelp.com/biz/rudys-santa-barbara?osq=rudys'
Taqueria_el_Buen_Gusto = 'https://www.yelp.com/biz/taqueria-el-buen-gusto-santa-barbara'
Monys_Mexican_Food = 'https://www.yelp.com/biz/monys-mexican-food-santa-barbara'
Rudys_Restaurant = 'https://www.yelp.com/biz/rudys-restaurant-no-1-santa-barbara'
Taqueria_El_Bajio = 'https://www.yelp.com/biz/taqueria-el-bajio-santa-barbara'
Tacos_Pipeye = 'https://www.yelp.com/biz/tacos-pipeye-santa-barbara-2'
La_Super_Rica = 'https://www.yelp.com/biz/la-super-rica-taqueria-santa-barbara'
Buena_Onda = 'https://www.yelp.com/biz/buena-onda-santa-barbara-4'
Mels = 'https://www.yelp.com/biz/mels-santa-barbara'
Chubbies_Hamburgers = 'https://www.yelp.com/biz/chubbies-hamburgers-santa-barbara'
South_Coast_Deli = 'https://www.yelp.com/biz/south-coast-deli-carrillo-santa-barbara'
Plaza_Deli = 'https://www.yelp.com/biz/plaza-deli-santa-barbara'
Chick_Fil_A = 'https://www.yelp.com/biz/chick-fil-a-santa-barbara'
Ginos_Sicilian_Express = 'https://www.yelp.com/biz/ginos-sicilian-express-santa-barbara-2'
Nonas_Italian_Deli = 'https://www.yelp.com/biz/nonas-italian-deli-santa-barbara-2'
The_Press_Room = 'https://www.yelp.com/biz/the-press-room-santa-barbara'

SB_list = {
    "American": ['Char West',"Joe's Cafe",'Uptown Bar & Lounge',"Derf's Cafe",'Breakwater Restaurant','The Waterline',"Island's","Longboard's Grill",'Eureka!','SB Munchiez','Shoreline Beach Cafe','Nook',"Jill's Place",'Seven Bar & Kitchen','Little Kitchen',"Shalhoob's Funk Zone Patio",'Farmer Boy','Scarlett Begonia',"Bossie's Kitchen",'Padaro Beach Grill','Dawn Patrol','The Palace Grill','Finch & Fork','The Black Sheep',"Finney's Crafthouse"],
    "Mexican": ['Los Altos','El Paseo',"Carlito's Cafe Y Cantina",'La Playa Azul Cafe','Rosales Mexican Restaurant','Cava Restaurant & Bar','Los Agaves','Corazon Cocina','East Beach Tacos','Santo Mezcal','Taqueria Cuernavaca'],
    "Mediterranean": ['Luna Grill','Mesa Verde','Zaytoon'],
    "Italian": ['California Pizza Kitchen','Uncle Roccos Famous NY Pizza','Mesa Pizza',"Petrini's Italian",'Persona Pizzeria',"Patxi's Pizza","Arnoldi's Cafe",'Crocodile Restaurant & Bar','Presto Pasta','Pascucci','Olio Pizzeria','Trattoria Vittoria',"OPPI'Z Bistro",'Convivo Restaurant and Bar',"Mollie's",'Bettina','Mizza'],
    "Seafood": ['Moby Dick','Kanaloa Seafood','The Harbor Restaurant','The Drunken Crab','Santa Barbara Fish House',"Teddy's By The Sea",'Bluewater Grill','Brophy Bros','Lure Fish House','Boathouse','Opal Restaurant and Bar','Santa Barbara Shellfish Company'],
    "Asian": ['Galanga Thai Restaurant','Shintori Sushi Factory','Ichiban','Kyoto','Sushi GoGo','TAP Thai Cuisine','Mandarin Palace','Zen Yai Thai','Phoevermore','Sachi Ramen','Your Place Thai','Shang Hai','Wabi Sabi','Sun Sushi','Sushi Bar 29','Saigon Vietnamese Restaurant','Kimchi Korean BBQ','Meet Up Chinese Cuisine','Sama Sama Kitchen','Empty Bowl Noodle Bar','Santa Barbara Craft Ramen'],
    "Caribbean": ['Embermill','Cubaneo'],
    "Brazilian": ['Brasil Arts Cafe'],
    "French": ['Petit Valentien'],
    "Indian": ['Apna Indian Kitchen','Himalayan Kitchen','Flavor of India'],
    "Danish": ["Andersen's Bakery & Restaurant"]}
Joes_Cafe = 'https://www.yelp.com/biz/joes-cafe-santa-barbara'
Uptown_Bar_Lounge = 'https://www.yelp.com/biz/uptown-bar-and-lounge-santa-barbara'
Derfs_Cafe = 'https://www.yelp.com/biz/derfs-cafe-santa-barbara-3'
The_Waterline = 'https://www.yelp.com/biz/the-waterline-santa-barbara'
Islands = 'https://www.yelp.com/biz/islands-restaurant-santa-barbara-2'
Longboards_Grill = 'https://www.yelp.com/biz/longboards-grill-santa-barbara'
Eureka = 'https://www.yelp.com/biz/eureka-santa-barbara-3'
SB_Munchiez = 'https://www.yelp.com/biz/sb-munchiez-santa-barbara-5'
Nook = 'https://www.yelp.com/biz/nook-santa-barbara-2'
Jills_Place = 'https://www.yelp.com/biz/jills-place-santa-barbara-2'
Seven_Bar_and_Kitchen = 'https://www.yelp.com/biz/seven-bar-and-kitchen-santa-barbara'
Little_Kitchen = 'https://www.yelp.com/biz/little-kitchen-santa-barbara'
Shalhoobs_Funk_Zone_Patio = 'https://www.yelp.com/biz/shalhoobs-funk-zone-patio-santa-barbara-4'
Bossies_Kitchen = 'https://www.yelp.com/biz/bossies-kitchen-santa-barbara'
Padaro_Beach_Grill = 'https://www.yelp.com/biz/padaro-beach-grill-carpinteria'
The_Palace_Grill = 'https://www.yelp.com/biz/the-palace-grill-santa-barbara'
The_Black_Sheep = 'https://www.yelp.com/biz/the-black-sheep-santa-barbara-2'
Finneys_Crafthouse = 'https://www.yelp.com/biz/finneys-crafthouse-santa-barbara'
Los_Altos = 'https://www.yelp.com/biz/los-altos-restaurant-santa-barbara'
El_Paseo = 'https://www.yelp.com/biz/el-paseo-mexican-restaurant-santa-barbara'
Carlitos = 'https://www.yelp.com/biz/carlitos-cafe-y-cantina-santa-barbara'
La_Playa_Azul_Cafe = 'https://www.yelp.com/biz/la-playa-azul-cafe-santa-barbara'
Rosales_Mexican_Restaurant = 'https://www.yelp.com/biz/rosales-mexican-restaurant-santa-barbara'
Cava_Restaurant_Bar = 'https://www.yelp.com/biz/cava-restaurant-and-bar-montecito'
Corazon_Cocina = 'https://www.yelp.com/biz/corazon-cocina-santa-barbara-2'
East_Beach_Tacos = 'https://www.yelp.com/biz/east-beach-tacos-santa-barbara'
Santo_Mezcal = 'https://www.yelp.com/biz/santo-mezcal-santa-barbara'
Taqueria_Cuernavaca = 'https://www.yelp.com/biz/taqueria-cuernavaca-santa-barbara'
Luna_Grill = 'https://www.yelp.com/biz/luna-grill-santa-barbara-3'
Mesa_Verde = 'https://www.yelp.com/biz/mesa-verde-santa-barbara-4'
Zaytoon = 'https://www.yelp.com/biz/zaytoon-santa-barbara'
CPK = 'https://www.yelp.com/biz/california-pizza-kitchen-at-santa-barbara-santa-barbara'
Uncle_Roccos = 'https://www.yelp.com/biz/uncle-roccos-famous-ny-pizza-santa-barbara'
Mesa_Pizza = 'https://www.yelp.com/biz/mesa-pizza-santa-barbara'
Petrinis_Italian = 'https://www.yelp.com/biz/petrinis-italian-restaurant-santa-barbara-santa-barbara'
Persona_Pizzeria = 'https://www.yelp.com/biz/persona-pizzeria-santa-barbara-4'
Patxis_Pizza = 'https://www.yelp.com/biz/patxis-pizza-santa-barbara'
Arnoldis_Cafe = 'https://www.yelp.com/biz/arnoldis-cafe-santa-barbara'
Crocodile_Restaurant_Bar = 'https://www.yelp.com/biz/crocodile-restaurant-and-bar-santa-barbara'
Presto_Pasta = 'https://www.yelp.com/biz/presto-pasta-santa-barbara-2'
Pascucci = 'https://www.yelp.com/biz/pascucci-santa-barbara-2'
Olio_Pizzeria = 'https://www.yelp.com/biz/olio-pizzeria-santa-barbara-2'
Trattoria_Vittoria = 'https://www.yelp.com/biz/trattoria-vittoria-santa-barbara'
OPPIZ_Bistro = 'https://www.yelp.com/biz/oppi-z-bistro-and-natural-pizza-santa-barbara'
Convivo_Restaurant_Bar = 'https://www.yelp.com/biz/convivo-restaurant-and-bar-santa-barbara-3'
Mollies = 'https://www.yelp.com/biz/mollies-santa-barbara-3'
Bettina = 'https://www.yelp.com/biz/bettina-santa-barbara'
Mizza = 'https://www.yelp.com/biz/mizza-santa-barbara-2"'
Moby_Dick = 'https://www.yelp.com/biz/moby-dick-restaurant-santa-barbara?osq=moby+dick'
Kanaloa = 'https://www.yelp.com/biz/kanaloa-seafood-santa-barbara-2'
The_Harbor_Restaurant = 'https://www.yelp.com/biz/the-harbor-restaurant-santa-barbara'
The_Drunken_Crab = 'https://www.yelp.com/biz/the-drunken-crab-santa-barbara-7'
Santa_Barbara_Fish_House = 'https://www.yelp.com/biz/santa-barbara-fishouse-santa-barbara'
Teddys = 'https://www.yelp.com/biz/teddys-by-the-sea-carpinteria'
Bluewater_Grill = 'https://www.yelp.com/biz/bluewater-grill-santa-barbara-santa-barbara-2'
Brophy_Bros = 'https://www.yelp.com/biz/brophy-bros-santa-barbara-santa-barbara'
Lure_Fish_House = 'https://www.yelp.com/biz/lure-fish-house-santa-barbara?osq=Lure+Fish+House'
Opal_Restaurant_Bar = 'https://www.yelp.com/biz/opal-restaurant-and-bar-santa-barbara'
Santa_Barbara_Shellfish_Company = 'https://www.yelp.com/biz/santa-barbara-shellfish-company-santa-barbara'
Galanga_Thai_Restaurant = 'https://www.yelp.com/biz/galanga-thai-restaurant-santa-barbara'
Shintori_Sushi_Factory = 'https://www.yelp.com/biz/shintori-sushi-factory-santa-barbara'
Ichiban = 'https://www.yelp.com/biz/ichiban-santa-barbara'
Kyoto = 'https://www.yelp.com/biz/kyoto-santa-barbara'
Sushi_GoGo = 'https://www.yelp.com/biz/sushi-gogo-santa-barbara'
TAP_Thai_Cuisine = 'https://www.yelp.com/biz/tap-thai-cuisine-santa-barbara-2'
Mandarin_Palace = 'https://www.yelp.com/biz/mandarin-palace-santa-barbara'
Zen_Yai_Thai = 'https://www.yelp.com/biz/zen-yai-thai-cuisine-santa-barbara'
Phoevermore = 'https://www.yelp.com/biz/phoevermore-carpinteria-2'
Sachi_Ramen = 'https://www.yelp.com/biz/sachi-ramen-and-robata-bar-santa-barbara-2'
Your_Place_Thai = 'https://www.yelp.com/biz/your-place-thai-restaurant-santa-barbara-2'
Shang_Hai = 'https://www.yelp.com/biz/shang-hai-santa-barbara-2'
Wabi_Sabi = 'https://www.yelp.com/biz/wabi-sabi-santa-barbara'
Sun_Sushi = 'https://www.yelp.com/biz/sun-sushi-santa-barbara'
Sushi_Bar_29 = 'https://www.yelp.com/biz/sushi-bar-29-santa-barbara'
Saigon_Vietnamese_Restaurant = 'https://www.yelp.com/biz/saigon-vietnamese-restaurant-santa-barbara-2'
Kimchi_Korean_BBQ = 'https://www.yelp.com/biz/kimchi-korean-bbq-santa-barbara'
Meet_Up_Chinese_Cuisine = 'https://www.yelp.com/biz/meet-up-chinese-cuisine-santa-barbara'
Sama_Sama_Kitchen = 'https://www.yelp.com/biz/sama-sama-kitchen-santa-barbara'
Empty_Bowl_Noodle_Bar = 'https://www.yelp.com/biz/empty-bowl-gourmet-noodle-bar-santa-barbara'
Santa_Barbara_Craft_Ramen = 'https://www.yelp.com/biz/santa-barbara-craft-ramen-santa-barbara'
Embermill = 'https://www.yelp.com/biz/embermill-santa-barbara'
Cubaneo = 'https://www.yelp.com/biz/cubaneo-santa-barbara'
Brasil_Arts_Cafe = 'https://www.yelp.com/biz/brasil-arts-cafe-santa-barbara'
Petit_Valentien = 'https://www.yelp.com/biz/petit-valentien-santa-barbara'
Apna_Indian_Kitchen = 'https://www.yelp.com/biz/apna-indian-kitchen-santa-barbara'
Himilayan_Kitchen = 'https://www.yelp.com/biz/himalayan-kitchen-santa-barbara-5?osq=Himalaya+Kitchen'
Flavor_of_India = 'https://www.yelp.com/biz/flavor-of-india-santa-barbara'

SB_expensive = {
    "American": ['Wine Cask','Blackbird','Tee-Off Restaurant and Lounge',"Lucky's",'The Lark','Barbareno','Stonehouse Restaurant',"Holdren's Steaks & Seafood"],
    "Indian": ['Bibi Ji'],
    "French": ['Bouchon',"Stella Mare's"],
    "Japanese": ['Sakana Sushi Bar','Oku','Yoichi','Arigato Sushi'],
    "Italian": ['Tre Lune','Toma Restaurant & Bar','Olio E Limone Ristorante'],
    "Spanish": ['Loquita']}

Wine_Cask = 'https://www.yelp.com/biz/wine-cask-santa-barbara'
Tee_Off = 'https://www.yelp.com/biz/tee-off-restaurant-and-lounge-santa-barbara'
Luckys = 'https://www.yelp.com/biz/luckys-montecito'
The_Lark = 'https://www.yelp.com/biz/the-lark-santa-barbara-3'
Barbareno = 'https://www.yelp.com/biz/barbare%C3%B1o-santa-barbara'
Stonehouse_Restaurant = 'https://www.yelp.com/biz/stonehouse-restaurant-santa-barbara-2'
Holdrens = 'https://www.yelp.com/biz/holdrens-steaks-and-seafood-santa-barbara-2'
Bibi_Ji = 'https://www.yelp.com/biz/bibi-ji-santa-barbara'
Bouchon = 'https://www.yelp.com/biz/bouchon-santa-barbara'
Stella_Mares = 'https://www.yelp.com/biz/stella-mares-santa-barbara-2'
Sakana_Sushi_Bar = 'https://www.yelp.com/biz/sakana-sushi-bar-and-japanese-santa-barbara'
Oku = 'https://www.yelp.com/biz/oku-santa-barbara'
Yoichi = 'https://www.yelp.com/biz/yoichis-santa-barbara'
Arigato_Sushi = 'https://www.yelp.com/biz/arigato-sushi-santa-barbara'
Tre_Lune = 'https://www.yelp.com/biz/tre-lune-montecito'
Toma_Restaurant = 'https://www.yelp.com/biz/toma-restaurant-and-bar-santa-barbara'
Olio_E_Limone = 'https://www.yelp.com/biz/olio-e-limone-ristorante-santa-barbara'
Loquita = 'https://www.yelp.com/biz/loquita-santa-barbara-2'
Blackbird = 'https://www.yelp.com/biz/blackbird-santa-barbara-2?osq=Restaurants'

#Commands/if statements
location = input("Enter City (IV, Goleta, or SB): ")
if location == 'IV':
    meal = input("Breakfast, Lunch, or Dinner: ")
    if meal == 'B':
        restaurant = random.choice(IV_breakfast[meal])
        print(restaurant)
    if meal == 'L':
        Category = input("Enter Cuisine: ")
        restaurant = random.choice(IV_list[Category])
        print(restaurant)
    if meal == 'D':
        Category = input("Enter Cuisine: ")
        restaurant = random.choice(IV_list[Category])
        print(restaurant)

        
if location == 'Goleta':
    meal = input("Breakfast, Lunch, or Dinner: ")
    if meal == 'B':
        restaurant = random.choice(Goleta_breakfast[meal])
        print(restaurant)
    if meal == 'L':
        price = input("Enter Price: ")
        if price == '$':
            Category = input("Enter Cuisine: ")
            restaurant = random.choice(Goleta_cheap[Category])
            print(restaurant)
        if price == '$$':
            Category = input("Enter Cuisine: ")
            restaurant = random.choice(Goleta_list[Category])
            print(restaurant)
        if price == '$$$':
            Category = input("Enter Cuisine: ")
            restaurant = random.choice(Goleta_expensive[Category])
            print(restaurant)
    if meal == 'D':
        price = input("Enter Price: ")
        if price == '$':
            Category = input("Enter Cuisine: ")
            restaurant = random.choice(Goleta_cheap[Category])
            print(restaurant)
        if price == '$$':
            Category = input("Enter Cuisine: ")
            restaurant = random.choice(Goleta_list[Category])
            print(restaurant)
        if price == '$$$':
            Category = input("Enter Cuisine: ")
            restaurant = random.choice(Goleta_expensive[Category])
            print(restaurant)

if location == 'SB':
    meal = input("Breakfast, Lunch, or Dinner: ")
    if meal == 'B':
        restaurant = random.choice(SB_breakfast[meal])
        print(restaurant)
    if meal == 'L':
        price = input("Enter Price: ")
        if price == '$':
            Category = input("Enter Cuisine: ")
            restaurant = random.choice(SB_cheap[Category])
            print(restaurant)
        if price == '$$':
            Category = input("Enter Cuisine: ")
            restaurant = random.choice(SB_list[Category])
            print(restaurant)
        if price == '$$$':
            Category = input("Enter Cuisine: ")
            restaurant = random.choice(SB_expensive[Category])
            print(restaurant)

    if meal == 'D':
        price = input("Enter Price: ")
        if price == '$':
            Category = input("Enter Cuisine: ")
            restaurant = random.choice(SB_cheap[Category])
            print(restaurant)
        if price == '$$':
            Category = input("Enter Cuisine: ")
            restaurant = random.choice(SB_list[Category])
            print(restaurant)
        if price == '$$$':
            Category = input("Enter Cuisine: ")
            restaurant = random.choice(SB_expensive[Category])
            print(restaurant)

if restaurant == 'Buddha Bowls':
    webbrowser.get(chrome_path).open(Buddha)
if restaurant == 'Rockfire Grill':
    webbrowser.get(chrome_path).open(Rockfire)
if restaurant == 'Habit':
    webbrowser.get(chrome_path).open(Habit)
if restaurant == 'IV Deli':
    webbrowser.get(chrome_path).open(IV_Deli)
if restaurant == 'Deja Vu':
    webbrowser.get(chrome_path).open(Deja_Vu)
if restaurant == "Sam's To Go":
    webbrowser.get(chrome_path).open(Sams)
if restaurant == 'Kaiju':
    webbrowser.get(chrome_path).open(Kaiju)
if restaurant == 'Subway':
    webbrowser.get(chrome_path).open(Subway)
if restaurant == "Kyle's":
    webbrowser.get(chrome_path).open(Kyles)
if restaurant == 'Romaine':
    webbrowser.get(chrome_path).open(Romaine)
if restaurant == 'Root 217':
    webbrowser.get(chrome_path).open(Root_217)
if restaurant == 'Bagel Cafe':
    webbrowser.get(chrome_path).open(Bagel)
if restaurant == 'Spudnuts':
    webbrowser.get(chrome_path).open(Spudnuts)
if restaurant == 'Caje':
    webbrowser.get(chrome_path).open(Caje)
if restaurant == 'Freebirds':
    webbrowser.get(chrome_path).open(Freebirds)
if restaurant == "Super Cuca's":
    webbrowser.get(chrome_path).open(Super_Cuca)
if restaurant == 'Rosarito':
    webbrowser.get(chrome_path).open(Rosarito)
if restaurant == 'Tacos and Taproom':
    webbrowser.get(chrome_path).open(Tacos_Taproom)
if restaurant == "Wahoo's":
    webbrowser.get(chrome_path).open(Wahoos)
if restaurant == 'Panda Express':
    webbrowser.get(chrome_path).open(Panda)
if restaurant == 'Poke Theory':
    webbrowser.get(chrome_path).open(Poke_Theory)
if restaurant == 'Naan Stop':
    webbrowser.get(chrome_path).open(NaanStop)
if restaurant == "Su's Bowls":
    webbrowser.get(chrome_path).open(Sus_Bowls)
if restaurant == 'Hana Kitchen':
    webbrowser.get(chrome_path).open(Hana)
if restaurant == 'PokeCeviche':
    webbrowser.get(chrome_path).open(PokeCeviche)
if restaurant == 'Sizzling Lunch':
    webbrowser.get(chrome_path).open(Sizzling)
if restaurant == 'Mojo Asian Fusion':
    webbrowser.get(chrome_path).open(Mojo)
if restaurant == 'Pho Bistro':
    webbrowser.get(chrome_path).open(Pho_Bistro)
if restaurant == 'Sushiya Express':
    webbrowser.get(chrome_path).open(Sushiya)
if restaurant == 'Lao Wang':
    webbrowser.get(chrome_path).open(Lao_Wang)
if restaurant == "Woodstock's":
    webbrowser.get(chrome_path).open(Woodstocks)
if restaurant == "Domino's":
    webbrowser.get(chrome_path).open(Dominos)
if restaurant == 'Pizza My Heart':
    webbrowser.get(chrome_path).open(Pizza_My_Heart)
if restaurant == 'Santorini Island Grill':
    webbrowser.get(chrome_path).open(Santorini)
if restaurant == "Kyle's Kitchen":
    webbrowser.get(chrome_path).open(Kyles_Kitchen)
if restaurant == 'Sandpiper Grill':
    webbrowser.get(chrome_path).open(Sandpiper)
if restaurant == 'Three Pickles':
    webbrowser.get(chrome_path).open(Three_Pickles)
if restaurant == 'Natural Cafe':
    webbrowser.get(chrome_path).open(Natural_Cafe)
if restaurant == 'Costco':
    webbrowser.get(chrome_path).open(Costco)
if restaurant == "Dave's Dogs Grill":
    webbrowser.get(chrome_path).open(Daves)
if restaurant == 'In N Out':
    webbrowser.get(chrome_path).open(In_N_Out)
if restaurant == 'Home Plate Grill':
    webbrowser.get(chrome_path).open(Home_Plate_Grill)
if restaurant == 'Goleta Coffee Co':
    webbrowser.get(chrome_path).open(Costco)
if restaurant == 'Santa Barbara Chicken Ranch':
    webbrowser.get(chrome_path).open(SB_Chicken)
if restaurant == "Wendy's":
    webbrowser.get(chrome_path).open(Wendys)
if restaurant == "McDonald's":
    webbrowser.get(chrome_path).open(Mcdonalds)
if restaurant == "Carl's Jr.":
    webbrowser.get(chrome_path).open(Carls)
if restaurant == 'IHOP':
    webbrowser.get(chrome_path).open(IHOP)
if restaurant == "Jersey Mike's":
    webbrowser.get(chrome_path).open(Jersey_Mikes)
if restaurant == 'Jack In The Box':
    webbrowser.get(chrome_path).open(Jack_in_the_Box)
if restaurant == 'KFC':
    webbrowser.get(chrome_path).open(KFC)
if restaurant == "Altamirano's":
    webbrowser.get(chrome_path).open(Altamiranos)
if restaurant == 'Del Valle Grill':
    webbrowser.get(chrome_path).open(Del_Valle_Grill)
if restaurant == 'La Tapatia':
    webbrowser.get(chrome_path).open(La_Tapatia)
if restaurant == 'Chipotle':
    webbrowser.get(chrome_path).open(Chipotle)
if restaurant == 'Taco Bell':
    webbrowser.get(chrome_path).open(Taco_Bell)
if restaurant == 'Cal Taco':
    webbrowser.get(chrome_path).open(Cal_Taco)
if restaurant == "Lilly's Taquiera":
    webbrowser.get(chrome_path).open(Lillys_Taquiera)
if restaurant == "Pollofino's":
    webbrowser.get(chrome_path).open(Pollofinos)
if restaurant == 'La Guerrerita':
    webbrowser.get(chrome_path).open(La_Guerrerita)
if restaurant == 'La Hacienda':
    webbrowser.get(chrome_path).open(La_Hacienda)
if restaurant == 'El Sitio':
    webbrowser.get(chrome_path).open(El_Sitio)
if restaurant == 'Del Pueblo':
    webbrowser.get(chrome_path).open(Del_Pueblo)
if restaurant == 'Noodle City':
    webbrowser.get(chrome_path).open(Noodle_City)
if restaurant == 'Saigon Noodle House':
    webbrowser.get(chrome_path).open(Saigon_Noodle_House)
if restaurant == 'Phamous Cafe':
    webbrowser.get(chrome_path).open(Phamous_Cafe)
if restaurant == 'L&L Hawaiian BBQ':
    webbrowser.get(chrome_path).open(LL)
if restaurant == "Little Ceasar's":
    webbrowser.get(chrome_path).open(Little_Ceasar)
if restaurant == 'Cajun Kitchen':
    webbrowser.get(chrome_path).open(Cajun_Kitchen)
if restaurant == "Domingo's Cafe":
    webbrowser.get(chrome_path).open(Domingos_Cafe)
if restaurant == "Jeannine's":
    webbrowser.get(chrome_path).open(Jeannines)
if restaurant == 'Outpost':
    webbrowser.get(chrome_path).open(Outpost)
if restaurant == 'On The Alley':
    webbrowser.get(chrome_path).open(On_The_Alley)
if restaurant == 'Flir Cafe':
    webbrowser.get(chrome_path).open(Flir_Cafe)
if restaurant == 'Goodland Dining':
    webbrowser.get(chrome_path).open(Goodland_Dining)
if restaurant == "Cody's Cafe":
    webbrowser.get(chrome_path).open(Codys_Cafe)
if restaurant == 'Frog Bar and Grill':
    webbrowser.get(chrome_path).open(Frog_Bar_And_Grill)
if restaurant == 'Panino':
    webbrowser.get(chrome_path).open(Panino)
if restaurant == "Pickle's & Swiss":
    webbrowser.get(chrome_path).open(Pickles_Swiss)
if restaurant == "Woody's BBQ":
    webbrowser.get(chrome_path).open(Woodys_BBQ)
if restaurant == "Chili's":
    webbrowser.get(chrome_path).open(Chilis)
if restaurant == 'The Nugget Bar and Grill':
    webbrowser.get(chrome_path).open(Nugget_Bar_And_Grill)
if restaurant == 'Mesa Burger':
    webbrowser.get(chrome_path).open(Mesa_Burger)
if restaurant == 'Hollister Brewing':
    webbrowser.get(chrome_path).open(Hollister_Brewing)
if restaurant == "Jane at the Marketplace":
    webbrowser.get(chrome_path).open(Jane)
if restaurant == "Rooftop Bistro & Bar":
    webbrowser.get(chrome_path).open(Rooftop_Bistro_Bar)
if restaurant == "Nikka Fish Market":
    webbrowser.get(chrome_path).open(Nikka_Fish_Market)
if restaurant == "China King":
    webbrowser.get(chrome_path).open(China_King)
if restaurant == "Meun Fan Thai Cafe":
    webbrowser.get(chrome_path).open(Meun_Fan_Thai_Cafe)
if restaurant == "Masala Spice":
    webbrowser.get(chrome_path).open(Masla_Spice)
if restaurant == "Choppa Poke":
    webbrowser.get(chrome_path).open(Choppa_Poke)
if restaurant == "Goleta Sushi House":
    webbrowser.get(chrome_path).open(Goleta_Sushi_House)
if restaurant == "Red Pepper":
    webbrowser.get(chrome_path).open(Red_Pepper)
if restaurant == "Choi Oriental Market":
    webbrowser.get(chrome_path).open(Choi_Oriental_Market)
if restaurant == "Ca'Dario":
    webbrowser.get(chrome_path).open(CaDario)
if restaurant == "Rusty's Pizza":
    webbrowser.get(chrome_path).open(Rustys_Pizza)
if restaurant == "Los Agaves":
    webbrowser.get(chrome_path).open(Los_Agaves)
if restaurant == "Los Arroyos":
    webbrowser.get(chrome_path).open(Los_Arroyos)
if restaurant == "Pepe's":
    webbrowser.get(chrome_path).open(Pepes)
if restaurant == "Costa Terraza":
    webbrowser.get(chrome_path).open(Costa_Terraza)
if restaurant == "Angel Oak at Bacara":
    webbrowser.get(chrome_path).open(Angel_Oak)
if restaurant == "The Bistro":
    webbrowser.get(chrome_path).open(The_Bistro)
if restaurant == "Char West":
    webbrowser.get(chrome_path).open(Char_West)
if restaurant == "Breakwater Restaurant":
    webbrowser.get(chrome_path).open(Pepes)
if restaurant == "Shoreline Beach Cafe":
    webbrowser.get(chrome_path).open(Shoreline_Beach_Cafe)
if restaurant == "The Shop Kitchen":
    webbrowser.get(chrome_path).open(The_Shop_Kitchen)
if restaurant == "Mesa Cafe":
    webbrowser.get(chrome_path).open(Mesa_Cafe)
if restaurant == "Farmer Boy":
    webbrowser.get(chrome_path).open(Farmer_Boy)
if restaurant == "Denny's":
    webbrowser.get(chrome_path).open(Denny)
if restaurant == "Boathouse":
    webbrowser.get(chrome_path).open(Boathouse)
if restaurant == "Dawn Patrol":
    webbrowser.get(chrome_path).open(Dawn_Patrol)
if restaurant == "Bree'osh":
    webbrowser.get(chrome_path).open(Breeosh)
if restaurant == "Finch and Fork":
    webbrowser.get(chrome_path).open(Finch_Fork)
if restaurant == "Chad's":
    webbrowser.get(chrome_path).open(Chads)
if restaurant == "Scarlett Begonia":
    webbrowser.get(chrome_path).open(Scarlett_Begonia)
if restaurant == "SB Sunshine Cafe":
    webbrowser.get(chrome_path).open(SB_Sunshine_Cafe)
if restaurant == "Helena Ave Bakery":
    webbrowser.get(chrome_path).open(Helena_Ave_Bakery)
if restaurant == "Garrett's Old Fashioned":
    webbrowser.get(chrome_path).open(Garretts)
if restaurant == "Andersen's Danish Bakery":
    webbrowser.get(chrome_path).open(Andersens)
if restaurant == "State & Fig":
    webbrowser.get(chrome_path).open(State_And_Fig)
if restaurant == "JJ's Diner":
    webbrowser.get(chrome_path).open(JJs_Diner)
if restaurant == "Yellow Belly":
    webbrowser.get(chrome_path).open(Yellow_Belly)
if restaurant == "Live Oak Cafe":
    webbrowser.get(chrome_path).open(Live_Oak_Cafe)
if restaurant == "4 Eggs & Pizza":
    webbrowser.get(chrome_path).open(Four_Eggs_Pizza)
if restaurant == "Jack's Bistro":
    webbrowser.get(chrome_path).open(Jacks_Bistro)
if restaurant == "Mulligan's Cafe & Bar":
    webbrowser.get(chrome_path).open(Mulligans)
if restaurant == "La Paloma":
    webbrowser.get(chrome_path).open(La_Paloma)
if restaurant == 'El Pollo Loco':
    webbrowser.get(chrome_path).open(El_Pollo_Loco)
if restaurant == 'Burger Express':
    webbrowser.get(chrome_path).open(Burger_Express)
if restaurant == 'Milpas Taqueria':
    webbrowser.get(chrome_path).open(Milpas_Taqueria)
if restaurant == "Mayo's Carniceria":
    webbrowser.get(chrome_path).open(Mayos_Carniceria)
if restaurant == 'Su Casa':
    webbrowser.get(chrome_path).open(Su_Casa)
if restaurant == 'Taqueria Rincon':
    webbrowser.get(chrome_path).open(Taqueria_Rincon)
if restaurant == 'El Zarape':
    webbrowser.get(chrome_path).open(El_Zarape)
if restaurant == "Rudy's":
    webbrowser.get(chrome_path).open(Rudys)
if restaurant == 'Taqueria el Buen Gusto':
    webbrowser.get(chrome_path).open(Taqueria_el_Buen_Gusto)
if restaurant == "Mony's Mexican Food":
    webbrowser.get(chrome_path).open(Monys_Mexican_Food)
if restaurant == "Rudy's Restaurant":
    webbrowser.get(chrome_path).open(Rudys_Restaurant)
if restaurant == 'Taqueria el Bajio':
    webbrowser.get(chrome_path).open(Taqueria_El_Bajio)
if restaurant == 'Tacos Pipeye':
    webbrowser.get(chrome_path).open(Tacos_Pipeye)
if restaurant == 'La-Super-Rica':
    webbrowser.get(chrome_path).open(La_Super_Rica)
if restaurant == 'Buenda Onda':
    webbrowser.get(chrome_path).open(Buenda_Onda)
if restaurant == 'Mels':
    webbrowser.get(chrome_path).open(Mels)
if restaurant == 'Chubbies Hamburgers':
    webbrowser.get(chrome_path).open(Chubbies_Hamburgers)
if restaurant == 'South Coast Deli':
    webbrowser.get(chrome_path).open(South_Coast_Deli)
if restaurant == 'Plaza Deli':
    webbrowser.get(chrome_path).open(Plaza_Deli)
if restaurant == 'Chick Fil A':
    webbrowser.get(chrome_path).open(Chick_Fil_A)
if restaurant == "Gino's Sicilian Express":
    webbrowser.get(chrome_path).open(Ginos_Sicilian_Express)
if restaurant == "Nona's Italian Deli":
    webbrowser.get(chrome_path).open(Nonas_Italian_Deli)
if restaurant == 'The Press Room':
    webbrowser.get(chrome_path).open(The_Press_Room)
if restaurant == "Joe's Cafe":
    webbrowser.get(chrome_path).open(Joes_Cafe)
if restaurant == 'Uptown Bar & Lounge':
    webbrowser.get(chrome_path).open(Uptown_Bar_Lounge)
if restaurant == "Derf's Cafe":
    webbrowser.get(chrome_path).open(Derfs_Cafe)
if restaurant == 'The Waterline':
    webbrowser.get(chrome_path).open(The_Waterline)
if restaurant == "Island's":
    webbrowser.get(chrome_path).open(Islands)
if restaurant == "Longboard's Grill":
    webbrowser.get(chrome_path).open(Longboards_Grill)
if restaurant == 'Eureka!':
    webbrowser.get(chrome_path).open(Eureka)
if restaurant == 'SB Munchiez':
    webbrowser.get(chrome_path).open(SB_Munchiez)
if restaurant == 'Nook':
    webbrowser.get(chrome_path).open(Nook)
if restaurant == "Jill's Place":
    webbrowser.get(chrome_path).open(Jills_Place)
if restaurant == 'Seven Bar and Kitchen':
    webbrowser.get(chrome_path).open(Seven_Bar_and_Kitchen)
if restaurant == 'Little Kitchen':
    webbrowser.get(chrome_path).open(Little_Kitchen)
if restaurant == "Shalhoob's Funk Zone Patio":
    webbrowser.get(chrome_path).open(Shalhoobs_Funk_Zone_Patio)
if restaurant == "Bossie's Kitchen":
    webbrowser.get(chrome_path).open(Bossies_Kitchen)
if restaurant == 'Padaro Beach Grill':
    webbrowser.get(chrome_path).open(Padaro_Beach_Grill)
if restaurant == 'The Palace Grill':
    webbrowser.get(chrome_path).open(The_Palace_Grill)
if restaurant == 'The Black Sheep':
    webbrowser.get(chrome_path).open(The_Black_Sheep)
if restaurant == "Finney's Crafthouse":
    webbrowser.get(chrome_path).open(Finneys_Crafthouse)
if restaurant == 'Los Altos':
    webbrowser.get(chrome_path).open(Los_Altos)
if restaurant == 'El Paseo':
    webbrowser.get(chrome_path).open(El_Paseo)
if restaurant == "Carlito's Cafe Y Cantina":
    webbrowser.get(chrome_path).open(Carlitos)
if restaurant == 'La Playa Azul Cafe':
    webbrowser.get(chrome_path).open(La_Playa_Azul_Cafe)
if restaurant == 'Rosales Mexican Restaurant':
    webbrowser.get(chrome_path).open(Rosales_Mexican_Restaurant)
if restaurant == 'Cava Restaurant & Bar':
    webbrowser.get(chrome_path).open(Cava_Restaurant_Bar)
if restaurant == 'Corazon Cocina':
    webbrowser.get(chrome_path).open(Corazon_Cocina)
if restaurant == 'East Beach Tacos':
    webbrowser.get(chrome_path).open(East_Beach_Tacos)
if restaurant == 'Santo Mezcal':
    webbrowser.get(chrome_path).open(Santo_Mezcal)
if restaurant == 'Taqueria Cuernavaca':
    webbrowser.get(chrome_path).open(Taqueria_Cuernavaca)
if restaurant == 'Luna Grill':
    webbrowser.get(chrome_path).open(Luna_Grill)
if restaurant == 'Mesa Verde':
    webbrowser.get(chrome_path).open(Mesa_Verde)
if restaurant == 'Zaytoon':
    webbrowser.get(chrome_path).open(Zaytoon)
if restaurant == 'California Pizza Kitchen':
    webbrowser.get(chrome_path).open(CPK)
if restaurant == "Uncle Rocco's NY Pizza":
    webbrowser.get(chrome_path).open(Uncle_Roccos)
if restaurant == 'Mesa Pizza':
    webbrowser.get(chrome_path).open(Mesa_Pizza)
if restaurant == "Petrini's Italian Restaurant":
    webbrowser.get(chrome_path).open(Petrinis_Italian)
if restaurant == 'Persona Pizzeria':
    webbrowser.get(chrome_path).open(Persona_Pizzeria)
if restaurant == "Patxi's Pizza":
    webbrowser.get(chrome_path).open(Patxis_Pizza)
if restaurant == "Arnoldi's Cafe":
    webbrowser.get(chrome_path).open(Arnoldis_Cafe)
if restaurant == 'Crocodile Restaurant & Bar':
    webbrowser.get(chrome_path).open(Crocodile_Restaurant_Bar)
if restaurant == 'Presto Pasta':
    webbrowser.get(chrome_path).open(Presto_Pasta)
if restaurant == 'Pascucci':
    webbrowser.get(chrome_path).open(Pascucci)
if restaurant == 'Olio Pizzeria':
    webbrowser.get(chrome_path).open(Olio_Pizzeria)
if restaurant == 'Trattoria Vittoria':
    webbrowser.get(chrome_path).open(Trattoria_Vittoria)
if restaurant == "OPPI'Z Bistro":
    webbrowser.get(chrome_path).open(OPPIZ_Bistro)
if restaurant == 'Convivo Restaurant and Bar':
    webbrowser.get(chrome_path).open(Convivo_Restaurant_Bar)
if restaurant == "Mollie's":
    webbrowser.get(chrome_path).open(Mollies)
if restaurant == 'Bettina':
    webbrowser.get(chrome_path).open(Bettina)
if restaurant == 'Mizza':
    webbrowser.get(chrome_path).open(Mizza)
if restaurant == 'Moby Dick':
    webbrowser.get(chrome_path).open(Moby_Dick)
if restaurant == 'Kanaloa':
    webbrowser.get(chrome_path).open(Kanaloa)
if restaurant == 'The Harbor Restaurant':
    webbrowser.get(chrome_path).open(The_Harbor_Restaurant)
if restaurant == 'The Drunken Crab':
    webbrowser.get(chrome_path).open(The_Drunken_Crab)
if restaurant == 'Santa Barbara Fish House':
    webbrowser.get(chrome_path).open(The_Santa_Barbara_Fish_House)
if restaurant == "Teddy's By The Sea":
    webbrowser.get(chrome_path).open(Teddys)
if restaurant == 'Bluewater Grill':
    webbrowser.get(chrome_path).open(Bluewater_Grill)
if restaurant == 'Brophy Bros':
    webbrowser.get(chrome_path).open(Brophy_Bros)
if restaurant == 'Lure Fish House':
    webbrowser.get(chrome_path).open(Lure_Fish_House)
if restaurant == 'Opal Restaurant and Bar':
    webbrowser.get(chrome_path).open(Opal_Restaurant_Bar)
if restaurant == 'Santa Barbara Shellfish Company':
    webbrowser.get(chrome_path).open(Santa_Barbara_Shellfish_Company)
if restaurant == 'Galanga Thai Restaurant':
    webbrowser.get(chrome_path).open(Galanga_Thai_Restaurant)
if restaurant == 'Shintori Sushi Factory':
    webbrowser.get(chrome_path).open(Shintori_Sushi_Factory)
if restaurant == 'Ichiban':
    webbrowser.get(chrome_path).open(Ichiban)
if restaurant == 'Kyoto':
    webbrowser.get(chrome_path).open(Kyoto)
if restaurant == 'Sushi GoGo':
    webbrowser.get(chrome_path).open(Sushi_GoGo)
if restaurant == 'TAP Thai Cuisine':
    webbrowser.get(chrome_path).open(TAP_Thai_Cuisine)
if restaurant == 'Mandarin Palace':
    webbrowser.get(chrome_path).open(Mandarin_Palace)
if restaurant == 'Zen Yai Thai':
    webbrowser.get(chrome_path).open(Zen_Yai_Thai)
if restaurant == 'Phoevermore':
    webbrowser.get(chrome_path).open(Phoevermore)
if restaurant == 'Sachi Ramen':
    webbrowser.get(chrome_path).open(Sachi_Ramen)
if restaurant == 'Your Place Thai':
    webbrowser.get(chrome_path).open(Caje)
if restaurant == 'Shang Hai':
    webbrowser.get(chrome_path).open(Shang_Hai)
if restaurant == 'Wabi Sabi':
    webbrowser.get(chrome_path).open(Wabi_Sabi)
if restaurant == 'Sun Sushi':
    webbrowser.get(chrome_path).open(Sun_Sushi)
if restaurant == 'Sushi Bar 29':
    webbrowser.get(chrome_path).open(Sushi_Bar_29)
if restaurant == 'Saigon Vietnamese Restaurant':
    webbrowser.get(chrome_path).open(Saigon_Vietnamese_Restaurant)
if restaurant == 'Kimchi Korean BBQ':
    webbrowser.get(chrome_path).open(Caje)
if restaurant == 'Meet Up Chinese Cuisine':
    webbrowser.get(chrome_path).open(Meet_Up_Chinese_Cuisine)
if restaurant == 'Sama Sama Kitchen':
    webbrowser.get(chrome_path).open(Sama_Sama_Kitchen)
if restaurant == 'Empty Bowl Noodle Bar':
    webbrowser.get(chrome_path).open(Empty_Bowl_Noodle_Bar)
if restaurant == 'Santa Barbara Craft Ramen':
    webbrowser.get(chrome_path).open(Santa_Barbara_Craft_Ramen)
if restaurant == 'Embermill':
    webbrowser.get(chrome_path).open(Embermill)
if restaurant == 'Cubaneo':
    webbrowser.get(chrome_path).open(Cubaneo)
if restaurant == 'Brasil Arts Cafe':
    webbrowser.get(chrome_path).open(Brasil_Arts_Cafe)
if restaurant == 'Petit Valentien':
    webbrowser.get(chrome_path).open(Petit_Valentien)
if restaurant == 'Apna Indian Kitchen':
    webbrowser.get(chrome_path).open(Apna_Indian_Kitchen)
if restaurant == 'Himilayan Kitchen':
    webbrowser.get(chrome_path).open(Himalayan_Kitchen)
if restaurant == 'Flavor of India':
    webbrowser.get(chrome_path).open(Flavor_of_India)
if restaurant == 'Wine Cask':
    webbrowser.get(chrome_path).open(Wine_Cask)
if restaurant == 'Tee-Off Restaurant and Lounge':
    webbrowser.get(chrome_path).open(Caje)
if restaurant == "Lucky's":
    webbrowser.get(chrome_path).open(Luckys)
if restaurant == 'The Lark':
    webbrowser.get(chrome_path).open(The_Lark)
if restaurant == 'Barbareno':
    webbrowser.get(chrome_path).open(Barbareno)
if restaurant == 'Stonehouse Restaurant':
    webbrowser.get(chrome_path).open(Stonehouse_Restaurant)
if restaurant == "Holdren's Steak & Seafood":
    webbrowser.get(chrome_path).open(Holdrens)
if restaurant == 'Bibi Ji':
    webbrowser.get(chrome_path).open(Bibi_Ji)
if restaurant == 'Bouchon':
    webbrowser.get(chrome_path).open(Bouchon)
if restaurant == "Stella Mare's":
    webbrowser.get(chrome_path).open(Stella_Mares)
if restaurant == 'Sakana Sushi Bar':
    webbrowser.get(chrome_path).open(Sakana_Sushi_Bar)
if restaurant == 'Oku':
    webbrowser.get(chrome_path).open(Oku)
if restaurant == 'Yoichi':
    webbrowser.get(chrome_path).open(Yoichi)
if restaurant == 'Arigato Sushi':
    webbrowser.get(chrome_path).open(Arigato_Sushi)
if restaurant == 'Tre Lune':
    webbrowser.get(chrome_path).open(Tre_Lune)
if restaurant == 'Toma Restaurant':
    webbrowser.get(chrome_path).open(Toma_Restaurant)
if restaurant == 'Olio_E_Limone':
    webbrowser.get(chrome_path).open(Olio_E_Limone)
if restaurant == 'Loquita':
    webbrowser.get(chrome_path).open(Loquita)
if restaurant == 'Blackbird':
    webbrowser.get(chrome_path).open(Blackbird)

