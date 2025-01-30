document.addEventListener('DOMContentLoaded', function () {
    // Table Sorting
    const table = document.querySelector('table');
    if (table) {
        const headers = table.querySelectorAll('th');
        const tableBody = table.querySelector('tbody');
        const rows = tableBody.querySelectorAll('tr');

        headers.forEach((header, index) => {
            header.addEventListener('click', () => {
                sortTable(index);
            });
        });

        const sortTable = (index) => {
            const direction = headers[index].getAttribute('data-direction') || 'asc';
            const sortedRows = Array.from(rows).sort((a, b) => {
                const aValue = a.querySelectorAll('td')[index].textContent.trim();
                const bValue = b.querySelectorAll('td')[index].textContent.trim();

                return direction === 'asc' ? aValue.localeCompare(bValue) : bValue.localeCompare(aValue);
            });

            headers[index].setAttribute('data-direction', direction === 'asc' ? 'desc' : 'asc');

            while (tableBody.firstChild) {
                tableBody.removeChild(tableBody.firstChild);
            }

            sortedRows.forEach(row => tableBody.appendChild(row));
        };
    }

    // Smooth Scrolling for Navigation Links
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId.startsWith('#')) {
                document.querySelector(targetId).scrollIntoView({
                    behavior: 'smooth'
                });
            } else {
                window.location.href = targetId; // Navigate to other pages
            }
        });
    });
});
