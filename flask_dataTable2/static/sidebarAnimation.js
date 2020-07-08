let dashboardVisible = false;

function sidebarToggle() {
    if (!dashboardVisible) {
        document.getElementById("sidebar").style.width = "250px";
        document.getElementById("content").style.marginLeft = "250px";
    } else {
        document.getElementById("sidebar").style.width = "0";
        document.getElementById("content").style.marginLeft= "0";
    }
    dashboardVisible = !dashboardVisible;
}