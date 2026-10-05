import { test, expect } from '@playwright/test';

test('can select option 1 and option 2 @smoke', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/dropdown');

  const dropdown = page.locator('#dropdown');

  // Select Option 1 by its visible label
  await dropdown.selectOption({ label: 'Option 1' });
  await expect(dropdown).toHaveValue('1');

  // Select Option 2 by its visible label
  await dropdown.selectOption({ label: 'Option 2' });
  await expect(dropdown).toHaveValue('2');
});

test('placeholder option cannot be selected as a real choice @regression', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/dropdown');

  const dropdown = page.locator('#dropdown');

  // The default/placeholder option should be selected initially
  await expect(dropdown).toHaveValue('');

  // After selecting a real option, confirm it's no longer the placeholder
  await dropdown.selectOption({ label: 'Option 1' });
  await expect(dropdown).not.toHaveValue('');
});