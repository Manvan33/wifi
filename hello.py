from flask import Flask, request, render_template_string

app = Flask(__name__)


TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Info</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #f4f4f9;
        }
        .info {
            margin-bottom: 20px;
            padding: 15px;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 80%;
            max-width: 400px;
        }
        button {
            padding: 10px 20px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="info" id="info">
        <p><strong>Your IP Address:</strong> {{ user_ip }}</p>
        <p><strong>User Agent:</strong> {{ user_agent }}</p>
    </div>
    <button onclick="copyToClipboard()">Copy to Clipboard</button>

    <script>
        function copyToClipboard() {
            const infoDiv = document.getElementById('info');
            const range = document.createRange();
            range.selectNode(infoDiv);
            window.getSelection().removeAllRanges();  // Clear current selection
            window.getSelection().addRange(range);    // Select the text
            try {
                const successful = document.execCommand('copy');
                alert(successful ? 'Copied!' : 'Copy failed');
            } catch (err) {
                alert('Oops, unable to copy');
            }
            window.getSelection().removeAllRanges();  // Deselect the text
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    return render_template_string(TEMPLATE, user_ip=user_ip, user_agent=user_agent)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)