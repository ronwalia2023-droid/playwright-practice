import { test, expect } from '@playwright/test';

test('text appears after clicking start @smoke', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/dynamic_loading/1');

  await expect(page.locator('#finish')).not.toBeVisible();

  await page.getByRole('button', { name: 'Start' }).click();

  // Extended timeout: this page has an intentional ~5s delay,
  // so we give it more headroom than the 5s default to avoid racing it.
  await expect(page.locator('#finish')).toBeVisible({ timeout: 10000 });
  await expect(page.locator('#finish')).toContainText('Hello World!');
});