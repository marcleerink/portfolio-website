from app.app import create_app

def app():
    app = create_app()
    return app

if __name__ == '__main__':
    app.run()
