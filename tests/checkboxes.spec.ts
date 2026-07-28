import { test, expect } from '@playwright/test';

test('checkbox 2 can be unchecked and rechecked @smoke', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/checkboxes');

  const checkbox2 = page.locator('#checkboxes input').nth(1);

  // It actually starts CHECKED on this site
  await expect(checkbox2).toBeChecked();

  // Uncheck it
  await checkbox2.uncheck();
  await expect(checkbox2).not.toBeChecked();

  // Check it again
  await checkbox2.check();
  await expect(checkbox2).toBeChecked();
});

test('checkbox 1 can be checked and unchecked @smoke', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/checkboxes');

  const checkbox1 = page.locator('#checkboxes input').nth(0);

  // This one starts UNCHECKED
  await expect(checkbox1).not.toBeChecked();

  await checkbox1.check();
  await expect(checkbox1).toBeChecked();

  await checkbox1.uncheck();
  await expect(checkbox1).not.toBeChecked();
});