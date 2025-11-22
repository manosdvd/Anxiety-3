from playwright.sync_api import sync_playwright, expect

def verify_dyslexia_game():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            # Navigate to the app (assuming default vite port 5173)
            page.goto("http://localhost:5173/dyslexia.html")

            # Wait for the game to load (start screen)
            # Use a more specific selector or role since "DYSLEXIA" appears twice
            expect(page.locator("h2", has_text="DYSLEXIA")).to_be_visible()
            expect(page.get_by_text("WORD HUNT")).to_be_visible()

            # Take a screenshot of the start screen
            page.screenshot(path="verification/dyslexia_start.png")
            print("Start screen screenshot taken.")

            # Start the game
            page.get_by_role("button", name="START").click()

            # Wait for game elements to appear (e.g., score, pause button)
            expect(page.get_by_text("SCORE")).to_be_visible()

            # Wait a bit for the game loop to run (since we fixed state updates related to it)
            page.wait_for_timeout(2000)

            # Take a screenshot of the active game
            page.screenshot(path="verification/dyslexia_gameplay.png")
            print("Gameplay screenshot taken.")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_dyslexia_game()
