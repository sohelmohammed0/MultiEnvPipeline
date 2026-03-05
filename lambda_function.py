def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": """
        <html>
            <body style="background-color:green;">
                <h1 style="color:white;text-align:center;margin-top:20%;">
                    GREEN prod LAMBDA
                </h1>
            </body>
        </html>
        """
    }