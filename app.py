from model import ModelRegression
from flask import Flask, request, render_template, url_for
app = Flask(__name__)


@app.route('/')
def home():
    neighbourhood_cleansed = ['Ang Mo Kio', 'Bedok', 'Bishan', 'Bukit Batok', 'Bukit Merah', 'Bukit Panjang', 'Bukit Timah', 'Central Water Catchment', 'Changi', 'Choa Chu Kang', 'Clementi', 'Downtown Core', 'Geylang', 'Hougang', 'Jurong East', 'Jurong West', 'Kallang', 'Mandai', 'Marina South', 'Marine Parade',
                              'Museum', 'Newton', 'Novena', 'Orchard', 'Outram', 'Pasir Ris', 'Pioneer', 'Punggol', 'Queenstown', 'River Valley', 'Rochor', 'Sembawang', 'Sengkang', 'Serangoon', 'Singapore River', 'Southern Islands', 'Sungei Kadut', 'Tampines', 'Tanglin', 'Toa Payoh', 'Tuas', 'Western Water Catchment', 'Woodlands', 'Yishun']
    room_type = ['Entire home/apt', 'Hotel room',
                 'Private room', 'Shared room']

    amenities = ['Elevator', 'CableTV', 'Washer', 'Wifi', 'TV', 'Airconditioning', 'Essentials', 'Shampoo', 'Gym', 'Pool', 'Kitchen', 'Dryer', 'Dedicatedworkspace', 'Lockonbedroomdoor', 'Gardenorbackyard', 'Smokealarm', 'Refrigerator', 'Freestreetparking', 'Longtermstaysallowed', 'Iron', 'Fireextinguisher', 'Children\\u2019sbooksandtoys', 'Hottub', 'Privateentrance', 'Hangers', 'Hotwater', 'Hairdryer', 'Luggagedropoffallowed', 'Keypad', 'Coffeemaker', 'Paidparkingonpremises', 'Heating', 'Firstaidkit', 'Microwave', 'Patioorbalcony', 'Smartlock', 'Dishesandsilverware', 'Oven', 'Stove', 'Cookingbasics', 'Extrapillowsandblankets', 'Bedlinens', 'Freeparkingonpremises', 'Paidparkingoffpremises', 'Pack\\u2019nPlay/travelcrib', 'Cleaningbeforecheckout', 'Hostgreetsyou', 'BBQgrill', 'Buildingstaff', 'Lockbox', 'Bathtub', 'Carbonmonoxidealarm', 'Breakfast', 'Dishwasher', 'Privatelivingroom', 'Room-darkeningshades', 'Singlelevelhome', 'Showergel', 'Freezer', 'Ethernetconnection', 'Bodysoap', 'Laundromatnearby', 'Pocketwifi', 'Crib', 'Children\\u2019sdinnerware', 'Highchair', 'Babybath', 'Waterfront', 'Beachfront', 'EVcharger', 'Changingtable', 'Paidstreetparkingoffpremises',
                 'Indoorfireplace', 'Lakeaccess', 'Windowguards', 'Ceilingfan', 'Hotwaterkettle', 'Washer\\u2013\\u00a0Inbuilding', 'Dryer\\u2013Inbuilding', 'Ricemaker', 'Stainlesssteeloven', 'Gameconsole', 'SPAbodysoap', 'Toaster', 'Outdoorfurniture', 'Portablefans', 'Bidet', 'Barbecueutensils', 'SPAconditioner', 'Cleaningproducts', 'Outdoordiningarea', 'Sharedsauna', 'Clothingstorage:closet', 'Bakingsheet', 'Pingpongtable', 'Beachessentials', 'Washer\\u2013\\u00a0Inunit', 'Conditioner', 'Tablecornerguards', 'Babysitterrecommendations', 'Breadmaker', 'Outletcovers', 'Pour-overcoffee', 'Babysafetygates', 'Fireplaceguards', '32\\HDTV', 'Freewasher\\u2013Inunit', 'Sharedoutdoorolympic-sizedpool', 'Recordplayer', 'Babymonitor', 'Clothingstorage', 'Diningtable', 'Dryingrackforclothing', 'Soundsystem', 'Nespressomachine', 'Ski-in/Ski-out', 'LGrefrigerator', 'Minifridge', 'Wifi\\u20131000Mbps', 'Paidparkinglotonpremises', 'Electricstove', 'Mielerefrigerator', 'Mieleoven', 'Dryer\\u2013\\u00a0Inunit', 'Paidparkinglotoffpremises', 'Inductionstove', 'Paidparkinggarageoffpremises', 'HDTV', 'Centralairconditioning', 'WindowACunit', 'Trashcompactor', 'Wineglasses', 'Piano']
    neighbourhood_cleansedLen = len(neighbourhood_cleansed)
    room_typeLen = len(room_type)
    amenitiesLen = len(amenities)
    # return str(ModelRegression.Regression([6, 2, 2, 1, 1, 1, 18, 91, 80, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0]))

    return render_template('index.html', neighbourhood_cleansed=neighbourhood_cleansed, room_type=room_type, amenities=amenities, amenitiesLen=amenitiesLen, room_typeLen=room_typeLen, neighbourhood_cleansedLen=neighbourhood_cleansedLen)


@app.route('/regression', methods=['POST'])
def regression():
    amenities = ['Elevator', 'CableTV', 'Washer', 'Wifi', 'TV', 'Airconditioning', 'Essentials', 'Shampoo', 'Gym', 'Pool', 'Kitchen', 'Dryer', 'Dedicatedworkspace', 'Lockonbedroomdoor', 'Gardenorbackyard', 'Smokealarm', 'Refrigerator', 'Freestreetparking', 'Longtermstaysallowed', 'Iron', 'Fireextinguisher', 'Children\\u2019sbooksandtoys', 'Hottub', 'Privateentrance', 'Hangers', 'Hotwater', 'Hairdryer', 'Luggagedropoffallowed', 'Keypad', 'Coffeemaker', 'Paidparkingonpremises', 'Heating', 'Firstaidkit', 'Microwave', 'Patioorbalcony', 'Smartlock', 'Dishesandsilverware', 'Oven', 'Stove', 'Cookingbasics', 'Extrapillowsandblankets', 'Bedlinens', 'Freeparkingonpremises', 'Paidparkingoffpremises', 'Pack\\u2019nPlay/travelcrib', 'Cleaningbeforecheckout', 'Hostgreetsyou', 'BBQgrill', 'Buildingstaff', 'Lockbox', 'Bathtub', 'Carbonmonoxidealarm', 'Breakfast', 'Dishwasher', 'Privatelivingroom', 'Room-darkeningshades', 'Singlelevelhome', 'Showergel', 'Freezer', 'Ethernetconnection', 'Bodysoap', 'Laundromatnearby', 'Pocketwifi', 'Crib', 'Children\\u2019sdinnerware', 'Highchair', 'Babybath', 'Waterfront', 'Beachfront', 'EVcharger', 'Changingtable', 'Paidstreetparkingoffpremises',
                 'Indoorfireplace', 'Lakeaccess', 'Windowguards', 'Ceilingfan', 'Hotwaterkettle', 'Washer\\u2013\\u00a0Inbuilding', 'Dryer\\u2013Inbuilding', 'Ricemaker', 'Stainlesssteeloven', 'Gameconsole', 'SPAbodysoap', 'Toaster', 'Outdoorfurniture', 'Portablefans', 'Bidet', 'Barbecueutensils', 'SPAconditioner', 'Cleaningproducts', 'Outdoordiningarea', 'Sharedsauna', 'Clothingstorage:closet', 'Bakingsheet', 'Pingpongtable', 'Beachessentials', 'Washer\\u2013\\u00a0Inunit', 'Conditioner', 'Tablecornerguards', 'Babysitterrecommendations', 'Breadmaker', 'Outletcovers', 'Pour-overcoffee', 'Babysafetygates', 'Fireplaceguards', '32\\HDTV', 'Freewasher\\u2013Inunit', 'Sharedoutdoorolympic-sizedpool', 'Recordplayer', 'Babymonitor', 'Clothingstorage', 'Diningtable', 'Dryingrackforclothing', 'Soundsystem', 'Nespressomachine', 'Ski-in/Ski-out', 'LGrefrigerator', 'Minifridge', 'Wifi\\u20131000Mbps', 'Paidparkinglotonpremises', 'Electricstove', 'Mielerefrigerator', 'Mieleoven', 'Dryer\\u2013\\u00a0Inunit', 'Paidparkinglotoffpremises', 'Inductionstove', 'Paidparkinggarageoffpremises', 'HDTV', 'Centralairconditioning', 'WindowACunit', 'Trashcompactor', 'Wineglasses', 'Piano']
    paramList = []
    paramList.append(request.form['neighbourhood_cleansed'])
    paramList.append(request.form['room_type'])
    paramList.append(request.form['accomodates'])
    paramList.append(request.form['bathrooms_text'])
    paramList.append(request.form['bedrooms'])
    paramList.append(request.form['beds'])
    paramList.append(request.form['number_of_reviews'])
    paramList.append(request.form['review_scores_rating'])

    for items in amenities:
        try:
            if request.form[items] == "1":
                paramList.append(1)
            else:
                paramList.append(0)
        except:
            print(items)
            paramList.append(0)

    result = ModelRegression.Regression(paramList)

    return render_template('result.html', linReg=result['Linear Regression'], svr=result['Super Vector Regression'])
