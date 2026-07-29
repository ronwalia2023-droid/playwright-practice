import { test, expect } from '@playwright/test';

test('can add multiple elements and count them @smoke', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/add_remove_elements/');

  const addButton = page.getByRole('button', { name: 'Add Element' });
  const deleteButtons = page.getByRole('button', { name: 'Delete' });

  // Should start with zero Delete buttons
  await expect(deleteButtons).toHaveCount(0);

  // Click Add 3 times
  await addButton.click();
  await addButton.click();
  await addButton.click();

  // Should now have exactly 3 Delete buttons
  await expect(deleteButtons).toHaveCount(3);
});

test('can remove an added element @regression', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/add_remove_elements/');

  const addButton = page.getByRole('button', { name: 'Add Element' });
  const deleteButtons = page.getByRole('button', { name: 'Delete' });

  await addButton.click();
  await addButton.click();
  await expect(deleteButtons).toHaveCount(2);

  // Click the first Delete button
  await deleteButtons.first().click();

  // Should now have just 1 left
  await expect(deleteButtons).toHaveCount(1);
});