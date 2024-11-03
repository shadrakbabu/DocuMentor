document.getElementById('search-input').addEventListener('input', function() {
    const query = this.value;
    console.log('Search query:', query);
    // If the input is empty, hide the results
    if (!query) {
        document.getElementById('search-results').style.display = 'none';
        return;
    }

    fetch(`/search/?q=${query}`)
        .then(response => response.json())
        .then(data => {
            const resultsDropdown = document.getElementById('search-results');
            resultsDropdown.innerHTML = ''; // Clear previous results

            if (data.community_posts.length || data.resources.length || data.tutorials.length) {
                resultsDropdown.style.display = 'block'; // Show the dropdown

                const ul = document.createElement('ul'); // Create a list for results

                // Add community posts
                data.community_posts.forEach(post => {
                    const li = document.createElement('li');
                    li.innerHTML = `<a href="/community/${post.id}">${post.heading}</a>`;
                    ul.appendChild(li);
                });

                // Add resources (Corrected field name)
                data.resources.forEach(resource => {
                    const li = document.createElement('li');
                    li.innerHTML = `<a href="/resources/${resource.id}">${resource.file_name}</a>`;  // Updated from 'title' to 'file_name'
                    ul.appendChild(li);
                });

                // Add tutorials (Corrected field name)
                data.tutorials.forEach(tutorial => {
                    const li = document.createElement('li');
                    li.innerHTML = `<a href="/tutorials/${tutorial.id}">${tutorial.topic}</a>`;  // Updated from 'title' to 'topic'
                    ul.appendChild(li);
                });

                resultsDropdown.appendChild(ul); // Add the list to the dropdown
            } else {
                resultsDropdown.style.display = 'none'; // No results, hide dropdown
            }
        });
});

// Hide the results when clicking outside the input
document.addEventListener('click', function(event) {
    const resultsDropdown = document.getElementById('search-results');
    if (!document.getElementById('search-form').contains(event.target)) {
        resultsDropdown.style.display = 'none'; // Hide dropdown
    }
});
