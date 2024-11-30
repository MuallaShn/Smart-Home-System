import asyncio
import time

from flask import Flask, render_template, jsonify, send_from_directory
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask_cors import CORS




app = Flask(__name__,static_folder="../FRONTEND/myapp/build",static_url_path="/")
@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")





def run_selenium():
    driver = webdriver.Edge()
    driver.get("http://127.0.0.1:5000")
    driver.find_element(by=By.ID,value="center_button").click()
    time.sleep(5)
    driver.quit()


def run_flask():
    app.run(debug=True, use_reloader=False)

async def main():
    await asyncio.gather(
        asyncio.to_thread(run_flask),
        asyncio.to_thread(run_selenium)
    )


if __name__ == "__main__":
    asyncio.run(main())
