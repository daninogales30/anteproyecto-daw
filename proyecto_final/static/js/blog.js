document.addEventListener('DOMContentLoaded', function () {
    const inputFiltro = document.getElementById('filter-username');
    const clearFilter = document.getElementById('clear-filter');
    const listaItems = document.querySelectorAll('#posts-list .post-item');
    const noResults = document.getElementById('no-results');
    const searchTerm = document.getElementById('search-term');

    function filterPosts() {
        const valor = inputFiltro.value.trim().toLowerCase();
        let visibleCount = 0;

        listaItems.forEach(function (item) {
            const autor = item.getAttribute('data-author');
            const titulo = item.getAttribute('data-title');

            const titleElement = item.querySelector('.post-title');
            const usernameElement = item.querySelector('.post-username');

            titleElement.innerHTML = titleElement.textContent;
            usernameElement.innerHTML = usernameElement.textContent;

            if (!valor) {
                item.style.display = '';
                visibleCount++;
                return;
            }

            if (autor.includes(valor) || titulo.includes(valor)) {
                item.style.display = '';
                visibleCount++;

                if (autor.includes(valor)) {
                    const usernameText = usernameElement.textContent;
                    const regex = new RegExp(valor, 'gi');
                    usernameElement.innerHTML = usernameText.replace(regex, match =>
                        `<span class="highlight">${match}</span>`
                    );
                }
            } else {
                item.style.display = 'none';
            }
        });

        if (visibleCount === 0 && valor) {
            searchTerm.textContent = valor;
            noResults.style.display = 'block';
        } else {
            noResults.style.display = 'none';
        }

        clearFilter.style.display = valor ? 'block' : 'none';
    }

    if (!inputFiltro || !listaItems) {
        console.error('[blog_filter.js] No se encontraron elementos claves en el DOM.');
        return;
    }

    inputFiltro.addEventListener('input', filterPosts);

    if (clearFilter) {
        clearFilter.addEventListener('click', function () {
            inputFiltro.value = '';
            filterPosts();
            inputFiltro.focus();
        });
    }
    filterPosts();
});