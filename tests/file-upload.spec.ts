import { test, expect } from '@playwright/test';
import path from 'path';

test('can upload a file successfully @smoke', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com/upload');

  // Set the file directly on the hidden file input — no OS dialog needed
  const filePath = path.join(__dirname, '..', 'test-upload.txt');
  await page.locator('#file-upload').setInputFiles(filePath);

  // Click the upload button
  await page.getByRole('button', { name: 'Upload' }).click();

  // Confirm the upload succeeded and shows the correct filename
  await expect(page.locator('h3')).toContainText('File Uploaded!');
  await expect(page.locator('#uploaded-files')).toContainText('test-upload.txt');
});