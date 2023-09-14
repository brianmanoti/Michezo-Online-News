document.addEventListener('DOMContentLoaded', function () {
    let profileDropdownList = document.querySelector(".profile-dropdown-list");
    let btn = document.querySelector(".profile-dropdown-btn");
  
    const toggle = () => profileDropdownList.classList.toggle("active");
  
    // Add a click event listener to the profile-dropdown-btn
    btn.addEventListener('click', function (e) {
      e.stopPropagation(); // Prevent the click event from propagating to the window
      toggle(); // Toggle the active class
    });
  
    // Add a click event listener to the window to close the dropdown when clicking outside of it
    window.addEventListener('click', function (e) {
      if (!profileDropdownList.contains(e.target) && e.target !== btn) {
        profileDropdownList.classList.remove("active");
      }
    });
  });
  