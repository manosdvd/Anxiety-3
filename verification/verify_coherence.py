from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the file directly since it is a single HTML file
        file_path = os.path.abspath("coherence.html")
        page.goto(f"file://{file_path}")

        # Wait for React to mount and start screen to appear
        page.wait_for_selector("text=COHERENCE")

        # Click Start Button
        page.click("text=BREATHE")

        # Wait for game to start (breathing meter visible)
        page.wait_for_selector(".grid-container")

        # Wait a few seconds for breathing animation to progress
        page.wait_for_timeout(3000)

        # Screenshot
        page.screenshot(path="verification/coherence_gameplay.png")

        browser.close()

if __name__ == "__main__":
    run()