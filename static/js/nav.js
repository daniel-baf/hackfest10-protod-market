window.addEventListener("DOMContentLoaded", (event) => {
    const _toggle_view_button = document.getElementById("hide-on-mixin")
    _toggle_view_button.addEventListener("click", toggleview(event))
});

function toggleview(event) {
    event.preventDefault();
    let _nav = document.getElementById("navbarNav")
    // alert("hide")
}