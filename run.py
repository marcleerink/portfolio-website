from app.app import create_app

app = create_app()
import logging

if __name__ == '__main__':
    app.run()
