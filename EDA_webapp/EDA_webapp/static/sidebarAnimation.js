let dashboardVisible = false;

function sidebarToggle() {
    if (!dashboardVisible) {
        document.getElementById("sidebar").style.width = "300px";
        document.getElementById("content").style.marginLeft = "300px";
    } else {
        document.getElementById("sidebar").style.width = "0";
        document.getElementById("content").style.marginLeft= "0";
    }
    dashboardVisible = !dashboardVisible;
}