const { contextBridge } = require('electron');

contextBridge.exposeInMainWorld('ceberus', {
  // Reserved for future IPC bridges
});
