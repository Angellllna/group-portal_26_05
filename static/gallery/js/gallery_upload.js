const dropZone  = document.getElementById('dropZone');
const fileInput = document.getElementById('{{ form.file.id_for_label }}');
const preview   = document.getElementById('filePreview');
const fileName  = document.getElementById('fileName');
const removeBtn = document.getElementById('removeFile');

function showFile(file) {
  if (!file) return;
  fileName.textContent = file.name;
  preview.classList.add('visible');
  dropZone.querySelector('.drop-zone__icon').textContent = '✅';
}

function clearFile() {
  fileInput.value = '';
  preview.classList.remove('visible');
  fileName.textContent = '';
  dropZone.querySelector('.drop-zone__icon').textContent = '📂';
}

fileInput.addEventListener('change', () => showFile(fileInput.files[0]));

removeBtn.addEventListener('click', (e) => {
  e.stopPropagation();
  clearFile();
});

dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.classList.add('drag-over');
});
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('drag-over'));
dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropZone.classList.remove('drag-over');
  const file = e.dataTransfer.files[0];
  if (file) {
    const dt = new DataTransfer();
    dt.items.add(file);
    fileInput.files = dt.files;
    showFile(file);
  }
});
