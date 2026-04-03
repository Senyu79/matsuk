document.addEventListener('DOMContentLoaded', function() {
    const trainerCards = document.querySelectorAll('.trainer-card, .person-item');

    trainerCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';

        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });

    const tariffCards = document.querySelectorAll('.trafic-light, .trafic-infinitty, .trafic-smart');

    tariffCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';

        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100 + 200);
    });
});

const currentYearSpan = document.getElementById('currentYear');
if (currentYearSpan) {
    currentYearSpan.textContent = new Date().getFullYear();
}

function showToast(message, type = 'success') {
    let toast = document.getElementById('toast');
    
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast';
        toast.className = 'toast';
        document.body.appendChild(toast);
    }
    
    toast.textContent = message;
    toast.className = `toast ${type}`;
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

function confirmPurchase(event, tariff, price) {
    event.preventDefault();
    if (confirm(`Вы уверены, что хотите приобрести тариф ${tariff} за ${price} руб.?`)) {
        showToast(`Вы выбрали тариф ${tariff}. Ожидайте звонка менеджера`, 'success');
        return true;
    }
    return false;
}

function confirmFreeTraining(event) {
    event.preventDefault();
    if (confirm('Хотите записаться на бесплатную тренировку?')) {
        showToast('Заявка отправлена! Менеджер свяжется с вами в ближайшее время', 'success');
        return true;
    }
    return false;
}

function confirmJoin(event) {
    event.preventDefault();
    if (confirm('Хотите присоединиться к клубу KURTOFF?')) {
        showToast('Спасибо за интерес! Менеджер свяжется с вами для оформления членства', 'success');
        return true;
    }
    return false;
}
