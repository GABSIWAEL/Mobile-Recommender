from flask import Flask, render_template, request
import csv

application = Flask(__name__)

# Path to your CSV file
csv_file = 'gsm.csv'

# Read CSV file and store data in memory
def read_csv():
    phones = []
    headers = [
        'Brand', 'Model', 'Network Technology', '2G Bands', 'GPRS', 'EDGE', 'Launch Date', 'Launch Status',
        'Body Dimensions', 'Body Weight', 'SIM', 'Display Type', 'Display Size', 'Display Resolution',
        'Memory Card Slot', 'Phonebook Memory', 'Call Records Memory', 'Loudspeaker', 'Alert Types', '3.5mm Jack',
        'Wi-Fi', 'Bluetooth', 'GPS', 'Radio', 'USB', 'Sensors', 'Messaging', 'Browser', 'Clock', 'Alarm', 'Games',
        'Java', 'Features', 'Colors', '3G Bands', 'Network Speed', 'OS', 'Chipset', 'CPU', 'GPU', 'Internal Memory',
        'Main Camera', 'Main Camera Video', 'Price', 'Main Camera Features', 'Body', '4G Bands', 'Body Build',
        'Display Protection', 'Memory', 'Dual Main Camera', 'Dual Selfie Camera', 'Selfie Camera Features',
        'Selfie Camera Video', 'NFC', 'Battery Charging', 'Models', 'Performance Tests', 'Camera Tests',
        'Loudspeaker Tests', 'Audio Quality Tests', 'Battery Life Tests', 'Display Tests', 'Single Selfie Camera',
        'Infrared Port', '5G Bands', 'Quad Main Camera', 'Triple Main Camera', 'Sound', 'SAR EU', 'Five Main Camera',
        'Languages', 'Keyboard', 'SAR', 'Battery', 'Dual or Triple Main Camera', 'Music Play Battery',
        'Triple Selfie Camera', 'Main Camera Version 1', 'Selfie Camera', 'Camera', 'Main Camera', 'Network',
        'Talk Time Battery', 'Stand-by Battery'
    ]
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            phone = {headers[i]: row[i].strip('"')
                     for i in range(len(headers))}
            phones.append(phone)
    return phones

phones_data = read_csv()

@application.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@application.route('/recommend', methods=['GET', 'POST'])
def recommend():
    phones = []
    user_input = {header: request.args.get(header) for header in phones_data[0].keys()}

    for phone in phones_data:
        match = True
        for key, value in user_input.items():
            if value and phone.get(key) and phone[key].lower() != value.lower():
                match = False
                break
        if match:
            phones.append(phone)

    return render_template('results.html', phones=phones)

if __name__ == '__main__':
    application.run(debug=True)
