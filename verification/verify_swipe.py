
import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Load the local file
        await page.goto("http://localhost:5174/coherence.html")

        # Start Game
        await page.click("button:has-text('BREATHE')")
        await asyncio.sleep(1)

        # Get a block in the middle
        # We need to find a block that has a valid swap or just any swap to trigger logic
        # For simplicity, we just try to swipe the block at 4,4 to the right.

        # We will inject a script to simulate touch events because Playwright's touch emulation
        # is sometimes tricky with specific React event handlers if not using mobile emulation context.

        # But let's try to verify via screenshot that the game runs first.
        await page.screenshot(path="verification/before_swipe_logic.png")
        print("Screenshot taken.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
