// Enable side panel to open upon clicking the action icon
chrome.sidePanel
  .setPanelBehavior({ openPanelOnActionClick: true })
  .catch((error) => console.error("Error setting side panel behavior:", error));