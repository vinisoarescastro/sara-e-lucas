// Contagem Regressiva
function atualizarContagem() {
    const dataEvento = new Date('2026-01-10T19:00:00').getTime();
    const agora = new Date().getTime();
    const diferenca = dataEvento - agora;

    const dias = Math.floor(diferenca / (1000 * 60 * 60 * 24));
    const horas = Math.floor((diferenca % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutos = Math.floor((diferenca % (1000 * 60 * 60)) / (1000 * 60));
    const segundos = Math.floor((diferenca % (1000 * 60)) / 1000);

    document.getElementById('dias').innerText = dias.toString().padStart(2, '0');
    document.getElementById('horas').innerText = horas.toString().padStart(2, '0');
    document.getElementById('minutos').innerText = minutos.toString().padStart(2, '0');
    document.getElementById('segundos').innerText = segundos.toString().padStart(2, '0')
    
    if (diferenca < 0) {
        document.querySelector('.countdown-timer').innerHTML = '<h3 style="color: white;">O grande dia chegou! 🎉</h3>';
    }
}

setInterval(atualizarContagem, 1000);
atualizarContagem();

// Copiar Chave PIX
function copiarPix() {
    const chave = 'pix@vscastro.com';
    navigator.clipboard.writeText(chave).then(() => {
        alert('Chave PIX copiada com sucesso!');
    }).catch(() => {
        alert('Erro ao copiar. Chave PIX: pix@vscastro.com');
    });
}

// Scroll suave
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});