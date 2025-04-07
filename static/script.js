// Update fields list on page load
document.addEventListener('DOMContentLoaded', function() {
    updateFieldsList();
});

// Accordion functionality
const accordionHeaders = document.querySelectorAll('.accordion-header');
accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
        const content = header.nextElementSibling;
        const isOpen = content.style.display === 'block';
        content.style.display = isOpen ? 'none' : 'block';
        header.setAttribute('aria-expanded', !isOpen);
    });
});