function searchTrainers(event) {
    if (event) event.preventDefault();
    
    const query = document.getElementById('trainer-search-input').value;
    
    if (query.trim() !== '') {
        window.location.href = `/search/?q=${encodeURIComponent(query)}`;
    } else {
        window.location.href = '/search/';
    }
}

window.searchTrainers = searchTrainers;