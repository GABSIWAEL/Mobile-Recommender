from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Path to your CSV file
csv_file = r'C:\Users\MSI\Desktop\projects\Mobile Recommender\gsm.csv'

# Function to handle user input for each criterion


def get_user_input(prompt):
    while True:
        user_input = request.args.get(prompt)
        if user_input:
            return user_input.strip()
        else:
            return None

# Route for the home page


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

# Route to handle form submission and display results


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    phones = []
    # Get criteria from the user
    user_input = {}
    user_input['Brand'] = get_user_input("Brand")
    user_input['Model'] = get_user_input("Model")
    user_input['Network Technology'] = get_user_input("Network Technology")
    user_input['2G Bands'] = get_user_input("2G Bands")
    user_input['GPRS'] = get_user_input("GPRS")
    user_input['EDGE'] = get_user_input("EDGE")
    user_input['Launch Date'] = get_user_input("Launch Date")
    user_input['Launch Status'] = get_user_input("Launch Status")
    user_input['Body Dimensions'] = get_user_input("Body Dimensions")
    user_input['Body Weight'] = get_user_input("Body Weight")
    user_input['SIM'] = get_user_input("SIM")
    user_input['Display Type'] = get_user_input("Display Type")
    user_input['Display Size'] = get_user_input("Display Size")
    user_input['Display Resolution'] = get_user_input("Display Resolution")
    user_input['Memory Card Slot'] = get_user_input("Memory Card Slot")
    user_input['Phonebook Memory'] = get_user_input("Phonebook Memory")
    user_input['Call Records Memory'] = get_user_input("Call Records Memory")
    user_input['Loudspeaker'] = get_user_input("Loudspeaker")
    user_input['Alert Types'] = get_user_input("Alert Types")
    user_input['3.5mm Jack'] = get_user_input("3.5mm Jack")
    user_input['Wi-Fi'] = get_user_input("Wi-Fi")
    user_input['Bluetooth'] = get_user_input("Bluetooth")
    user_input['GPS'] = get_user_input("GPS")
    user_input['Radio'] = get_user_input("Radio")
    user_input['USB'] = get_user_input("USB")
    user_input['Sensors'] = get_user_input("Sensors")
    user_input['Messaging'] = get_user_input("Messaging")
    user_input['Browser'] = get_user_input("Browser")
    user_input['Clock'] = get_user_input("Clock")
    user_input['Alarm'] = get_user_input("Alarm")
    user_input['Games'] = get_user_input("Games")
    user_input['Java'] = get_user_input("Java")
    user_input['Features'] = get_user_input("Features")
    user_input['Colors'] = get_user_input("Colors")
    user_input['3G Bands'] = get_user_input("3G Bands")
    user_input['Network Speed'] = get_user_input("Network Speed")
    user_input['OS'] = get_user_input("OS")
    user_input['Chipset'] = get_user_input("Chipset")
    user_input['CPU'] = get_user_input("CPU")
    user_input['GPU'] = get_user_input("GPU")
    user_input['Internal Memory'] = get_user_input("Internal Memory")
    user_input['Main Camera'] = get_user_input("Main Camera")
    user_input['Main Camera Video'] = get_user_input("Main Camera Video")
    user_input['Price'] = get_user_input("Price")
    user_input['Main Camera Features'] = get_user_input("Main Camera Features")
    user_input['Body'] = get_user_input("Body")
    user_input['4G Bands'] = get_user_input("4G Bands")
    user_input['Body Build'] = get_user_input("Body Build")
    user_input['Display Protection'] = get_user_input("Display Protection")
    user_input['Memory'] = get_user_input("Memory")
    user_input['Dual Main Camera'] = get_user_input("Dual Main Camera")
    user_input['Dual Selfie Camera'] = get_user_input("Dual Selfie Camera")
    user_input['Selfie Camera Features'] = get_user_input(
        "Selfie Camera Features")
    user_input['Selfie Camera Video'] = get_user_input("Selfie Camera Video")
    user_input['NFC'] = get_user_input("NFC")
    user_input['Battery Charging'] = get_user_input("Battery Charging")
    user_input['Models'] = get_user_input("Models")
    user_input['Performance Tests'] = get_user_input("Performance Tests")
    user_input['Camera Tests'] = get_user_input("Camera Tests")
    user_input['Loudspeaker Tests'] = get_user_input("Loudspeaker Tests")
    user_input['Audio Quality Tests'] = get_user_input("Audio Quality Tests")
    user_input['Battery Life Tests'] = get_user_input("Battery Life Tests")
    user_input['Display Tests'] = get_user_input("Display Tests")
    user_input['Single Selfie Camera'] = get_user_input("Single Selfie Camera")
    user_input['Infrared Port'] = get_user_input("Infrared Port")
    user_input['5G Bands'] = get_user_input("5G Bands")
    user_input['Quad Main Camera'] = get_user_input("Quad Main Camera")
    user_input['Triple Main Camera'] = get_user_input("Triple Main Camera")
    user_input['Sound'] = get_user_input("Sound")
    user_input['SAR EU'] = get_user_input("SAR EU")
    user_input['Five Main Camera'] = get_user_input("Five Main Camera")
    user_input['Languages'] = get_user_input("Languages")
    user_input['Keyboard'] = get_user_input("Keyboard")
    user_input['SAR'] = get_user_input("SAR")
    user_input['Battery'] = get_user_input("Battery")
    user_input['Dual or Triple Main Camera'] = get_user_input(
        "Dual or Triple Main Camera")
    user_input['Music Play Battery'] = get_user_input("Music Play Battery")
    user_input['Triple Selfie Camera'] = get_user_input("Triple Selfie Camera")
    user_input['Main Camera Version 1'] = get_user_input(
        "Main Camera Version 1")
    user_input['Selfie Camera'] = get_user_input("Selfie Camera")
    user_input['Camera'] = get_user_input("Camera")
    user_input['Main Camera'] = get_user_input("Main Camera")
    user_input['Network'] = get_user_input("Network")
    user_input['Talk Time Battery'] = get_user_input("Talk Time Battery")
    user_input['Stand-by Battery'] = get_user_input("Stand-by Battery")

    # Open the CSV file and read data
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')
        # Skip the header row if it exists
        next(csv_reader)
        for row in csv_reader:
            phone = {}
            phone['Brand'] = row[0].strip('"')
            phone['Model'] = row[1].strip('"')
            phone['Network Technology'] = row[2].strip('"')
            phone['2G Bands'] = row[3].strip('"')
            phone['GPRS'] = row[4].strip('"')
            phone['EDGE'] = row[5].strip('"')
            phone['Launch Date'] = row[6].strip('"')
            phone['Launch Status'] = row[7].strip('"')
            phone['Body Dimensions'] = row[8].strip('"')
            phone['Body Weight'] = row[9].strip('"')
            phone['SIM'] = row[10].strip('"')
            phone['Display Type'] = row[11].strip('"')
            phone['Display Size'] = row[12].strip('"')
            phone['Display Resolution'] = row[13].strip('"')
            phone['Display'] = row[14].strip('"')
            phone['Memory Card Slot'] = row[15].strip('"')
            phone['Phonebook Memory'] = row[16].strip('"')
            phone['Call Records Memory'] = row[17].strip('"')
            phone['Loudspeaker'] = row[18].strip('"')
            phone['Alert Types'] = row[19].strip('"')
            phone['3.5mm Jack'] = row[20].strip('"')
            phone['Wi-Fi'] = row[21].strip('"')
            phone['Bluetooth'] = row[22].strip('"')
            phone['GPS'] = row[23].strip('"')
            phone['Radio'] = row[24].strip('"')
            phone['USB'] = row[25].strip('"')
            phone['Sensors'] = row[26].strip('"')
            phone['Messaging'] = row[27].strip('"')
            phone['Browser'] = row[28].strip('"')
            phone['Clock'] = row[29].strip('"')
            phone['Alarm'] = row[30].strip('"')
            phone['Games'] = row[31].strip('"')
            phone['Java'] = row[32].strip('"')
            phone['Features'] = row[33].strip('"')
            phone['Colors'] = row[34].strip('"')
            phone['3G Bands'] = row[35].strip('"')
            phone['Network Speed'] = row[36].strip('"')
            phone['OS'] = row[37].strip('"')
            phone['Chipset'] = row[38].strip('"')
            phone['CPU'] = row[39].strip('"')
            phone['GPU'] = row[40].strip('"')
            phone['Internal Memory'] = row[41].strip('"')
            phone['Main Camera'] = row[42].strip('"')
            phone['Main Camera Video'] = row[43].strip('"')
            phone['Price'] = row[44].strip('"')
            phone['Main Camera Features'] = row[45].strip('"')
            phone['Body'] = row[46].strip('"')
            phone['4G Bands'] = row[47].strip('"')
            phone['Body Build'] = row[48].strip('"')
            phone['Display Protection'] = row[49].strip('"')
            phone['Memory'] = row[50].strip('"')
            phone['Dual Main Camera'] = row[51].strip('"')
            phone['Dual Selfie Camera'] = row[52].strip('"')
            phone['Selfie Camera Features'] = row[53].strip('"')
            phone['Selfie Camera Video'] = row[54].strip('"')
            phone['NFC'] = row[55].strip('"')
            phone['Battery Charging'] = row[56].strip('"')
            phone['Models'] = row[57].strip('"')
            phone['Performance Tests'] = row[58].strip('"')
            phone['Camera Tests'] = row[59].strip('"')
            phone['Loudspeaker Tests'] = row[60].strip('"')
            phone['Audio Quality Tests'] = row[61].strip('"')
            phone['Battery Life Tests'] = row[62].strip('"')
            phone['Display Tests'] = row[63].strip('"')
            phone['Single Selfie Camera'] = row[64].strip('"')
            phone['Infrared Port'] = row[65].strip('"')
            phone['5G Bands'] = row[66].strip('"')
            phone['Quad Main Camera'] = row[67].strip('"')
            phone['Triple Main Camera'] = row[68].strip('"')
            phone['Sound'] = row[69].strip('"')
            phone['SAR EU'] = row[70].strip('"')
            phone['Five Main Camera'] = row[71].strip('"')
            phone['Languages'] = row[72].strip('"')
            phone['Keyboard'] = row[73].strip('"')
            phone['SAR'] = row[74].strip('"')
            phone['Battery'] = row[75].strip('"')
            phone['Dual or Triple Main Camera'] = row[76].strip('"')
            phone['Music Play Battery'] = row[77].strip('"')
            phone['Triple Selfie Camera'] = row[78].strip('"')
            phone['Main Camera Version 1'] = row[79].strip('"')
            phone['Selfie Camera'] = row[80].strip('"')
            phone['Camera'] = row[81].strip('"')
            phone['Main Camera'] = row[82].strip('"')
            phone['Network'] = row[83].strip('"')
            phone['Talk Time Battery'] = row[84].strip('"')
            phone['Stand-by Battery'] = row[85].strip('"')

            # Apply filters based on user input
            match = True
            for key, value in user_input.items():
                if value and phone.get(key) != value:
                    match = False
                    break
            if match:
                phones.append(phone)

    return render_template('results.html', phones=phones)


if __name__ == '__main__':
    app.run(debug=True)
