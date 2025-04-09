from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Wild Rydes - DevOps Test</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
      </head>
      <body class="bg-dark text-white d-flex flex-column justify-content-center align-items-center vh-100">
        <div class="text-center">
          <h1 class="display-4 mb-4">🚀 Wild Rydes</h1>
          <p class="lead">DevOps Test #2 Deployed Successfully on ECS Fargate!</p>
          <span class="badge bg-success fs-5 mt-3">Status: LIVE</span>
        </div>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
