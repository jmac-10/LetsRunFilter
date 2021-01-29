// Saves options to chrome.storage
function save_options() {
  var filterOn = document.getElementById('onoff').checked;
  var blacklist = document.getElementById('blacklist').value
  chrome.storage.sync.set({
    filterOn: filterOn,
    blacklist: blacklist
  }, function() {
    // Update status to let user know options were saved.
    var status = document.getElementById('status');
    status.textContent = 'Options saved.';
    setTimeout(function() {
      status.textContent = '';
    }, 750);
  });
}

// Restores select box and checkbox state using the preferences
// stored in chrome.storage.
function restore_options() {
  chrome.storage.sync.get({
    filterOn: true,
    blacklist: ''
  }, function(items) {
    document.getElementById('blacklist').value = items.blacklist;
    document.getElementById('onoff').checked = items.filterOn;
  });
}
document.addEventListener('DOMContentLoaded', restore_options);
document.getElementById('save').addEventListener('click',
    save_options);