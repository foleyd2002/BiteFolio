document.addEventListener('DOMContentLoaded', function () {
    // Table Sorting
    const table = document.querySelector('table');
    if (table) {
        const headers = table.querySelectorAll('th');
        const tableBody = table.querySelector('tbody');
        const rows = Array.from(tableBody.querySelectorAll('tr'));

        headers.forEach((header, index) => {
            header.addEventListener('click', () => {
                sortTable(index);
            });
        });

        const sortTable = (index) => {
            const direction = headers[index].getAttribute('data-direction') || 'asc';
            const sortedRows = rows.slice().sort((a, b) => {
                let aValue = a.cells[index].textContent.trim();
                let bValue = b.cells[index].textContent.trim();

                // Check if values are numbers and sort numerically
                if (!isNaN(aValue) && !isNaN(bValue)) {
                    return direction === 'asc' ? aValue - bValue : bValue - aValue;
                }

                return direction === 'asc' ? aValue.localeCompare(bValue) : bValue.localeCompare(aValue);
            });

            headers[index].setAttribute('data-direction', direction === 'asc' ? 'desc' : 'asc');

            // Reattach sorted rows
            tableBody.innerHTML = "";
            sortedRows.forEach(row => tableBody.appendChild(row));
        };
    }

    // Smooth Scrolling for Navigation Links
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            const targetId = this.getAttribute('href');

            if (targetId.startsWith('#')) {
                event.preventDefault();
                const targetElement = document.querySelector(targetId);

                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: 'smooth' });
                }
            } else {
                window.location.href = targetId; // Navigate to external links
            }
        });
    });
});
