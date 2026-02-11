const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('enemyAPI', {
  loadEnemies: () => ipcRenderer.invoke('load-enemies'),
  saveEnemies: (enemies) => ipcRenderer.invoke('save-enemies', enemies),
  openNewWindow: () => ipcRenderer.invoke('open-new-window')
});
