const { app, BrowserWindow, ipcMain } = require('electron/main');
const path = require('path');
const fs = require('fs');

const ENEMIES_PATH = path.join(__dirname, '..', '..', 'src', 'data', 'enemies.json');

const createWindow = () => {
  const win = new BrowserWindow({
    width: 900,
    height: 650,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  });

  win.loadFile('index.html');
};

ipcMain.handle('load-enemies', async () => {
  const data = fs.readFileSync(ENEMIES_PATH, 'utf-8');
  const parsed = JSON.parse(data);
  return parsed.enemies_list;
});

ipcMain.handle('save-enemies', async (_event, enemies) => {
  const data = { enemies_list: enemies };
  fs.writeFileSync(ENEMIES_PATH, JSON.stringify(data, null, 4), 'utf-8');
  return true;
});

ipcMain.handle('open-new-window', () => {
  createWindow();
});

app.whenReady().then(() => {
  createWindow();
    
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
