window.history.pushState(null, null, window.location.href);
    
window.onpopstate = function () {
    document.cookie = 'token=; expires=Thu, 01 Jan 2020 00:00:00 UTC; path=/';
        
    fetch('/logout', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    }).then(() => {
        window.location.reload();
    });
};
