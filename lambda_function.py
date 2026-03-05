def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": """
        <html>
            <body style="background-color:yellow;">
                <h1 style="color:white;text-align:center;margin-top:20%;">
                    Yellow update test LAMBDA
                </h1>
            </body>
        </html>
        """
    }
