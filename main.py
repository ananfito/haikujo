# haikujo (haiku journal)
# main.py 

# import libraries
from datetime import datetime
import csv 
import os 

# get folder where main.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# create file paths for CSV and HTML files
csv_path = os.path.join(base_dir, 'haikus.csv')
html_path = os.path.join(base_dir, 'index.html')

# initialize CSV file 
def initilize_csv():
    if not os.path.exists(csv_path):
        with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['timestamp', 'line1','line2','line3'])


# get haiku lines from user 
def get_haiku_from_user():
    print('\nEnter your haiku line by line.')
    line1 = input('Line 1: ')
    line2 = input('Line 2: ')
    line3 = input('Line 3: ')
    return line1, line2, line3 

# save haiku to CSV 
def save_haiku_to_csv(line1, line2, line3):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(csv_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, line1, line2, line3])
    print('\nHaiku saved!')

# export haiku to HTML file
def export_haikus_to_html(csv_file=csv_path, html_file=html_path):
    html_content = '''
    <html>
        <head>
            <title>haikujo</title>
            <style>
                body {
                    background-color: #FFF5EE;
                    color: #333;
                    font-family: Georgia, serif;
                    text-align: center;
                    max-width: 80%;
                    margin: auto;
                    padding: 2rem;
                }

                .haiku { 
                    font-size: 1.5em;
                    color: #555;
                    font-style: italic;
                }

                .timestamp {
                    color: #555;
                    font-style: normal;
                }

                footer {
                    margin-top: 4rem;
                    text-align: center;
                }

                a {
                    color: #16452C; 
                }
            </style>
        </head>
        <body>
            <h1>haikujo</h1>
            <hr>
    '''

    # read and reverse haikus
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        haikus = list(reader)[::-1] # reverse order

    for row in haikus:
        html_content += f'''
            <div class="haiku">
                <h3 class="timestamp">{row['timestamp']}</h3>
                <p>{row['line1']}</p>
                <p>{row['line2']}</p>
                <p>{row['line3']}</p>
            </div>
            <hr>
        '''
    
    # add footer
    html_content += f'''
        <footer>
            <p>Total haiku: {len(haikus)}</p>
            <p>&copy; 2025 Anthony Nanfito. All rights reserved for haiku content.</p>
            <p>Site code open sourced on <a href="https://github.com/ananfito/haikujo" target="_blank">GitHub</a>.</p>
        </footer>
    '''

    html_content += "</body></html>"

    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f'Exported haikus to {html_file}\n')

# put it all together in main() function
def main():
    initilize_csv()

    while True:
        print('\nWelcome to haikujo')
        print('\nWhat would you like to do?')
        print('1. Write a haiku')
        print('2. Exit')
        choice = input('\nChoose an option (1 or 2): ')

        if choice == '1':
            line1, line2, line3 = get_haiku_from_user()
            save_haiku_to_csv(line1, line2, line3)
            export_haikus_to_html(csv_path, html_path)
        elif choice == '2':
            print('\nGoodbye\n')
            break
        else:
            print('\nInvalid option.\n')

if __name__ == '__main__':
    main()
