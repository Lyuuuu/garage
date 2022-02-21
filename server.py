from sanic import Sanic
from sanic.response import text


app = Sanic('Garage')


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")

if __name__ == '__main__':
    app.update_config('./config/config.py')
    app.run(host='0.0.0.0', port=8011, workers=1, auto_reload=True, debug=True, )

