import { test, expect } from '@playwright/test';

test('handles simple JS alert @smoke', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/javascript_alerts');

  // Set up the listener BEFORE clicking, so Playwright is ready to catch the dialog
  page.on('dialog', async (dialog) => {
    expect(dialog.type()).toBe('alert');
    expect(dialog.message()).toBe('I am a JS Alert');
    await dialog.accept(); // clicks "OK"
  });

  await page.getByRole('button', { name: 'Click for JS Alert' }).click();

  await expect(page.locator('#result')).toContainText('You successfully clicked an alert');
});

test('can accept a JS confirm @smoke', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/javascript_alerts');

  page.on('dialog', async (dialog) => {
    expect(dialog.type()).toBe('confirm');
    await dialog.accept(); // clicks "OK"
  });

  await page.getByRole('button', { name: 'Click for JS Confirm' }).click();

  await expect(page.locator('#result')).toContainText('You clicked: Ok');
});

test('can dismiss a JS confirm @regression', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/javascript_alerts');

  page.on('dialog', async (dialog) => {
    await dialog.dismiss(); // clicks "Cancel"
  });

  await page.getByRole('button', { name: 'Click for JS Confirm' }).click();

  await expect(page.locator('#result')).toContainText('You clicked: Cancel');
});

test('can enter text into a JS prompt @regression', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/javascript_alerts');

  page.on('dialog', async (dialog) => {
    expect(dialog.type()).toBe('prompt');
    await dialog.accept('Hello from Playwright'); // types text, then clicks OK
  });

  await page.getByRole('button', { name: 'Click for JS Prompt' }).click();

  await expect(page.locator('#result')).toContainText('You entered: Hello from Playwright');
});