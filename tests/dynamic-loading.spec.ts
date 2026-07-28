import { test, expect } from '@playwright/test';

test('text appears after clicking start @smoke', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/dynamic_loading/1');

  // Confirm the text is NOT visible yet
  await expect(page.locator('#finish')).not.toBeVisible();

  // Click the Start button
  await page.getByRole('button', { name: 'Start' }).click();

  // Playwright automatically waits for this to become visible —
  // no manual timeout needed. Default wait is up to 5 seconds (configurable).
  await expect(page.locator('#finish')).toBeVisible();
  await expect(page.locator('#finish')).toContainText('Hello World!');
});