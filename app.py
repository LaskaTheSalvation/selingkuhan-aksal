from flask import Flask

app = Flask(__name__)

@app.route('/')
def generate_flower():
    # Membuat kode HTML untuk menampilkan bunga yang lebih rumit
    flower_html = '''
    <html>
    <head>
        <title>Bunga</title>
    </head>
    <body>
        <h1>Bunga</h1>
        <div style="text-align: center;">
            <svg height="400" width="400">
                <!-- Batang bunga -->
                <rect x="195" y="250" width="10" height="100" fill="brown" />

                <!-- Kelopak bunga -->
                <circle cx="200" cy="150" r="100" fill="orange" />
                <circle cx="200" cy="150" r="80" fill="yellow" />
                <circle cx="200" cy="150" r="60" fill="pink" />
                <circle cx="200" cy="150" r="40" fill="purple" />
                <circle cx="200" cy="150" r="20" fill="red" />

                <!-- Daun bunga -->
                <circle cx="100" cy="240" r="70" fill="green" />
                <circle cx="300" cy="240" r="70" fill="green" />
                <circle cx="70" cy="180" r="70" fill="green" />
                <circle cx="330" cy="180" r="70" fill="green" />

                <!-- Tepi bunga -->
                <circle cx="200" cy="150" r="100" fill="none" stroke="red" stroke-width="4" />
                <circle cx="200" cy="150" r="80" fill="none" stroke="red" stroke-width="4" />
                <circle cx="200" cy="150" r="60" fill="none" stroke="red" stroke-width="4" />
                <circle cx="200" cy="150" r="40" fill="none" stroke="red" stroke-width="4" />
                <circle cx="200" cy="150" r="20" fill="none" stroke="red" stroke-width="4" />
            </svg>
        </div>
    </body>
    </html>
    '''
    return flower_html

if __name__ == '__main__':
    app.run(debug=True)

