document.addEventListener('DOMContentLoaded', () => {
  AOS.init({
    duration: 1000,
    once: true,
  });

  const fileInput = document.getElementById('fileInput');
  if (fileInput) {
    fileInput.addEventListener('change', (e) => {
      const fileName = document.getElementById('fileName');
      if (e.target.files.length > 0) {
        fileName.innerHTML = `<strong>Выбран файл:</strong> ${e.target.files[0].name}`;
        fileName.style.marginTop = '10px';
      }
    });
  }

  const feedbackForm = document.getElementById('feedbackForm');
  if (feedbackForm) {
    feedbackForm.addEventListener('submit', () => {
      const submitBtn = document.querySelector('.submit-btn');
      if (submitBtn) {
        submitBtn.style.opacity = '0.7';
        submitBtn.innerHTML = 'Отправка... <i class="fas fa-spinner fa-spin"></i>';
      }
    });
  }

  const fileContainer = document.querySelector('.file-input-container');
  if (fileContainer) {
    fileContainer.addEventListener('dragover', (e) => {
      e.preventDefault();
      fileContainer.style.transform = 'translateY(-5px)';
      fileContainer.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.1)';
    });

    fileContainer.addEventListener('dragleave', () => {
      fileContainer.style.transform = 'none';
      fileContainer.style.boxShadow = 'none';
    });
  }
});