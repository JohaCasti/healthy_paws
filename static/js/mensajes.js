setTimeout(function() {
    document.querySelectorAll('.alert').forEach(function(alert) {
        alert.style.opacity = '0';
        alert.style.transform = 'translateX(100%)';
        setTimeout(() => alert.style.display = 'none', 600);
    });
}, 2000); // Desaparece luego de 3 segundos

