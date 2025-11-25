
import os
from playwright.sync_api import sync_playwright

def verify_fix():
    os.makedirs('verification', exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use mobile viewport
        context = browser.new_context(viewport={'width': 375, 'height': 667})
        page = context.new_page()

        # Capture Coherence (After Fix)
        print("Capturing coherence.html (fixed)...")
        page.goto("http://localhost:5174/coherence.html")
        page.wait_for_selector(".grid-container")

        # Verify specific CSS values if possible (optional, but visual is better)
        header = page.locator("h1")
        # Ensure text is 2xl (approx 24px or 1.5rem) - verifying class presence is easier
        # Tailwind classes might not be computed styles directly, but we can check the element

        page.screenshot(path="verification/after_coherence.png")

        # Capture Dyslexia & Discalculia for sanity check
        print("Capturing dyslexia.html...")
        page.goto("http://localhost:5174/dyslexia.html")
        page.wait_for_selector(".grid-container")
        page.screenshot(path="verification/check_dyslexia.png")

        print("Capturing discalculia.html...")
        page.goto("http://localhost:5174/discalculia.html")
        page.wait_for_selector(".grid-container")
        page.screenshot(path="verification/check_discalculia.png")

        browser.close()

if __name__ == "__main__":
    verify_fix()
