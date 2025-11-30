
import os
from playwright.sync_api import sync_playwright

def capture_layouts():
    os.makedirs('verification', exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use mobile viewport to trigger the layout issues
        context = browser.new_context(viewport={'width': 375, 'height': 667})
        page = context.new_page()

        # Capture Anxiety (Reference)
        print("Capturing anxiety.html...")
        page.goto("http://localhost:5174/anxiety.html")
        page.wait_for_selector(".grid-container")
        page.screenshot(path="verification/before_anxiety.png")

        # Capture Coherence (Target)
        print("Capturing coherence.html...")
        page.goto("http://localhost:5174/coherence.html")
        page.wait_for_selector(".grid-container")
        page.screenshot(path="verification/before_coherence.png")

        browser.close()

if __name__ == "__main__":
    capture_layouts()
