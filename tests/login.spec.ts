import { test, expect } from '@playwright/test';

test('login and logout flow', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/login');

  await page.getByRole('textbox', { name: 'Username' }).fill('tomsmith');
  await page.getByRole('textbox', { name: 'Password' }).fill('SuperSecretPassword!');
  await page.getByRole('button', { name: ' Login' }).click();

  await expect(page.locator('.flash.success')).toContainText('You logged into a secure area');
  await expect(page).toHaveURL(/.*secure/);

  await page.getByRole('link', { name: 'Logout' }).click();

  await expect(page.locator('.flash.success')).toContainText('You logged out of the secure area');
  await expect(page).toHaveURL(/.*login/);
});

test('shows error with wrong password', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/login');

  await page.getByRole('textbox', { name: 'Username' }).fill('tomsmith');
  await page.getByRole('textbox', { name: 'Password' }).fill('WrongPassword123');
  await page.getByRole('button', { name: ' Login' }).click();

  await expect(page.locator('.flash.error')).toContainText('Your password is invalid!');
  await expect(page).toHaveURL(/.*login/);
});

test('shows error with wrong username', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/login');

  await page.getByRole('textbox', { name: 'Username' }).fill('wronguser');
  await page.getByRole('textbox', { name: 'Password' }).fill('SuperSecretPassword!');
  await page.getByRole('button', { name: ' Login' }).click();

  await expect(page.locator('.flash.error')).toContainText('Your username is invalid!');
  await expect(page).toHaveURL(/.*login/);
});